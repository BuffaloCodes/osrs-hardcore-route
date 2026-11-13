"""Checks starter-guide.md. Run it from anywhere: python tools/check-guide.py

Checks:
- every wiki link returns HTTP 200
- the number of section headers equals the number of level tables
- the number of Rewards lines equals the number of quest links
- the first line is a Last Updated line, and its date is not older than the last commit that changed the guide
- there are no em dashes
"""
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

GUIDE = Path(__file__).resolve().parent.parent / "starter-guide.md"
text = GUIDE.read_text(encoding="utf-8")
problems = []

link_pattern = r"\]\((https://oldschool\.runescape\.wiki/[^)]+)\)"
all_links = re.findall(link_pattern, text)

for url in sorted(set(all_links)):
    request = urllib.request.Request(url, headers={"User-Agent": "guide-link-check"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            if response.status != 200:
                problems.append(f"{url} returned {response.status}")
    except urllib.error.HTTPError as error:
        problems.append(f"{url} returned {error.code}")
    except urllib.error.URLError as error:
        problems.append(f"{url} failed: {error.reason}")

headers = len(re.findall(r"^## ", text, re.M))
tables = text.count("**Estimated levels after this section:**")
if headers != tables:
    problems.append(f"{headers} section headers but {tables} level tables")

rewards = len(re.findall(r"^  - Rewards:", text, re.M))
if rewards != len(all_links):
    problems.append(f"{len(all_links)} quest links but {rewards} Rewards lines")

updated = re.match(r"Last Updated: (\d{1,2} \w+ \d{4})\n", text)
if not updated:
    problems.append("the first line is not a Last Updated line")
else:
    try:
        stamped = datetime.strptime(updated.group(1), "%d %B %Y").date()
        committed = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(GUIDE)],
            cwd=GUIDE.parent, capture_output=True, text=True, check=True,
        ).stdout.strip()
        if committed and stamped < datetime.strptime(committed, "%Y-%m-%d").date():
            problems.append(f"Last Updated is {stamped} but the guide was last committed on {committed}")
    except ValueError:
        problems.append("the Last Updated date could not be read")
    except (OSError, subprocess.CalledProcessError):
        pass  # git is not available, so skip this check

if "—" in text:
    problems.append("the guide contains an em dash")

if problems:
    print("Problems found:")
    for problem in problems:
        print(f"- {problem}")
    sys.exit(1)

print(f"OK: {len(set(all_links))} links, {headers} sections, {tables} level tables, {rewards} reward lines.")
