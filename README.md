# 🔥 Wildfire Emergency Response Analytics

An interactive wildfire analytics and emergency response dashboard built using NASA FIRMS active fire data.

The project analyzes wildfire activity, fire intensity, geographic distribution, and temporal patterns to identify high-priority wildfire events and support emergency response decision-making.

---

## 🎯 Project Objective

The objective of this project is to analyze satellite-based wildfire data and provide actionable insights for emergency response teams.

The dashboard helps answer questions such as:

- Where are wildfire hotspots concentrated?
- Which locations have the highest fire intensity?
- How does wildfire activity change over time?
- Which fire events require immediate attention?
- What areas should emergency teams prioritize?

---

## 🛰️ Data Source

The project uses wildfire data from:

**NASA FIRMS — Fire Information for Resource Management System**

The dataset contains satellite-based active fire observations.

### Data Used

- MODIS
- NASA FIRMS
- Active Fire Detection Data
- 2025 wildfire observations

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Jupyter Notebook
- NASA FIRMS
- Git & GitHub

---

## 📊 Key Analysis

The project performs:

### 1. Data Cleaning

- Missing value analysis
- Duplicate detection
- Data type conversion
- Date and time processing
- Geographic data validation

### 2. Exploratory Data Analysis

- Fire detection distribution
- Fire Radiative Power (FRP) analysis
- Monthly wildfire trends
- Geographic hotspot analysis
- Fire intensity analysis

### 3. Emergency Risk Analysis

Fire events are analyzed based on:

- FRP
- Fire intensity
- Geographic location
- Temporal activity

High-intensity fire events are identified as priority areas for emergency response.

---

## 📈 Dashboard Features

The Streamlit dashboard provides:

- 🔥 Total Fire Detections
- 🚨 High / Extreme Fire Events
- 📊 Average Fire Radiative Power
- ⚡ Maximum Fire Radiative Power
- 📅 Monthly Fire Activity
- 🗺️ Wildfire Hotspot Analysis
- 🔥 Fire Intensity Distribution
- 🚨 Emergency Response Priority
- 📋 Top Fire Events

---

## 📂 Project Structure

```text
Wildfire Emergency Response Analytics/
│
├── data/
│   ├── raw/
│   │   └── nasa_firms_2025.csv
│   │
│   └── processed/
│       ├── wildfire_analytics_2025.csv
│       └── wildfire_kpi_summary.csv
│
├── notebooks/
│   └── 01_fire_eda.ipynb
│
├── dashboard/
│   └── app.py
│
├── src/
│
├── sql/
│
├── requirements.txt
├── .gitignore
└── README.mdg