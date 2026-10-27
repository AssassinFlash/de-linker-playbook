#!/usr/bin/env python3
"""Serve the local lead-generation learning pages and open one in a browser."""
from __future__ import annotations

import argparse
import os
import socket
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = (ROOT / "deliverables" / "lead" / "00-system").resolve()
APP_PATH = "/lead-academy.html"
LOCK = Path.home() / ".config" / "de-linker-playbook" / "lead-academy.port"
HOST = "127.0.0.1"
PREFERRED_PORT = 8778


def port_open(port: int) -> bool:
    probe = socket.socket()
    probe.settimeout(0.25)
    try:
        probe.connect((HOST, port))
        return True
    except OSError:
        return False
    finally:
        probe.close()


def running_port() -> int | None:
    if not LOCK.exists():
        return None
    text = LOCK.read_text(encoding="utf-8").strip()
    if not text.isdigit():
        return None
    port = int(text)
    return port if port_open(port) else None


def free_port() -> int:
    for port in range(PREFERRED_PORT, PREFERRED_PORT + 30):
        if port_open(port):
            continue
        probe = socket.socket()
        try:
            probe.bind((HOST, port))
            return port
        except OSError:
            continue
        finally:
            probe.close()
    raise SystemExit(f"{PREFERRED_PORT}–{PREFERRED_PORT + 29} 都被占用了")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DATA), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        return

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def open_url(url: str) -> None:
    if os.environ.get("LEAD_ACADEMY_NO_OPEN") != "1":
        webbrowser.open(url)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--page",
        default=APP_PATH.lstrip("/"),
        help="00-system 下的页面，例如 lead-academy.html 或 knowledge-base.html",
    )
    args = parser.parse_args()
    page = args.page.strip().lstrip("/")
    page_file = (DATA / page).resolve()
    if DATA not in page_file.parents or not page_file.is_file():
        raise SystemExit(f"找不到页面：{page}")
    page_path = "/" + page

    existing = running_port()
    if existing:
        open_url(f"http://{HOST}:{existing}{page_path}")
        return 0

    port = free_port()
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    LOCK.write_text(str(port), encoding="utf-8")
    os.chmod(LOCK, 0o600)
    server = ThreadingHTTPServer((HOST, port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f"http://{HOST}:{port}{page_path}"
    print(url, flush=True)
    print("关掉这个窗口，学习应用就停。", flush=True)
    open_url(url)
    try:
        thread.join()
    except KeyboardInterrupt:
        server.shutdown()
    finally:
        LOCK.unlink(missing_ok=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
