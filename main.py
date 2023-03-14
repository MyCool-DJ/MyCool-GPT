from pathlib import Path
import re

data_path = Path("training/facts/")
filename = "Facebook_data.txt"
full_path = data_path / filename

with open(full_path, "r") as f:
    lines = f.readlines()

# regex pattern for matching timestamps
pattern = re.compile(r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:\s\d+)?$")

# filter out lines that start with the timestamp
new_lines = [line for line in lines if not pattern.match(line)]

with open("main.py", "w") as f:
    f.writelines(new_lines)


