```md
# Automobile Sales Analysis during Recession

**Tags**: `automobile sales`, `recession analysis`, `data visualization`, `Python`, `Matplotlib`, `Seaborn`, `Folium`, `pandas`, `economic indicators`, `time series analysis`, `GDP`, `unemployment`, `consumer confidence`, `advertising expenditure`, `vehicle types`

---

## 📊 Key Visualizations and Insights

### 1. Line Chart: Average Automobile Sales Over Years
- **Task:** Show the fluctuation of average sales from year to year, annotating recession periods.
- **Insight:** Sales drop significantly during recession years (e.g., 1981–82, 2007–09) and recover during non-recession periods.

### 2. Dual-Axis Line Chart: Advertising vs Sales (Non-Recession)
- **Task:** Compare advertising expenditure with sales trends during non-recession years.
- **Insight:** During non-recession periods, advertising expenditure and sales generally move together, suggesting that advertising may boost sales when the economy is strong.

### 3. Bar Plot: Vehicle Type Sales (Recession vs Non-Recession)
- **Task:** Compare average sales per vehicle type across recession and non-recession periods using Seaborn.
- **Insight:** Sales of all vehicle types fall during recessions, but luxury/executive cars and sports cars experience steeper declines compared to small family cars and superminis.

### 4. Subplots: GDP Variation Over Time
- **Task:** Compare GDP trends during recession vs non-recession periods using two line charts side by side.
- **Insight:** GDP is generally lower and more volatile during recessions, reflecting weaker economic conditions that reduce automobile demand.

### 5. Bubble Plot: Seasonality Impact on Sales
- **Task:** Visualize automobile sales by month, with bubble size representing seasonality weight.
- **Insight:** Sales peak in certain months (e.g., December) and drop in others, confirming seasonal patterns. Non-recession periods show higher overall sales across all months.

### 6. Scatter Plots: Consumer Confidence & Price vs Sales (Recession)
- **Task:** Explore relationships between consumer confidence and sales, and between vehicle price and sales during recessions.
- **Insight:** Higher consumer confidence correlates with higher sales, while higher prices tend to suppress sales—both relationships are more pronounced during recessions.

### 7. Pie Charts: Advertising Expenditure Distribution
- **Task:** Show the proportion of advertising spending during recession vs non-recession, and by vehicle type during recession.
- **Insight:** Most advertising expenditure occurs during non-recession periods. During recessions, the largest share is allocated to small family cars and superminis, possibly to appeal to budget-conscious consumers.

### 8. Line Plot: Unemployment Rate vs Sales by Vehicle Type
- **Task:** Analyze how unemployment affects sales of different vehicle types during recessions.
- **Insight:** Higher unemployment rates are associated with lower sales across all vehicle types. Superminis and small family cars show relatively better resilience than larger vehicles.

### 9. Optional Map: City-Level Sales (Choropleth)
- **Task:** Visualize the geographic distribution of sales during recessions using Folium.
- **Insight:** Certain cities (e.g., New York, Los Angeles) have higher sales volumes, possibly due to larger populations or stronger local economies.

---

## 📁 Dataset

The dataset `automobile-sales.csv` is obtained from the following URL:  
[https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv)

### Variables
- **Date** – Month-end date of the observation  
- **Recession** – Binary indicator (1 = recession, 0 = normal)  
- **Automobile_Sales** – Number of vehicles sold  
- **GDP** – Per capita GDP (USD)  
- **unemployment_rate** – Monthly unemployment rate  
- **Consumer_Confidence** – Synthetic consumer confidence index  
- **Seasonality_Weight** – Seasonal effect on sales (>1 = high season, <1 = low season)  
- **Price** – Average vehicle price  
- **Advertising_Expenditure** – Company advertising spend  
- **Vehicle_Type** – SuperminiCar, SmallFamilyCar, MediumFamilyCar, ExecutiveCar, Sports  
- **Competition** – Market competition measure  
- **Month**, **Year** – Extracted from Date  
- **City** – Office location

---

## 🛠️ Requirements

Install the required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn folium
```

Alternatively, run the commands in the provided Jupyter notebook.

---

## 🚀 Usage

1. **Clone** this repository to your local machine.
2. **Ensure** the dataset is available – the notebook automatically fetches it from the given URL.
3. **Open** the Jupyter notebook (`automobile_sales_analysis.ipynb`) and run all cells.
4. All plots will be generated **inline** in the notebook.
5. Optionally, you can modify the notebook to filter different recession periods or customise the visualisations.

---

## 📝 Notebook Structure

The notebook is organised into **tasks** corresponding to each visualisation objective. Each task includes:
- **Data preparation** (filtering, grouping, aggregation)
- **Plotting code** using Matplotlib, Seaborn, or Folium
- **Interpretation comments** to explain the insights derived from each plot

The flow follows the sequence of questions posed in the analysis, starting from overall sales trends and drilling down into specific economic factors and their impact on different vehicle types and regions.

---

## 📌 Key Findings

- **Recessions significantly reduce automobile sales** across all vehicle types, but the impact is strongest on luxury and sports cars.
- **Advertising expenditure is cut during recessions**, which may further dampen sales. However, spending on smaller, more affordable vehicles remains relatively higher.
- **Consumer confidence and GDP** are strong positive predictors of sales; both drop sharply in recessions.
- **Unemployment** negatively affects sales, especially for medium and large vehicles.
- **Seasonality** persists in both recession and non-recession periods, with end-of-year months showing higher sales.

---

## 📄 License

This project is for educational purposes. All rights reserved © Probal Dhali, 2026.  
You may use, share, and adapt the code for non‑commercial purposes with proper attribution.

---

## 👤 Author

**Prionti Das**  
[GitHub](https://github.com/Priontipayel05) *(replace with your actual GitHub profile URL)*

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!  
If you would like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

For any questions, feedback, or collaboration inquiries, please reach out via:

- **GitHub Issues**: [Open an issue](https://github.com/Priontipayel05/Final-Assignment:-Part-1/issues)  
- **Email**: dprionti2004@gmail.com

---

*Happy analysing! 🚗📈*
```