import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv(r"C:\Users\HP\Downloads\Python CA ka Dataset.csv")

# 1. Strip whitespace from column names
df.columns = df.columns.str.strip()

# 2. Fill missing numeric values with 0
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# 3. Convert 'Upload_Date' column to datetime if it exists
if 'Upload_Date' in df.columns:
    df['Upload_Date'] = pd.to_datetime(df['Upload_Date'], errors='coerce')
    df = df.dropna(subset=['Upload_Date'])

# 4. Convert float columns with only integers to int type
for col in numeric_cols:
    if df[col].dropna().apply(float.is_integer).all():
        df[col] = df[col].astype(int)

# 5. Save the cleaned dataset
output_path = r"C:\Users\HP\Downloads\Python CA ka Dataset.csv"  # Change to your desired location
df.to_csv(output_path, index=False)

print("Cleaned dataset saved to:", output_path)
