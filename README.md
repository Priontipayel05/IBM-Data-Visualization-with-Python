# 📊 IBM Data Visualization with Python

A complete implementation of the **IBM Data Visualization with Python** course and final assignments, covering data preprocessing, exploratory data analysis, static visualizations, geospatial visualization, interactive dashboards, and economic analysis using Python.

The project focuses on analyzing **automobile sales during recession and non-recession periods** and presenting the results through meaningful visualizations and an interactive dashboard.

---

## 🚀 Project Overview

Data visualization is an essential part of data analysis because it transforms raw data into understandable patterns, trends, and relationships.

This repository demonstrates practical use of Python visualization libraries to analyze automobile sales and investigate how economic factors such as:

* 📉 Recession
* 💰 GDP
* 📢 Advertising expenditure
* 👥 Unemployment
* 😊 Consumer confidence
* 🚗 Vehicle type
* 💵 Vehicle price
* 📅 Seasonality
* 🏢 Competition

affect automobile sales.

The project is divided into two major final assignments.

---

## 📁 Repository Structure

```text
IBM-Data-Visualization-with-Python/
│
├── Final Assignment: Part 1/
│   ├── Final_Assignment_Part_1_Create_Visualizations_using_Matplotlib,_Seaborn_&_Folium.ipynb
│   └── README.md
│
├── Final Assignment: Part 2/
│   ├── FINAL_ASSIGNMENT_PART_2_Create_Dashboard_using_Plotly_and_Dash.ipynb
│   ├── Final_Assignment_Part_2_Dashboard.py
│   ├── RecessionReportgraphs.png
│   └── YearlyReportgraphs.png
│
└── LICENSE
```

---

# 🧩 Final Assignment – Part 1

## Automobile Sales Analysis During Recession

Part 1 focuses on creating static and geospatial visualizations using:

* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Folium**

The notebook performs data preparation, filtering, aggregation, visualization, and interpretation.

### 📊 Visualizations Included

#### 1. Average Automobile Sales Over Time

A line chart is used to examine automobile sales across different years and identify changes during recession periods.

**Key observation:** Automobile sales generally decline during recession periods and recover as economic conditions improve.

#### 2. Advertising Expenditure vs Automobile Sales

A dual-axis visualization compares advertising expenditure with automobile sales during non-recession periods.

This helps investigate whether increased advertising expenditure is associated with increased sales.

#### 3. Vehicle Type Sales

A Seaborn bar plot compares average automobile sales for different vehicle categories during recession and non-recession periods.

Vehicle categories include:

* Supermini
* Small Family Car
* Medium Family Car
* Executive Car
* Sports

#### 4. GDP Analysis

GDP trends are compared between recession and non-recession periods to understand the relationship between economic conditions and automobile demand.

#### 5. Seasonal Automobile Sales

A bubble visualization examines monthly automobile sales while incorporating the seasonal impact on demand.

This helps identify months with relatively high and low automobile sales.

#### 6. Consumer Confidence and Vehicle Price

Scatter plots investigate relationships between:

* Consumer confidence and automobile sales
* Vehicle price and automobile sales

These visualizations provide insight into consumer purchasing behavior during economic downturns.

#### 7. Advertising Expenditure Distribution

Pie charts visualize advertising expenditure across:

* Recession vs non-recession periods
* Different vehicle types during recessions

#### 8. Unemployment vs Automobile Sales

The analysis examines how unemployment rates influence automobile sales for different vehicle categories.

#### 9. Geographic Visualization

Folium is used to provide an optional city-level geographic visualization of automobile sales.

---

# 📈 Final Assignment – Part 2

## Interactive Automobile Sales Dashboard

Part 2 extends the analysis by creating an interactive dashboard using:

* **Plotly**
* **Dash**
* **Pandas**
* **Python**

The repository contains both the Jupyter Notebook implementation and the standalone Python dashboard application.

### Dashboard Features

The dashboard allows users to explore automobile sales through interactive reports and visualizations.

### 📉 Recession Report

The recession report focuses on automobile sales during recession periods.

The dashboard/report visualizations include analysis of:

* Automobile sales trends
* Average sales by vehicle type
* Advertising expenditure
* Economic indicators
* Recession-related changes

### 📅 Yearly Report

The yearly report provides a broader view of automobile sales over time.

It helps analyze:

* Yearly sales trends
* Vehicle-type performance
* Economic conditions
* Changes in automobile demand

The generated dashboard report images are included in the repository as:

```text
RecessionReportgraphs.png
YearlyReportgraphs.png
```

---

# 🗃️ Dataset

The project uses an **Automobile Sales** dataset containing monthly observations and economic indicators.

### Important Variables

| Variable                  | Description                |
| ------------------------- | -------------------------- |
| `Date`                    | Month-end observation date |
| `Recession`               | Recession indicator        |
| `Automobile_Sales`        | Number of automobiles sold |
| `GDP`                     | Per-capita GDP             |
| `unemployment_rate`       | Monthly unemployment rate  |
| `Consumer_Confidence`     | Consumer confidence index  |
| `Seasonality_Weight`      | Seasonal effect on sales   |
| `Price`                   | Average vehicle price      |
| `Advertising_Expenditure` | Advertising expenditure    |
| `Vehicle_Type`            | Type of automobile         |
| `Competition`             | Market competition measure |
| `Month`                   | Month extracted from date  |
| `Year`                    | Year extracted from date   |
| `City`                    | City/office location       |

The Part 1 notebook references the automobile sales dataset provided for the IBM course.

---

# 🛠️ Technologies Used

| Technology          | Purpose                           |
| ------------------- | --------------------------------- |
| 🐍 Python           | Core programming language         |
| 🐼 Pandas           | Data manipulation and analysis    |
| 🔢 NumPy            | Numerical computation             |
| 📊 Matplotlib       | Static visualization              |
| 🎨 Seaborn          | Statistical visualization         |
| 🗺️ Folium          | Geographic visualization          |
| 📈 Plotly           | Interactive visualization         |
| ⚡ Dash              | Interactive web dashboard         |
| 📓 Jupyter Notebook | Data analysis and experimentation |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/probal2005/IBM-Data-Visualization-with-Python.git
```

Navigate into the project:

```bash
cd IBM-Data-Visualization-with-Python
```

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn folium plotly dash jupyter
```

---

# ▶️ Running the Notebooks

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
Final Assignment: Part 1/
```

or

```text
Final Assignment: Part 2/
```

Run the notebook cells sequentially to reproduce the analysis and visualizations.

---

# 🖥️ Running the Dash Dashboard

Navigate to the Part 2 directory:

```bash
cd "Final Assignment: Part 2"
```

Run the dashboard application:

```bash
python Final_Assignment_Part_2_Dashboard.py
```

The Dash application will start a local web server.

Open the URL displayed in the terminal in your web browser.

---

# 🔍 Key Findings

The analysis demonstrates several important relationships between economic conditions and automobile sales.

### 📉 Recessions Reduce Automobile Sales

Automobile sales generally decrease during recession periods because consumers tend to reduce discretionary spending.

### 🚗 Vehicle Type Matters

Higher-priced and luxury-oriented vehicle categories tend to experience stronger reductions in demand during economic downturns, while smaller and relatively affordable vehicles can be more resilient.

### 💰 GDP and Sales

Economic performance and automobile demand show a positive relationship. Weaker economic conditions are generally associated with lower automobile sales.

### 👥 Unemployment

Increasing unemployment can negatively affect automobile demand because consumers have less disposable income and greater economic uncertainty.

### 😊 Consumer Confidence

Consumer confidence is an important indicator of purchasing behavior. Higher confidence is generally associated with stronger automobile sales.

### 📢 Advertising

Advertising expenditure and sales can move together during stronger economic periods, while advertising strategies may change during recessions.

### 📅 Seasonality

Automobile sales exhibit seasonal patterns, with some months consistently showing stronger demand than others.

---

# 🎯 Learning Outcomes

Through this project, the following skills were developed:

* Data preprocessing with Pandas
* Exploratory data analysis
* Data aggregation and filtering
* Time-series visualization
* Statistical visualization
* Categorical data visualization
* Correlation analysis
* Geospatial visualization
* Interactive visualization
* Dashboard development
* Plotly chart creation
* Dash application development
* Data storytelling
* Interpretation of economic indicators

---

# 📸 Project Outputs

The repository contains generated visualization outputs for the dashboard:

### Recession Report

`RecessionReportgraphs.png`

### Yearly Report

`YearlyReportgraphs.png`

These outputs provide visual summaries of the automobile sales analysis performed in the dashboard.

---

# 📚 Course Context

This repository was created as part of the **IBM Data Visualization with Python** learning and final-assignment work.

The project demonstrates the progression from basic Python-based data visualization to interactive dashboard development.

The workflow can be summarized as:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Aggregation
   ↓
Static Visualization
   ↓
Interactive Visualization
   ↓
Dashboard Development
   ↓
Insights & Interpretation
```

---

# 👨‍💻 Author

**Prionti Das**

Computer Science & Engineering (AI & ML)

GitHub:
https://github.com/Priontipayel05

---

# 📄 License

This project is available under the **CC0 1.0 Universal** license currently present in the repository.

---

## ⭐ Acknowledgement

This project was developed as part of the IBM Data Visualization with Python coursework and uses Python's data-analysis and visualization ecosystem to demonstrate practical data storytelling.

---

## 📌 Repository

**GitHub:**
https://github.com/Priontipayel05/IBM-Data-Visualization-with-Python

If you find this project useful, consider giving the repository a ⭐.
