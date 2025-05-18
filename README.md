# 🌞 Solar Challenge - Week 1

This repository contains the setup for **Week 1's Solar Challenge**. It includes a Python development environment, proper `.gitignore` rules, dependency management, and a GitHub Actions CI workflow.

---

## 🚀 Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Tensaey-sol/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🧱 Project Structure

```
solar-challenge-week1/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions workflow
├── .gitignore                 # Ignore rules for Git
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── src/                       # Source code directory
├── notebooks/                 # Jupyter notebooks
│   ├── __init__.py
│   └── README.md
├── data/                      ← ignored by .gitignore
└── .venv/                     # Virtual environment (ignored by git)
```

---

## ⚙️ GitHub Actions CI

A continuous integration workflow is configured to automatically run when changes are pushed to the branches:

- Uses **Python 3.13.1**
- Installs dependencies from `requirements.txt`
- Workflow is defined in `.github/workflows/ci.yml`

You can view its status in the **Actions** tab of the GitHub repository.

---

## 🛠 Tools Used

- Python **3.13.1**
- **VSCode** (Recommended editor)
- `venv` for isolated Python environments
- Git & GitHub for version control
- GitHub Actions for automation

---

## ✅ Future Improvements

- Add core functionality to `src/`
- Write and run unit tests in `tests/`
- Add linting (e.g., with `flake8`) and formatting (e.g., `black`)
- Extend CI to run automated tests

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Questions?

If you have any questions, suggestions, or contributions, feel free to open an issue or submit a pull request.
