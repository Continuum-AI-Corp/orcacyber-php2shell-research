#!/usr/bin/env python3
"""Offline PHP2Shell version triage. A vendor backport can supersede this check."""
import argparse
import re

FIXED = {"8.2": (8, 2, 35), "8.3": (8, 3, 36), "8.4": (8, 4, 27), "8.5": (8, 5, 12)}


def assess(version):
    match = re.search(r"\b(\d+)\.(\d+)\.(\d+)\b", version)
    if not match:
        return "UNKNOWN: Cannot parse PHP version"
    numbers = tuple(map(int, match.groups()))
    branch = f"{numbers[0]}.{numbers[1]}"
    if branch in FIXED:
        if numbers >= FIXED[branch]:
            return "FIXED UPSTREAM: Verify deployed PHP workers use this build"
        return f"UPDATE REQUIRED: Upstream fixed at {'.'.join(map(str, FIXED[branch]))}"
    if numbers[0] < 8 or (numbers[0] == 8 and numbers[1] < 2):
        return "LEGACY/EOL: Check vendor backports or migrate to supported PHP"
    return "UNASSESSED BRANCH: Consult upstream and vendor advisories"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help='e.g. "PHP 8.4.26 (cli)"')
    args = parser.parse_args()
    print(assess(args.version))
    print("Note: Linux vendors may backport fixes without changing the upstream version number.")
