# Contributing to LeetCode Journey Template

Thank you for your interest in improving the **LeetCode Journey Template**! This project aims to provide the cleanest, most efficient, and easily extensible automated template for tracking algorithm problem-solving.

---

## 🚨 Essential Rule: No Solved Exercises Accepted

> [!IMPORTANT]
> **This repository is a template, NOT a personal solution archive.**
>
> - **We do NOT accept Pull Requests that add solved LeetCode problems, solution code, or personal notes to `solutions/`.**
> - If you want to track your own solutions, please click the **"Use this template"** button at the top of the repository on GitHub and create your own personal repository.
> - Any PR containing actual problem solutions will be closed immediately.

---

## ✅ What We Welcome & What You Can Contribute

We actively look for contributions that enhance the functionality, flexibility, and developer experience of the template:

### 1. 🌐 Support for New Programming Languages
- Extend `LANGUAGE_CONFIG` in `update_readme.py` with new language definitions (file extensions, display name, icon/emoji, priority order).
- Add corresponding starter templates (`utils/template.<ext>`) and local test runners (`utils/template_test.<ext>`).

### 2. ⚡ Script Optimizations & Robustness
- Improve the parsing logic in `update_readme.py` (e.g., handling edge cases in problem numbering, filenames, complexity strings, or multi-line docstrings).
- Enhance performance when scanning large solution directories.
- Improve cross-platform path compatibility.

### 3. 🤖 Automation & CI/CD Pipelines
- Optimize the GitHub Actions workflow (`.github/workflows/update_readme.yml`).
- Add workflow checks for docstring format validation or code formatting (e.g., pre-commit linters).
- Add new workflow triggers or notification options.

### 4. 🛠️ Utilities, Tooling & Test Harnesses
- Create new test runner harnesses for unsupported languages in `utils/`.
- Add helper scripts for problem scaffolding (e.g., a CLI helper to generate boilerplate files from a LeetCode problem URL/number).

### 5. 📖 Documentation & AI Mentor Guidelines
- Clarify instructions in `README.md` or `utils/README.md`.
- Improve the AI mentor instructions in `AGENT.md` (e.g., prompt enhancements for Claude, Cursor, ChatGPT, Copilot, or Antigravity).

---

## 🛠️ Contribution Workflow

1. **Fork the Repository:** Click the "Fork" button on GitHub.
2. **Clone your Fork:**
   ```bash
   git clone https://github.com/<your-username>/leetcode-journey-template.git
   cd leetcode-journey-template
   ```
3. **Create a Feature Branch:**
   ```bash
   git checkout -b feat/support-rust-language
   # or
   git checkout -b fix/complexity-parser-regex
   ```
4. **Make Your Changes:** Keep changes concise, focused, and well-structured.
5. **Test Locally:**
   Run the table generation script locally to verify everything functions as expected:
   ```bash
   python update_readme.py
   ```
   Ensure no syntax errors occur and markdown tables render cleanly.
6. **Commit with Clear Messages:** Follow conventional commit conventions (e.g., `feat: ...`, `fix: ...`, `docs: ...`).
7. **Push to Your Fork & Open a Pull Request:**
   Submit your PR against the `main` branch of this repository.

---

## 📋 Pull Request Expectations

Before opening your Pull Request, please ensure:
- [ ] Your PR does **not** introduce any personal solutions or completed exercises.
- [ ] You tested any code or script changes locally.
- [ ] New language additions include an entry in `LANGUAGE_CONFIG` and a matching template in `utils/`.
- [ ] Documentation is updated if user-facing behavior changes.

---

Thank you for helping make this template better for developers worldwide! 🚀
