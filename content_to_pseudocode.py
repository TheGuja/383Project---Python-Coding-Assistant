import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env.local')

_open_ai_tkn = os.environ.get('OPENAI_KEY')
_project_tkn = os.environ.get('OPENAI_PROJECT')
_organisation_tkn = os.environ.get('OPENAI_ORG')

client = OpenAI(
  organization=_organisation_tkn,
  project=_project_tkn,
  api_key=_open_ai_tkn
)

# Converts from Problem Description to Pseudocode

# Content directory
content_dir = "/Users/guja/College/Spring 2025/CS 383/group-project-383-project-teateam/Problem Description/leetcode_easy_content"

# Output directory
output_dir = "/Users/guja/College/Spring 2025/CS 383/group-project-383-project-teateam/Pseudocode/leetcode_easy_pseudocode"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(content_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(content_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        user_content = f"Convert the following description into pseudocode. Think step by step. Here is the description: \n\n{content}"
        
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": user_content}
            ],
            model="gpt-4o-mini",
            max_tokens=500
        )

        pseudocode = response.choices[0].message.content.strip()

        output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_converted.txt")
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(pseudocode)