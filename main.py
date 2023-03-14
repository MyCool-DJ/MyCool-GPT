from pathlib import Path
import re

data_path = Path("training/facts/")
filename = "Facebook_data.txt"
full_path = data_path / filename

with open(full_path, "r") as f:
    lines = f.readlines()

pattern = re.compile(r"^[A-Z][a-z]{2}\s\d{1,2},\s\d{4}\s\d{1,2}:\d{2}:\d{2}[ap]m$")  # update pattern to match new format

# filter out lines that contain timestamps
new_lines = [line for line in lines if not pattern.match(line)]

with open(full_path, "w") as f:
    f.writelines(new_lines)

print("Done")