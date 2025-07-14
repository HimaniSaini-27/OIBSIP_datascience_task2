
---

# 📈 Unemployment Analysis with Python – OIBSIP Data Science Internship Task 2

### 🔍 Objective

The goal of this project is to analyze the unemployment rate in India using publicly available data. Unemployment, measured as the percentage of the labor force that is jobless, spiked sharply during the COVID-19 pandemic. This analysis provides insight into how unemployment rates have evolved over time, across regions, and between rural and urban areas.

This was submitted as part of my Oasis Infobyte Internship (OIBSIP).

---

### ✅ Steps Performed

#### 1. Data Acquisition & Loading

* Downloaded the dataset from Kaggle using `kagglehub`
* Loaded the dataset into a pandas DataFrame
* Checked and cleaned column names for uniformity

#### 2. Data Cleaning & Preparation

* Converted the `Date` column to `datetime` format
* Sorted data chronologically
* Dropped rows with missing values
* Ensured consistency in column labels and data types

#### 3. Exploratory Data Analysis (EDA)

* **Overall Trend**: Line plot showing India's estimated unemployment rate over time
* **Regional Analysis**: Plots showing unemployment trends across different Indian regions
* **Area-wise Comparison**: Compared unemployment between rural and urban areas

---

### 📊 Visualizations & Insights

* 📅 **Time Series Trend**: Identified fluctuations and spikes in unemployment, particularly during the pandemic period.
* 🌍 **Regional Disparities**: Highlighted how different Indian regions were affected differently in terms of unemployment.
* 🏙️ **Urban vs. Rural Comparison**: Revealed differences in unemployment patterns based on area type, useful for targeted policy-making.

---

### 🛠️ Tools & Libraries Used

* **Python**
* `pandas` – for data manipulation
* `matplotlib`, `seaborn` – for visualization
* `datetime` – for handling and transforming date fields
* `kagglehub` – for automated dataset download

---

### 📌 Outcome

This analysis helped uncover key insights about the unemployment scenario in India:

* 🟢 Time-based trends highlighting peaks during major disruptions like COVID-19
* 🟣 Regions and states with consistently higher or lower unemployment rates
* 🔵 Variation between rural and urban unemployment rates

These insights can assist policymakers, researchers, and businesses in making informed decisions related to employment strategies and economic recovery efforts.

---
