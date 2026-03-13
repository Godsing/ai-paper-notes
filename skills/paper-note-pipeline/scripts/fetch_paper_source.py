#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

UA = "Mozilla/5.0 OpenClaw/Allen ai-paper-notes"

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in {"script", "style", "svg", "noscript"} and self.skip:
            self.skip -= 1
        if tag in {"p", "div", "section", "article", "h1", "h2", "h3", "li", "br"}:
            self.parts.append("\n")
    def handle_data(self, data):
        if not self.skip:
            text = data.strip()
            if text:
                self.parts.append(text)
                self.parts.append(" ")
    def text(self):
        text = "".join(self.parts)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        return text.strip()


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, resp.read().decode("utf-8", "ignore")


def pick_arxiv_id(text: str) -> str | None:
    text = text.strip()
    m = re.search(r"arxiv\.org/(?:abs|html|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?", text)
    if m:
        return m.group(1)
    m = re.fullmatch(r"([0-9]{4}\.[0-9]{4,5})(?:v\d+)?", text)
    if m:
        return m.group(1)
    return None


def summarize_text(text: str, limit: int = 12000) -> str:
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text[:limit].strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper", help="arXiv id or arXiv URL")
    args = ap.parse_args()

    arxiv_id = pick_arxiv_id(args.paper)
    if not arxiv_id:
        print(json.dumps({"ok": False, "error": "unsupported paper id/url"}, ensure_ascii=False))
        sys.exit(1)

    html_url = f"https://arxiv.org/html/{arxiv_id}"
    abs_url = f"https://arxiv.org/abs/{arxiv_id}"

    result = {
        "ok": True,
        "paper_id": arxiv_id,
        "html_url": html_url,
        "abs_url": abs_url,
        "used": None,
        "canonical_url": None,
        "text": None,
    }

    try:
        status, raw = fetch(html_url)
        if status == 200:
            parser = TextExtractor()
            parser.feed(raw)
            text = summarize_text(parser.text())
            if text:
                result["used"] = "html"
                result["canonical_url"] = html_url
                result["text"] = text
                print(json.dumps(result, ensure_ascii=False, indent=2))
                return
    except Exception:
        pass

    try:
        status, raw = fetch(abs_url)
        if status == 200:
            parser = TextExtractor()
            parser.feed(raw)
            text = summarize_text(parser.text(), limit=8000)
            result["used"] = "abs"
            result["canonical_url"] = abs_url
            result["text"] = text
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return
    except Exception as e:
        result["ok"] = False
        result["error"] = str(e)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(1)

if __name__ == "__main__":
    main()
