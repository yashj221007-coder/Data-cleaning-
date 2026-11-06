import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Create or load a sample dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Product_Category': [
        'Electronics',
        'Clothing',
        'Home',
        'Electronics',
        'Clothing',
        'Home',
    ],
    'Sales': [4500, 3200, 2800, 5100, 3900, None],  # Notice a missing value (NaN)
    'Expenses': [2300, 1900, 1500, 2600, 2100, 1800],
}

df = pd.DataFrame(data)

# Explore the dataset
print('--- Dataset Info ---')
print(df.info())
print('\n--- Missing Values ---')
print(df.isnull().sum())

# Cleaning: Fill missing 'Sales' with the mean of the column
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# Check after cleaning
print('\n--- After Cleaning ---')
print(df)

# Summary statistics
print('\n--- Summary Statistics ---')
print(df.describe())

# Group by Product Category to see total sales
category_sales = df.groupby('Product_Category')['Sales'].sum()
print('\n--- Sales by Category ---')
print(category_sales)

plt.figure(figsize=(8, 4))
plt.plot(
    df['Month'],
    df['Sales'],
    marker='o',
    color='blue',
    linewidth=2,
    label='Sales',
)
plt.plot(
    df['Month'],
    df['Expenses'],
    marker='s',
    color='red',
    linestyle='--',
    label='Expenses',
)
plt.title('Monthly Sales vs. Expenses')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

plt.figure(figsize=(6, 4))
categories = category_sales.index
values = category_sales.values

plt.bar(categories, values, color=['#3498db', '#2ecc71', '#e74c3c'])
plt.title('Total Sales by Product Category')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.show()

plt.figure(figsize=(6, 6))
plt.pie(
    values,
    labels=categories,
    autopct='%1.1f%%',
    startangle=90,
    colors=['#3498db', '#2ecc71', '#e74c3c'],
)
plt.title('Sales Proportion by Category')
plt.axis('equal')  # Ensures a circular pie chart
plt.show()
