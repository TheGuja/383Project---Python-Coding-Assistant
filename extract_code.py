import re

def extract_code(entry):
    full_text = entry["python"]

    match = re.search(r"```python(.*?)```", full_text, re.DOTALL)
    if match:
        python_code = match.group(1).strip()
        return(python_code)
    else:
        return("No Python code block found.")
    
def extract_content(entry):
    full_content = entry["content"]
    cleaned_content = re.sub(r"\*\*Follow-up:\*\*.*", "", full_content, flags=re.DOTALL).strip()

    return cleaned_content