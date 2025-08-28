import os
import re

def extract_triple_quoted(text):
    match = re.search(r"```(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None

def process_and_write(input_dir, output_dir, file_extension=".txt"):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(file_extension):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                extracted = extract_triple_quoted(content)

            if extracted:
                with open(output_path, 'w', encoding='utf-8') as outfile:
                    outfile.write(extracted)


input_directory = '/Users/guja/College/Spring 2025/CS 383/group-project-383-project-teateam/Pseudocode/leetcode_easy_pseudocode'
output_directory = '/Users/guja/College/Spring 2025/CS 383/group-project-383-project-teateam/Pseudocode/leetcode_easy_pseudocode'
process_and_write(input_directory, output_directory)