#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import mimetypes
import os
import re
import ssl
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "assets" / "images"
TARGET_SUFFIXES = {".html", ".css", ".js"}
EXCLUDED_DIRS = {"docs"}
URL_RE = re.compile(r"https://images\.unsplash\.com/[^\s\"'<>)]*")


def iter_target_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TARGET_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in EXCLUDED_DIRS:
            continue
        yield path


def find_urls():
    urls = []
    for path in iter_target_files():
        urls.extend(URL_RE.findall(path.read_text(errors="ignore")))
    return sorted(set(urls))


def filename_for(url: str, content_type: str | None = None) -> str:
    parsed = urllib.parse.urlparse(url)
    stem = Path(parsed.path).name or "unsplash-image"
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem).strip(".-_") or "unsplash-image"
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
    ext = Path(stem).suffix.lower()
    base = stem[: -len(ext)] if ext else stem
    if not ext:
        guessed = mimetypes.guess_extension((content_type or "").split(";", 1)[0].strip())
        if guessed in {".jpe", ".jpeg"}:
            guessed = ".jpg"
        ext = guessed if guessed in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"} else ".jpg"
    if ext == ".jpeg":
        ext = ".jpg"
    safe = f"unsplash-{base}-{digest}{ext}"
    return re.sub(r"[^A-Za-z0-9._-]+", "-", safe)


def download(url: str, dest: Path) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 static-clone-localizer"})
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=45, context=context) as resp:
        content_type = resp.headers.get("Content-Type")
        data = resp.read()
    final = IMAGE_DIR / filename_for(url, content_type)
    final.write_bytes(data)
    if dest != final and dest.exists():
        dest.unlink()
    return final.name


def relative_reference(path: Path, image_name: str) -> str:
    target = IMAGE_DIR / image_name
    return Path(os.path.relpath(target, path.parent)).as_posix()


def main() -> int:
    urls = find_urls()
    print(f"unique_unsplash_urls_before {len(urls)}")
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    mapping = {}
    for idx, url in enumerate(urls, 1):
        provisional = IMAGE_DIR / filename_for(url)
        if provisional.exists():
            name = provisional.name
        else:
            name = download(url, provisional)
            time.sleep(0.05)
        mapping[url] = name
        print(f"downloaded {idx}/{len(urls)} {name}")
    changed = 0
    for path in iter_target_files():
        original = path.read_text(errors="ignore")
        updated = original
        for url, name in mapping.items():
            if url in updated:
                updated = updated.replace(url, relative_reference(path, name))
        if updated != original:
            path.write_text(updated)
            changed += 1
            print(f"rewrote {path.relative_to(ROOT)}")
    remaining = find_urls()
    print(f"unique_unsplash_urls_after {len(remaining)}")
    return 0 if not remaining else 1

if __name__ == "__main__":
    raise SystemExit(main())
