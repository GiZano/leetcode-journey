<div align="center">

# 🚀 LeetCode Journey Template
### Automated LeetCode Progress Tracker & Multi-Language Practice Hub

> An automated, production-ready repository template designed to document, organize, and track your LeetCode problem-solving progress with automatic GitHub Actions updates.

<br>

[![Use this template](https://img.shields.io/badge/Use%20this%20template-238636?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GiZano/leetcode-journey-template/generate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](./.github/workflows/update_readme.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](./CONTRIBUTING.md)

</div>

---

## ✨ Features

- **🔄 Automated Statistics & Tables:** A built-in GitHub Actions workflow executes on every push to update difficulty tables and overall progress counters.
- **🌐 Multi-Language Support:** First-class support for C++, Python, Rust, Java, Go, TypeScript, C#, Kotlin, Swift, and more.
- **📁 Organized Structure:** Dedicated folders for `easy`, `medium`, and `hard` problems, each maintaining its own index table.
- **⏱️ Complexity Tracking:** Automatically parses Time Complexity and Space Complexity from file docstrings.
- **🧪 Templates & Test Runners:** Ready-to-use solution files and local test runners located in `utils/`.
- **🤖 AI Coding Guidelines:** Zero-spoiler mentor guidelines included in `AGENT.md` for AI assistants (Antigravity, Cursor, Copilot, Claude).

---

## 🚀 Quick Start

### 1. Create your repository
Click the [**Use this template**](https://github.com/GiZano/leetcode-journey-template/generate) button on GitHub to initialize your personal repository.

### 2. Configure GitHub Actions Permissions
To allow GitHub Actions to commit the updated README tables back to your repository:
1. Open your new repository on GitHub.
2. Go to **Settings** > **Actions** > **General**.
3. Under **Workflow permissions**, select **Read and write permissions**.
4. Click **Save**.

### 3. Clone and Customize
Clone your repository locally:
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

Personalize your LeetCode username, profile badge, and details in `README.md`.

### 4. Add your first solution
Copy a starter template from `utils/` to the matching difficulty directory:
```bash
# Example for a Python solution:
cp utils/template.py solutions/easy/0001-two-sum.py

# Example for a C++ solution:
cp utils/template.cpp solutions/easy/0001-two-sum.cpp
```

Ensure your file starts with the metadata header:
```python
"""
Problem: 1. Two Sum
Time: O(n)
Space: O(n)
"""
```

### 5. Push your code
Push your commits to your repository:
```bash
git add .
git commit -m "feat: add 0001-two-sum"
git push
```
The GitHub Action will automatically run `update_readme.py` and commit the updated tables and stats.

---

## 📊 Progress Tracker

<!-- STATS_START -->
| Difficulty | Solved | View Solutions |
| :---: | :---: | :--- |
| 🟢 **Easy** | 0 | [📁 Browse Easy](./solutions/easy/README.md) |
| 🟡 **Medium** | 0 | [📁 Browse Medium](./solutions/medium/README.md) |
| 🔴 **Hard** | 0 | [📁 Browse Hard](./solutions/hard/README.md) |
| 🏆 **Total** | **0** | |
<!-- STATS_END -->

---

## 📂 Repository Structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/        # Issue templates (Bug report, Feature request, New language)
│   ├── workflows/
│   │   └── update_readme.yml  # Automation pipeline
│   └── PULL_REQUEST_TEMPLATE.md
├── solutions/
│   ├── easy/                  # Easy difficulty solutions & auto-updated README
│   ├── medium/                # Medium difficulty solutions & auto-updated README
│   └── hard/                  # Hard difficulty solutions & auto-updated README
├── utils/                     # Starter templates and local unit test harnesses
│   ├── template.py
│   ├── template.cpp
│   ├── template_test.py
│   ├── template_test.cpp
│   └── README.md
├── AGENT.md                   # Zero-spoiler mentor guidelines for AI assistants
├── CONTRIBUTING.md             # Contribution guidelines
├── CODE_OF_CONDUCT.md         # Community code of conduct
├── LICENSE                    # MIT License
├── update_readme.py           # Table and statistic generation script
└── README.md                  # Main progress dashboard
```

---

## 🤝 Contributing

We welcome open-source contributions! Please review [CONTRIBUTING.md](./CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) before opening a pull request.

> [!NOTE]
> **What we accept:**
> - 🌐 New language definitions and starter templates.
> - ⚡ Optimizations and bug fixes in `update_readme.py`.
> - 🤖 GitHub Actions and automation improvements.
> - 🛠️ Test runners and scaffolding utilities in `utils/`.
>
> **What we do NOT accept:**
> - ❌ Solved LeetCode exercises or personal solutions. *(Please use this repository as a template for your own solutions instead!)*

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).
