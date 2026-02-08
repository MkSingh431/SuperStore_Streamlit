# SuperStore Data Analysis

This project analyzes the SuperStore dataset to uncover business insights and answer key questions about sales, profit, customers, and product categories.

## Dataset

- **Source:** SuperStore.csv
- **Contents:** Sales transactions including order details, customer info, product categories, sales, profit, and more.

## Project Steps

1. **Dashboard Setup**: Initialize the Streamlit app with a wide layout and custom page title.
2. **Data Ingestion**: Implement a file uploader to accept CSV/Excel files, defaulting to `Superstore.csv` if no file is uploaded.
3. **Date Filtering**: Create date input widgets to filter the dataset based on the `Order Date` range.
4. **Sidebar Filtering**: Add interactive sidebar filters for `Region`, `State`, and `City` to dynamically slice the data.
5. **Sales Summary Visualizations**:
   - Display a bar chart for **Category-wise Sales**.
   - Display a pie chart for **Region-wise Sales**.
6. **Data Export**: Provide download buttons for aggregated data (Category and Region views).
7. **Time Series Analysis**: Visualize monthly sales trends using a line chart.
8. **Hierarchical Visualization**: Create a TreeMap to show sales distribution across `Region`, `Category`, and `Sub-Category`.
9. **Segment & Category Analysis**: Display pie charts for sales distribution by `Segment` and `Category`.
10. **Detailed Matrix**: Generate a pivot table (heatmap style) showing month-wise sales for each sub-category.
11. **Profitability Analysis**: Plot a scatter chart to analyze the relationship between **Sales** and **Profit**, sized by **Quantity**.
12. **Raw Data Access**: Include an expander to view the raw data and a button to download the final processed dataset.

## Visualizations

- Line charts for trends
- Histograms for distributions
- Heatmaps for correlations

## How to Run

1. Open `SuperStore.ipynb` in Jupyter Notebook or VS Code.
2. Ensure `Superstore.csv` is in the same directory.
3. Run each cell sequentially to reproduce the analysis and plots.

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

Install requirements with:
```bash
pip install pandas numpy matplotlib seaborn
```

## Author

- [Mk Singh]
- [LinkedIn](https://www.linkedin.com/in/motilal-das-42b4a9254)

---
*This project demonstrates practical data analysis and visualization using Python and pandas.*
