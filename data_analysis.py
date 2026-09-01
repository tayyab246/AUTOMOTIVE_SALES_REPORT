import pandas as pd

# Load the raw dataset
df = pd.read_csv('Car_sales.csv')

# 1. Drop entirely empty columns
df.drop(columns=['Unnamed: 16'], inplace=True, errors='ignore')

# 2. Clean 'Price_in_thousands' (remove '$' and convert to numeric)
df['Price_in_thousands'] = df['Price_in_thousands'].astype(str).str.replace('$', '', regex=False)
df['Price_in_thousands'] = pd.to_numeric(df['Price_in_thousands'], errors='coerce')

# 3. CONVERT TO ACTUAL VALUES (Multiply by 1000)
# This converts Sales, Price, and Resale Value from thousands to whole numbers
df['Sales'] = df['Sales_in_thousands'] * 1000
df['Price'] = df['Price_in_thousands'] * 1000
df['Resale_Value'] = df['__year_resale_value'] * 1000

# 4. Handle missing values
# Fill numerical columns with the median
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
 
# 5. Fix Date format
df['Latest_Launch'] = pd.to_datetime(df['Latest_Launch'], errors='coerce')

# 6. Final Column Selection & Cleanup
# We keep only the new actual values and remove the old 'in_thousand' columns
cols_to_drop = ['Sales_in_thousands', 'Price_in_thousands', '__year_resale_value']
df.drop(columns=cols_to_drop, inplace=True)

# Save the fully cleaned dataset
df.to_csv('cleaned_car_sales.csv', index=False)
print("Data Cleaning Complete")