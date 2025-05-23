# 📊 Solar Radiation Dashboard

## 🌞 Overview

This Streamlit dashboard provides an interactive interface to explore solar radiation data for West African countries—Benin, Sierra Leone, and Togo. It visualizes patterns and helps stakeholders identify investment opportunities in renewable energy.

---

## 📁 Project Structure

```
├── app
│   ├── __init__.py
│   ├── main.py              # Main Streamlit app
│   ├── utils.py             # Utility functions
│   └── README.md            # Documentation for the development process and usage instructions
├── data                     # Cleaned CSV files (not tracked by Git)
├── .gitignore               # Ignore rules for Git
└── requirements.txt         # Python dependencies
```

---

## ✅ Features

- **Time Series Plots**: Visualize radiation variables like GHI, DNI, DHI, and ambient temperature over time.
- **Interactive Filtering**: Select countries and metrics using widgets.
- **Boxplots**: Compare GHI or other metrics across regions.
- **Top Regions Table**: Identify regions with the highest solar potential.
- **Color-Themed Visuals**: Distinct country colors for clarity and consistency.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Tensaey-sol/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Set Up Virtual Environment

From your project root:

```bash
python -m venv venv
```

Activate it:

- **Windows**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app/main.py
```

A new browser tab should open with your dashboard.

---

## 📂 Data

- Place cleaned CSVs in the `data/processed/` directory. This folder is ignored by Git.
- Alternatively I am providing the cleaned CSVs from a publicly available Google Drive link.

---

## 🛠 Development Notes

- Branch used: `dashboard-dev`
- Initial commit: `feat: basic Streamlit UI`
- Colors defined for country plots:

  ```python
  color_dict = {
      'Benin': '#1F77B4',
      'Sierra Leone': '#8C564B',
      'Togo': '#17BECF'
  }
  ```

- All plotting and data-loading logic is modularized in `app/utils.py`

---

## 🌐 Deployment

Deploy the app to [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your repo to GitHub.
2. Log in to Streamlit Cloud.
3. Click "New App" and select your repo.
4. Set the main file to `app/main.py`.

---

## 📧 Contact

For questions, suggestions, or contributions, feel free to open an issue or submit a pull request.
