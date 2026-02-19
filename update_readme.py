import os
import re

def generate_table():
    path = "solutions" 
    files_data = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                files_data.append(os.path.join(root, file))
    
    rows = [
        "| # | Title | Complexity (Time / Space) | Code |", 
        "|---|-------|---------------------------|------|"
    ]

    for file_path in sorted(files_data):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            prob_match = re.search(r"Problem:\s*(\d+)\s+(.*)", content)
            time_match = re.search(r"Time:\s*(O\([^)]+\))", content)
            space_match = re.search(r"Space:\s*(O\([^)]+\))", content)

            if prob_match:
                num, title = prob_match.groups()
                time_comp = time_match.group(1) if time_match else "N/A"
                space_comp = space_match.group(1) if space_match else "N/A"
                clean_path = file_path.replace("\\", "/") 
                link = f"[Python](./{clean_path})"
                
                rows.append(f"| {num} | **{title.strip()}** | {time_comp} / {space_comp} | {link} |")
    
    return "\n".join(rows)

def update_readme():
    readme_path = "README.md"
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    new_table = generate_table()
    
    pattern = r"(\n).*?(\n)"
    updated_content = re.sub(pattern, rf"\1{new_table}\2", readme_content, flags=re.DOTALL)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

if __name__ == "__main__":
    update_readme()
    print("README.md succesfully updated!!")