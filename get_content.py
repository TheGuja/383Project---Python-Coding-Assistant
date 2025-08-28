from datasets import load_dataset
from extract_code import extract_content
import os

ds = load_dataset("greengerong/leetcode", split="train")
        
# Output directory
output_dir = "/Users/guja/College/Spring 2025/CS 383/group-project-383-project-teateam/Entries/leetcode_easy"
os.makedirs(output_dir, exist_ok=True)

for idx, point in enumerate(ds):
    if point["difficulty"] == "Easy":
        content = extract_content(point)
        file_name = os.path.join(output_dir, f"entry_{idx+1}.txt")

        with open(file_name, "w") as f:
            f.write(f"Problem Statement:\n{content}\n\n")