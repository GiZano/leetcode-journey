# 🛠️ Utilities & Templates

This directory contains starter templates and test harnesses to kickstart solving new LeetCode problems.

## 📄 Available Templates

| File | Language | Purpose |
| :--- | :--- | :--- |
| [`template.py`](./template.py) | Python 3 | Docstring metadata template with problem info and Big O analysis |
| [`template.cpp`](./template.cpp) | C++20 | Starter file with common STL headers and class template |
| [`template_test.py`](./template_test.py) | Python 3 | Local unit test runner (table-driven test cases) |
| [`template_test.cpp`](./template_test.cpp) | C++20 | Local test runner with `#ifdef LOCAL` compilation flag |

---

## 🚀 How to Use

1. **Copy a template** into the appropriate difficulty folder:
   ```bash
   cp utils/template.py solutions/easy/0001-two-sum.py
   # or for C++:
   cp utils/template.cpp solutions/easy/0001-two-sum.cpp
   ```

2. **Fill in the metadata header** at the top of the file:
   - Make sure `Problem: <Number>. <Title>`, `Time: O(...)`, and `Space: O(...)` are clearly stated.
   - The automated tracking script `update_readme.py` uses these tags to populate your repository's solution tables.

3. *(Optional)* **Append the test harness** (`template_test.py` or `template_test.cpp`) to test your solution locally before submitting to LeetCode:
   - For Python: `python3 solutions/easy/0001-two-sum.py`
   - For C++: `g++ -std=c++20 -DLOCAL solutions/easy/0001-two-sum.cpp -o runner && ./runner`
