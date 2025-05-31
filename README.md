# 📊 Job Data Analysis — Exploratory Report & Streamlit App

## 🗂️ Project Overview

This project presents an exploratory data analysis of job postings focused on data analyst roles. The analysis is provided in two formats:

* **Jupyter Notebook**: A detailed step-by-step exploration with data inspection, visualizations, and insights.
* **Streamlit App**: A clean, interactive dashboard showcasing the core visuals and key insights without filters or sidebars, aimed at easy consumption of results.

---

## 📦 Dataset Details

* **Source:** Job postings dataset from `datasets/Job Postings` folder by cloning `https://github.com/AshishJangra27/datasets`
* **Format:** Compressed CSV file (`.csv.zip`)
* **Columns (examples):** `rating`, `min_exp`, `max_exp`, `skills`, etc.

---

## 🎯 Objectives

* Explore and understand job posting data structure and key attributes
* Analyze company ratings and experience requirements
* Visualize most demanded skills for data analyst roles
* Investigate how years of experience influence job availability

---

## 🛠️ Components & Workflow

### Jupyter Notebook

1. **Environment Setup:** Import libraries like `pandas`, `numpy`, `matplotlib`, `plotly`.
2. **Data Loading:** Read dataset files and perform initial inspection.
3. **Exploratory Data Analysis:**

   * Overview with `head()`, `info()`, and `describe()`
   * Distribution of company ratings
   * Summary statistics
4. **Visualizations:**

   * Pie chart of skill demand (using Plotly Express for interactivity)
   * Bar chart showing experience requirements vs number of job postings

### Streamlit App

* Presents core visuals and summary content from the notebook
* Simple UI with no filters or sidebars, focused on delivering insights through interactive charts
* Enables easy sharing and real-time interaction with visuals

---

## ✅ Key Findings

* Job postings show a wide distribution of company ratings.
* Certain skills emerge as highly demanded for data analyst roles.
* Demand peaks for jobs requiring early to mid-career experience levels.

---

## 🧠 Future Enhancements

* Add comprehensive null value and data cleaning steps
* Introduce filters and interactive controls in the Streamlit app
* Explore correlations, salary trends, or other relevant factors
* Extend analysis with predictive ML models
* Build a fully interactive dashboard with Plotly Dash or Voila

---

## 🚀 How to Run

### Jupyter Notebook

* Open `Job_Data_Analysis.ipynb` in JupyterLab or Jupyter Notebook
* Execute cells sequentially to reproduce the analysis and visualizations

### Streamlit App

* Install Streamlit if needed:

  ```bash
  pip install streamlit  
  ```
* Run the app:

  ```bash
  streamlit run dashboard.py  
  ```
* Access the app via the provided local URL in your browser

---

## 👤 Author

Prepared by: *\[Mohammed Omer Siddiqui]*
Affiliation: Data Analyst / AI Enthusiast
Last Updated: May 2025
