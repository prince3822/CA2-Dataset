import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\HP\Downloads\Python CA ka Dataset.csv")  # Adjust path if needed

# Show original column names
print("Original Columns:\n", df.columns.tolist())

# Clean column names for consistency
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Print cleaned column names
print("\nCleaned Columns:\n", df.columns.tolist())

# Display basic info and stats
print("\nDataset Info:\n")
print(df.info())
print("\nSummary Statistics:\n")
print(df.describe(include='all'))

# Check if required columns exist
required_cols = ['views', 'likes', 'comments', 'watch_time']
for col in required_cols:
    if col not in df.columns:
        print(f"Missing expected column: {col}")
        
# Safely identify the title-like column
title_col = next((col for col in df.columns if 'title' in col), None)
if title_col:
    top_views = df.sort_values(by='views', ascending=False).head(5)
    print(f"\nTop 5 Videos by Views:\n", top_views[[title_col, 'views']])
else:
    print("No title-like column found for videos.")

# Correlation matrix
metrics = [col for col in ['views', 'likes', 'comments', 'watch_time'] if col in df.columns]
if len(metrics) >= 2:
    correlation = df[metrics].corr()
    print("\nCorrelation Matrix:\n", correlation)

# Visualization - Top 10 videos by views
if title_col and 'views' in df.columns:
    top_10 = df.sort_values(by='views', ascending=False).head(10)
    plt.figure(figsize=(12,6))
    plt.barh(top_10[title_col], top_10['views'], color='skyblue')
    plt.xlabel('Views')
    plt.title('Top 10 Videos by Views')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

# Scatter plot - Views vs Likes
if 'views' in df.columns and 'likes' in df.columns:
    plt.figure(figsize=(8,6))
    plt.scatter(df['views'], df['likes'], alpha=0.6, color='green')
    plt.xlabel('Views')
    plt.ylabel('Likes')
    plt.title('Views vs Likes')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Line chart - Views over time
if 'upload_date' in df.columns and 'views' in df.columns:
    df['upload_date'] = pd.to_datetime(df['upload_date'], errors='coerce')
    df_sorted = df.sort_values(by='upload_date')
    plt.figure(figsize=(10,5))
    plt.plot(df_sorted['upload_date'], df_sorted['views'], marker='o')
    plt.title('Views Over Time')
    plt.xlabel('Upload Date')
    plt.ylabel('Views')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
