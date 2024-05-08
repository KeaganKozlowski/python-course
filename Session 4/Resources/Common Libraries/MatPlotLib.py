import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
sales_data = pd.read_csv("sales_data.csv")

# Convert the 'Date' column to datetime
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Group sales data by month and calculate total sales
monthly_sales = sales_data.groupby(sales_data['Date'].dt.to_period('M'))['Sales'].sum()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index.to_timestamp(), monthly_sales.values, marker='o', linestyle='-')

# Formatting the plot
plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()
