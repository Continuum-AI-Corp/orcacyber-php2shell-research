#!/usr/bin/env python3
"""Offline summary of a previously captured HTTP response. Never prints cookie contents."""
import argparse
from pathlib import Path
from urllib.parse import unquote_to_bytes


def summarize(path):
    data = Path(path).read_bytes()
    head = data.split(b"\r\n\r\n", 1)[0]
    for line in head.split(b"\r\n"):
        if not line.lower().startswith(b"set-cookie:"):
            continue
        cookie = line.split(b":", 1)[1].strip().split(b";", 1)[0]
        name, sep, value = cookie.partition(b"=")
        if not sep or name.strip().lower() != b"phpsessid":
            continue
        decoded = unquote_to_bytes(value.decode("latin-1"))
        print(f"PHPSESSID encoded_length={len(value)} decoded_length={len(decoded)}")
        print(f"Unusually large value: {len(decoded) > 256}")
        print("Value redacted; unusual size is an investigation lead, not proof of exploitation.")
        return
    print("No PHPSESSID Set-Cookie header found")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("response_file", help="Local HTTP response file, not a URL")
    summarize(p.parse_args().response_file)
