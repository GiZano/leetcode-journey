import os
import re

def generate_table():
    # Define the directory containing the solutions
    path = "solutions"
    files_data = []
    
    # Check if the directory exists
    if not os.path.exists(path):
        return ""

    # Walk through the directory and its subdirectories to find all .py files
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                files_data.append(os.path.join(root, file))
    
    # Initialize the table header
    rows = [
        "| # | Title | Complexity (Time / Space) | Code |",
        "|---|-------|---------------------------|------|"
    ]

    # Sort files to ensure numerical/alphabetical order in the table
    for file_path in sorted(files_data):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract data using Regex from the docstrings
            prob_match = re.search(r"Problem:\s*(\d+)\.?\s*(.*)", content)
            time_match = re.search(r"Time:\s*(O\(.*?\))", content)
            space_match = re.search(r"Space:\s*(O\(.*?\))", content)

            # If a valid Problem tag is found, format it for the table
            if prob_match:
                num, title = prob_match.groups()
                t_comp = time_match.group(1) if time_match else "N/A"
                s_comp = space_match.group(1) if space_match else "N/A"
                
                # Replace backslashes with forward slashes for GitHub markdown links
                github_path = file_path.replace("\\", "/")
                rows.append(f"| {num} | **{title.strip()}** | {t_comp} / {s_comp} | [Python](./{github_path}) |")
    
    # Join all rows to form the final markdown table
    return "\n".join(rows)

def update_readme():
    readme_path = "README.md"
    start_marker = "<!-- TABLE_START -->"
    end_marker = "<!-- TABLE_END -->"

    if not os.path.exists(readme_path):
        print("Error: README.md not found.")
        return

    # Read the current content of the README
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Generate the new table content
    new_table = generate_table()
    
    new_content = []
    skip = False
    found_markers = False

    # Safely replace the content between markers line by line
    for line in lines:
        if start_marker in line:
            new_content.append(line)
            new_content.append(new_table + "\n")
            skip = True
            found_markers = True
            continue
        if end_marker in line:
            new_content.append(line)
            skip = False
            continue
        if not skip:
            new_content.append(line)

    # Write the updated content back to the README if markers were successfully found
    if found_markers:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.writelines(new_content)
        print("README.md updated successfully!")
    else:
        print("Error: HTML markers not found! Please check your README.md format.")

if __name__ == "__main__":
    update_readme()