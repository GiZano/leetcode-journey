import os
import re

def parse_problems():
    # Define the directory containing the solutions
    path = "solutions"
    problems = {"easy": [], "medium": [], "hard": []}

    # Check if the directory exists
    if not os.path.exists(path):
        return problems

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
                    
                    # Append dictionary with data (saving just the file name since it will be in the same folder)
                    problems[diff].append({
                        "num": int(num), 
                        "title": title.strip(),
                        "t_comp": t_comp,
                        "s_comp": s_comp,
                        "file_name": file
                    })
    return problems

def generate_tables(problems):
    tables = {}
    for diff, probs in problems.items():
        if not probs:
            tables[diff] = "*No problem solved in this category yet.*"
            continue
            
        # Sort numerically by problem ID
        probs.sort(key=lambda x: x["num"])
        
        rows = [
            "| # | Title | Complexity (Time / Space) | Code |",
            "|---|-------|---------------------------|------|"
        ]
        for p in probs:
            # Note the relative path: the README is in the same folder as the .py files!
            rows.append(f"| {p['num']} | **{p['title']}** | {p['t_comp']} / {p['s_comp']} | [Python](./{p['file_name']}) |")
        
        tables[diff] = "\n".join(rows)
    return tables

def generate_stats(problems):
    easy_count = len(problems["easy"])
    medium_count = len(problems["medium"])
    hard_count = len(problems["hard"])
    total = easy_count + medium_count + hard_count

    rows = [
        "| Difficulty | Solved | View Solutions |",
        "| :---: | :---: | :--- |",
        f"| 🟢 **Easy** | {easy_count} | [📁 Browse Easy](./solutions/easy/README.md) |",
        f"| 🟡 **Medium** | {medium_count} | [📁 Browse Medium](./solutions/medium/README.md) |",
        f"| 🔴 **Hard** | {hard_count} | [📁 Browse Hard](./solutions/hard/README.md) |",
        f"| 🏆 **Total** | **{total}** | |"
    ]
    return "\n".join(rows)

def update_file(file_path, start_marker, end_marker, replacement_content):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Skipping.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if start_marker in content and end_marker in content:
        # Regex to replace everything between the start and end markers
        pattern = re.compile(rf"({start_marker}).*?({end_marker})", re.DOTALL)
        new_content = pattern.sub(rf"\1\n{replacement_content}\n\2", content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Success: Updated {file_path}")
    else:
        print(f"Warning: Markers {start_marker} / {end_marker} not found in {file_path}.")

def main():
    print("Starting README update process...")
    problems = parse_problems()
    
    tables = generate_tables(problems)
    stats = generate_stats(problems)
    
    # 1. Update Main README with stats
    update_file("README.md", "<!-- STATS_START -->", "<!-- STATS_END -->", stats)
    
    # 2. Update sub-directory READMEs with their respective tables
    update_file("solutions/easy/README.md",   "<!-- TABLE_START -->", "<!-- TABLE_END -->", tables["easy"])
    update_file("solutions/medium/README.md", "<!-- TABLE_START -->", "<!-- TABLE_END -->", tables["medium"])
    update_file("solutions/hard/README.md",   "<!-- TABLE_START -->", "<!-- TABLE_END -->", tables["hard"])
    
    print("Process finished!")

if __name__ == "__main__":
    main()