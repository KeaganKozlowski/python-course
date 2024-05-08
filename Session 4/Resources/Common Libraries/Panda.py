import pandas as pd

# Read the CSV file into a Pandas DataFrame
sales_data = pd.read_csv("sales_data.csv")

# Display the first few rows of the DataFrame
print("First 5 rows of the sales data:")
print(sales_data.head())

# Summary statistics
print("\nSummary statistics:")
print(sales_data.describe())

# Total sales by product category
total_sales_by_category = sales_data.groupby('Product Category')['Sales'].sum()
print("\nTotal sales by product category:")
print(total_sales_by_category)

# Average sales by month
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data['Month'] = sales_data['Date'].dt.month
average_sales_by_month = sales_data.groupby('Month')['Sales'].mean()
print("\nAverage sales by month:")
print(average_sales_by_month)
