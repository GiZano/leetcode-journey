import os
import re

def generate_table():
    path = "solutions"
    files_data = []
    
    # Walk through the directories
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                files_data.append(os.path.join(root, file))
    
    # Table Headers
    rows = [
        "| # | Title | Complexity (Time / Space) | Code |",
        "|---|-------|---------------------------|------|"
    ]

    # Order based on numbers
    for file_path in sorted(files_data):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract data
            prob_match = re.search(r"Problem:\s*(\d+)\.?\s*(.*)", content)
            time_match = re.search(r"Time:\s*(O\(.*?\))", content)
            space_match = re.search(r"Space:\s*(O\(.*?\))", content)

            if prob_match:
                num, title = prob_match.groups()
                t_comp = time_match.group(1) if time_match else "N/A"
                s_comp = space_match.group(1) if space_match else "N/A"
                
                # Clean path for GitHub
                github_path = file_path.replace("\\", "/")
                link = f"[Python](./{github_path})"
                
                rows.append(f"| {num} | **{title.strip()}** | {t_comp} / {s_comp} | {link} |")
    
    return "\n".join(rows)

def update_readme():
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print("Error: README.md not found!")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate new table
    new_table = generate_table()
    
    # Exact markers
    start_marker = ""
    end_marker = ""
    
    # Robust regex robusta to find everything that stands between markers
    pattern = f"{start_marker}.*?{end_marker}"
    replacement = f"{start_marker}\n{new_table}\n{end_marker}"
    
    if start_marker in content and end_marker in content:
        # Single and safe substitution
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("README updated!")
    else:
        print("Error: Marker not found int README.md")

if __name__ == "__main__":
    update_readme()