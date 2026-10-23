#!/usr/bin/env python3
"""Offline counter for worker-crash signatures in Apache logs."""
import argparse
from collections import Counter
from pathlib import Path
import re

PATTERN = re.compile(r"exit signal (Abort \(6\)|Segmentation fault \(11\))", re.I)
if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("log_file")
    data = Path(p.parse_args().log_file).read_text(errors="replace")
    counts = Counter(PATTERN.findall(data))
    for signal, count in sorted(counts.items()):
        print(f"{signal}: {count}")
    print("Crashes are not conclusive evidence of PHP2Shell exploitation.")
