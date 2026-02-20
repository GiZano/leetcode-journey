import os
import re

def generate_tables():
    # Define the directory containing the solutions
    path = "solutions"
    
    # Dictionaries to hold parsed data per difficulty
    problems = {
        "easy": [],
        "medium": [],
        "hard": []
    }
    
    # Check if the directory exists
    if not os.path.exists(path):
        return {}

    # Walk through the directory and parse files
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                
                # Determine difficulty from folder name (defaults to easy if not found)
                diff = "easy"
                if "medium" in file_path.lower():
                    diff = "medium"
                elif "hard" in file_path.lower():
                    diff = "hard"

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Extract data using Regex from the docstrings
                    prob_match = re.search(r"Problem:\s*(\d+)\.?\s*(.*)", content)
                    time_match = re.search(r"Time:\s*(O\(.*?\))", content)
                    space_match = re.search(r"Space:\s*(O\(.*?\))", content)

                    if prob_match:
                        num, title = prob_match.groups()
                        t_comp = time_match.group(1) if time_match else "N/A"
                        s_comp = space_match.group(1) if space_match else "N/A"
                        github_path = file_path.replace("\\", "/")
                        
                        # Append dictionary with data, saving num as integer for proper sorting!
                        problems[diff].append({
                            "num": int(num), 
                            "title": title.strip(),
                            "t_comp": t_comp,
                            "s_comp": s_comp,
                            "path": github_path
                        })

    # Generate Markdown tables for each difficulty
    tables = {}
    for diff in problems.keys():
        if not problems[diff]:
            tables[diff] = "*Nessun problema risolto in questa categoria per ora.*"
            continue
            
        # Sort numerically by problem ID
        problems[diff].sort(key=lambda x: x["num"])
        
        rows = [
            "| # | Title | Complexity (Time / Space) | Code |",
            "|---|-------|---------------------------|------|"
        ]
        for p in problems[diff]:
            rows.append(f"| {p['num']} | **{p['title']}** | {p['t_comp']} / {p['s_comp']} | [Python](./{p['path']}) |")
        
        tables[diff] = "\n".join(rows)
        
    return tables

def update_readme():
    readme_path = "README.md"

    if not os.path.exists(readme_path):
        print("Error: README.md not found.")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    tables = generate_tables()
    
    # Process each difficulty marker
    for diff in ["EASY", "MEDIUM", "HARD"]:
        start_marker = f"<!-- {diff}_TABLE_START -->"
        end_marker = f"<!-- {diff}_TABLE_END -->"
        
        # Check if markers exist in README
        if start_marker in content and end_marker in content:
            # Regex to replace everything between the start and end markers
            pattern = re.compile(rf"({start_marker}).*?({end_marker})", re.DOTALL)
            content = pattern.sub(rf"\1\n{tables.get(diff.lower(), '')}\n\2", content)
            print(f"Table for {diff.upper()} updated successfully!")
        else:
            print(f"Warning: Markers {start_marker} / {end_marker} not found in README.md.")

    # Write the updated content back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("README.md update process finished!")

if __name__ == "__main__":
    update_readme()