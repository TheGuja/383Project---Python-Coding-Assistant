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

# Input directory
pseudocode_dir = "/Users/guja/College/Spring 2025/CS 383/group-project-383-project-teateam/Pseudocode/leetcode_easy_pseudocode"

# Output directory
output_dir = "/Users/guja/College/Spring 2025/CS 383/group-project-383-project-teateam/LLM Outputs/leetcode_easy_outputs"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(pseudocode_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(pseudocode_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            pseudocode = file.read()
        
        user_content = f"Convert the following pseudocode into Python. Think line by line. Here are the requirements for the output:\n1) Add comments to the code to explain your thought process.\n2) Only return a Python code block.\n3) Do not output any additional information like usage or explanation of the code.\n\nHere is the pseudocode: \n\n{pseudocode}"
        
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": user_content}
            ],
            model="gpt-4o-mini",
            max_tokens=500
        )

        python_code = response.choices[0].message.content.strip()

        output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_converted.py")
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(python_code)