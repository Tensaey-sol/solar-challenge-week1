# Notebooks

This folder contains Jupyter notebooks for performing exploratory data analysis (EDA) on solar datasets from various countries.

Each notebook is created in its own Git branch and corresponds to a specific country's dataset (e.g., `eda-benin`, `eda-sierraleone`, etc.).

## 📁 Structure

- `notebooks/<country>_eda.ipynb`: Main notebook for EDA of the selected country.
- `src/`: Contains reusable Python modules for data loading, cleaning, and visualization.
- `data/`: Contains local copies of raw or cleaned datasets. This folder is git-ignored to avoid committing large or sensitive files.

## 🧪 How to Use

1. **Activate the virtual environment:**

```bash
source .venv/bin/activate         # macOS/Linux
.\.venv\Scripts\activate          # Windows
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the notebook:**

   - Open this project in VS Code.
   - Go to your target notebook (e.g., `benin_eda.ipynb`).
   - Select the kernel linked to your `.venv`.
   - Run cells normally using Jupyter interface.

4. **Import reusable modules** like this:

```python
from src.data_loader import load_csv
from src.cleaning import remove_outliers_zscore
from src.visualization import plot_time_series
```

> 🔁 If you encounter `ModuleNotFoundError`, append the path manually:

```python
import sys
sys.path.append('../src')
```

## ✨ Guidelines

- Do not commit data files (`data/` is included in `.gitignore`).
- Use modular code by leveraging the `src/` utilities.
- Keep notebooks clean and well-documented with markdown headers.

## ✅ Naming Convention

Branch: `eda-<country>`
Notebook: `<country>_eda.ipynb`
