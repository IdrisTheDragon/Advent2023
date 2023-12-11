import sys
from pathlib import Path

assert len(sys.argv) > 1, "Missing day"
day_num = int(sys.argv[1])

day_dir = Path(f"day-{day_num}")
day_dir.mkdir()

files = ["input.txt","example.txt",f"day{day_num}.py"]

for file in files:
    (day_dir / file).touch()
