# 💼 IT Salaries Data Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/M0haAmmad/IT-Salaries-Data-Analysis)

An exploratory data analysis (EDA) and data cleaning project focusing on Information Technology compensation benchmarks. This repository explores salary distributions across diverse technical roles, years of professional experience, and remote work arrangements using **Python** and **Pandas**.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Dataset Architecture](#-dataset-architecture)
- [Key Features & Analysis Pipeline](#-key-features--analysis-pipeline)
  - [1. Data Ingestion & Creation](#1-data-ingestion--creation)
  - [2. Data Cleaning & Preprocessing](#2-data-cleaning--preprocessing)
  - [3. Structured Data Profiling](#3-structured-data-profiling)
  - [4. Exploratory Data Analysis (EDA)](#4-exploratory-data-analysis-eda)
- [Key Findings & Insights](#-key-findings--insights)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Analysis](#running-the-analysis)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Author & License](#-author--license)

---

## 🚀 Overview

Understanding compensation trends in the tech sector is essential for industry professionals, hiring managers, and career strategists. This project implements a streamlined, reproducible data pipeline to:
- Structure raw compensation and role attributes into structured DataFrames.
- Clean and sanitize records (duplicate removal and handling missing data).
- Generate custom, aligned metadata summary tables for schema verification.
- Compute aggregate compensation statistics grouped by technical specializations.

---

## 📊 Dataset Architecture

The dataset captures four primary dimensions of IT employment:

| Column Name | Data Type | Description | Sample Values |
| :--- | :--- | :--- | :--- |
| **`Job_Title`** | `object` (string) | Professional role classification | *Data Analyst, Software Engineer, Data Scientist, DevOps Engineer* |
| **`Experience_Years`** | `int64` | Total years of relevant professional experience | *1, 2, 3, 4, 5, 6* |
| **`Salary_USD`** | `int64` / `float64` | Annual gross compensation in USD ($) | *$45,000 – $95,000* |
| **`Remote`** | `object` (string) | Remote work eligibility / status | *Yes / No* |

---

## ⚙️ Key Features & Analysis Pipeline

The pipeline in [`analysis.py`](analysis.py) executes sequentially through four structured phases:

### 1. Data Ingestion & Creation
Constructs a benchmark dataset modeling typical salary figures across key technological domains:
```python
data = {
    'Job_Title': ['Data Analyst', 'Software Engineer', 'Data Scientist', ...],
    'Experience_Years': [1, 3, 4, 2, 5, 6, 2, 3],
    'Salary_USD': [45000, 75000, 90000, 48000, 85000, 95000, 88000, 47000],
    'Remote': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']
}
df = pd.DataFrame(data)
```

### 2. Data Cleaning & Preprocessing
Ensures data consistency and prevents skewing from duplicates or null values:
- **Deduplication:** Removes redundant entries using `.drop_duplicates()`.
- **Missing Value Imputation:** Fills any null values in `Salary_USD` with the column mean.

### 3. Structured Data Profiling
Rather than relying on unformatted console logs, the pipeline builds a clean, aligned tabular summary displaying non-null counts, null frequencies, and explicit data types for each attribute:

```
Column_Name        Non_Null_Count    Null_Count    Data_Type
Job_Title          8                 0             object
Experience_Years   8                 0             int64
Salary_USD         8                 0             int64
Remote             8                 0             object
```

### 4. Exploratory Data Analysis (EDA)
Calculates the mean annual compensation for each distinct job role, rounded to the nearest integer dollar for clear business reporting:
```python
avg_salary_by_job = df.groupby('Job_Title')['Salary_USD'].mean().round(0).astype(int).reset_index()
```

---

## 💡 Key Findings & Insights

Based on the exploratory analysis:

| Job Title | Average Salary (USD) | Relative Rank |
| :--- | :---: | :---: |
| 🛠️ **DevOps Engineer** | **$95,000** | 🥇 Top Tier |
| 🔬 **Data Scientist** | **$89,000** | 🥈 High Tier |
| 💻 **Software Engineer** | **$80,000** | 🥉 Mid-High Tier |
| 📈 **Data Analyst** | **$46,667** | Entry/Intermediate Tier |

- **Infrastructure & Advanced Analytics Premium:** DevOps Engineers and Data Scientists command the highest base compensation in the sample benchmark.
- **Experience Correlation:** Software Engineers demonstrate steady salary increases corresponding to years of experience ($75k at 3 years to $85k at 5 years).
- **Remote Flexibility:** Roles across all categories showcase strong remote work feasibility.

---

## 📁 Project Structure

```bash
IT-Salaries-Data-Analysis/
│
├── analysis.py       # Main data processing & exploratory analysis script
└── README.md         # Comprehensive project documentation & insights
```

---

## 🛠️ Getting Started

### Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/M0haAmmad/IT-Salaries-Data-Analysis.git
   cd IT-Salaries-Data-Analysis
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install pandas
   ```

### Running the Analysis

The script uses `display()` for interactive tabular visualization:

- **Option A — Jupyter Notebook / VS Code Interactive Window / IPython (Recommended):**
  ```bash
  pip install ipython
  ipython analysis.py
  ```

- **Option B — Standard Python CLI:**
  If running directly with `python analysis.py`, you can run it via an interactive shell or ensure `IPython.display` is present:
  ```bash
  python -c "from IPython.display import display; exec(open('analysis.py').read())"
  ```

---

## 🔮 Future Enhancements

- [ ] **Data Visualization:** Integrate `matplotlib` and `seaborn` for boxplots, salary distribution curves, and correlation heatmaps.
- [ ] **Expanded Datasets:** Ingest larger open datasets (e.g., Stack Overflow Developer Survey, Kaggle Data Science Salaries).
- [ ] **Predictive Modeling:** Build regression models (e.g., Scikit-Learn Random Forest / XGBoost) to predict salary based on years of experience, remote status, and role.
- [ ] **Interactive Dashboard:** Develop a Streamlit or Dash web app for real-time compensation filtering.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/M0haAmmad/IT-Salaries-Data-Analysis/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author

**Mohammad Ashraf**
- GitHub: [@M0haAmmad](https://github.com/M0haAmmad)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
