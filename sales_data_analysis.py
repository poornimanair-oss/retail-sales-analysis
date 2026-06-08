import pandas as pd

df = pd.read_csv("retail_sales_dataset.csv")

print(df.info())
print(df.describe())
df.isnull().sum()
print(df.columns)
for col in df.select_dtypes(include='number').columns:
    negative_count = (df[col] < 0).sum()
    print(f"{col}: {negative_count} negative values")
negative_rows = df[df['Total Amount'] < 0]
print(negative_rows)
negative_rows = df[df['Total Amount'] < 0]
print(negative_rows.index)
for idx in negative_rows.index:
    print(f"Excel row number: {idx + 2}")

print(df['Total Amount'].sum())
print(df.groupby('Product Category')['Total Amount'].sum())
print(df.groupby('Gender')['Total Amount'].sum())
#in product category electronics had the most purchase and beauty had the least purchase
#Females has contributed to most of the purchases
df['Age Group'] = pd.cut(
    df['Age'],
    bins=[0,18,25,35,45,55,100]
)

print(df.groupby('Age Group')['Total Amount'].sum())
#people from age group 45-55 has spent the most and 0-18 the least
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
print(df.groupby('Month')['Total Amount'].sum())
#most of the purchases was in may and the least in september
print(df['Product Category'].value_counts())
print(df.groupby('Product Category')['Total Amount'].sum())
print(df.groupby('Product Category')['Total Amount'].mean())
print(df.groupby('Product Category').agg({
    'Transaction ID':'count',
    'Total Amount':['sum','mean']
}))
import matplotlib.pyplot as plt

df.groupby('Product Category')['Total Amount'].sum().plot(kind='bar')
plt.title('Revenue by Product Category')
plt.show()