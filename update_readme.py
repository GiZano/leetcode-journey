import os
import re

# Supported languages configuration
# Priority order: C++ (1), Python (2), Rust (3), Java (4), etc.
LANGUAGE_CONFIG = {
    ".cpp":   {"name": "C++",        "icon": "⚙️", "order": 1},
    ".cc":    {"name": "C++",        "icon": "⚙️", "order": 1},
    ".cxx":   {"name": "C++",        "icon": "⚙️", "order": 1},
    ".py":    {"name": "Python",     "icon": "🐍", "order": 2},
    ".rs":    {"name": "Rust",       "icon": "🦀", "order": 3},
    ".java":  {"name": "Java",       "icon": "☕", "order": 4},
    ".c":     {"name": "C",          "icon": "🔤", "order": 5},
    ".go":    {"name": "Go",         "icon": "🐹", "order": 6},
    ".ts":    {"name": "TypeScript", "icon": "🔷", "order": 7},
    ".js":    {"name": "JavaScript", "icon": "📜", "order": 8},
    ".kt":    {"name": "Kotlin",     "icon": "🎯", "order": 9},
    ".cs":    {"name": "C#",         "icon": "🟩", "order": 10},
    ".swift": {"name": "Swift",      "icon": "🐦", "order": 11},
}

def clean_complexity(raw_str):
    """Clean complexity string, removing comments and trailing markers."""
    if not raw_str:
        return "N/A"
    cleaned = re.split(r'#|//|\*/', raw_str)[0].rstrip('*').strip()
    return cleaned if cleaned else "N/A"

def parse_problems():
    """
    Scan solutions directory and group files by problem identifier.
    Returns: dict mapping difficulty ("easy", "medium", "hard") to a list of problem dicts.
    """
    path = "solutions"
    # Internal map: {diff: {problem_key: problem_data}}
    problems_map = {"easy": {}, "medium": {}, "hard": {}}

    if not os.path.exists(path):
        return {"easy": [], "medium": [], "hard": []}

    for root, dirs, files in os.walk(path):
        for file in files:
            base_name, ext = os.path.splitext(file)
            ext = ext.lower()

            if ext not in LANGUAGE_CONFIG:
                continue

            lang_info = LANGUAGE_CONFIG[ext]
            file_path = os.path.join(root, file)

            # Determine difficulty from folder name (defaults to easy if not found)
            diff = "easy"
            if "medium" in file_path.lower():
                diff = "medium"
            elif "hard" in file_path.lower():
                diff = "hard"

            # Compute relative link from the difficulty README's location (solutions/<diff>/)
            diff_dir = os.path.join(path, diff)
            rel_file_path = os.path.relpath(file_path, diff_dir).replace(os.sep, '/')
            rel_link = f"./{rel_file_path}"

            # Read file docstrings
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            prob_match = re.search(r"Problem:\s*(\d+)\.?\s*(.*)", content)
            time_match = re.search(r"Time:\s*(.*)", content)
            space_match = re.search(r"Space:\s*(.*)", content)

            num = None
            title = None
            if prob_match:
                num = int(prob_match.group(1))
                raw_title = prob_match.group(2)
                title = re.split(r'#|//|\*/', raw_title)[0].rstrip('*').strip()

            # Identify grouping key from base filename or problem number
            fn_match = re.match(r"^(\d+)-(.*)$", base_name)
            if fn_match:
                fn_num = int(fn_match.group(1))
                fn_slug = fn_match.group(2)
                problem_key = f"{fn_num:04d}"
                if num is None:
                    num = fn_num
                if not title:
                    title = fn_slug.replace("-", " ").title()
            elif num is not None and num > 0:
                problem_key = f"{num:04d}"
            else:
                problem_key = base_name
                if num is None:
                    num = 0
                if not title:
                    title = base_name

            t_comp = clean_complexity(time_match.group(1)) if time_match else "N/A"
            s_comp = clean_complexity(space_match.group(1)) if space_match else "N/A"

            # Create problem entry if not yet registered in this category
            if problem_key not in problems_map[diff]:
                problems_map[diff][problem_key] = {
                    "num": num,
                    "title": title,
                    "t_comp": t_comp,
                    "s_comp": s_comp,
                    "solutions": []
                }
            else:
                curr = problems_map[diff][problem_key]
                # Merge metadata if current entry has placeholder/missing info
                if (curr["t_comp"] == "N/A" or not curr["t_comp"]) and t_comp != "N/A":
                    curr["t_comp"] = t_comp
                if (curr["s_comp"] == "N/A" or not curr["s_comp"]) and s_comp != "N/A":
                    curr["s_comp"] = s_comp
                if (not curr["title"] or curr["title"] == "N/A") and title:
                    curr["title"] = title
                if curr["num"] == 0 and num != 0:
                    curr["num"] = num

            # Add solution if not already present
            existing_links = [s["link"] for s in problems_map[diff][problem_key]["solutions"]]
            if rel_link not in existing_links:
                problems_map[diff][problem_key]["solutions"].append({
                    "name": lang_info["name"],
                    "icon": lang_info["icon"],
                    "order": lang_info["order"],
                    "link": rel_link
                })

    # Convert to sorted lists
    problems = {}
    for diff, prob_dict in problems_map.items():
        prob_list = list(prob_dict.values())
        # Sort solutions within each problem by defined order, then name
        for p in prob_list:
            p["solutions"].sort(key=lambda s: (s["order"], s["name"]))
        # Sort problems numerically by ID
        prob_list.sort(key=lambda x: x["num"])
        problems[diff] = prob_list

    return problems

def generate_tables(problems):
    tables = {}
    for diff, probs in problems.items():
        if not probs:
            tables[diff] = "*No problem solved in this category yet.*"
            continue

        rows = [
            "| # | Title | Complexity (Time / Space) | Solutions |",
            "|---|-------|---------------------------|-----------|"
        ]
        for p in probs:
            sol_links = [f"[{s['icon']} {s['name']}]({s['link']})" for s in p["solutions"]]
            sol_str = " · ".join(sol_links) if sol_links else "N/A"
            rows.append(f"| {p['num']} | **{p['title']}** | {p['t_comp']} / {p['s_comp']} | {sol_str} |")

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