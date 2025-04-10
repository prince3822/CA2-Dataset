import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\HP\Downloads\Python CA ka Dataset.csv")

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Print column names to find the category column
print("Available columns:\n", df.columns.tolist())

# Try to detect category column
category_col = next((col for col in df.columns if 'category' in col), None)

if category_col is None:
    print("No category column found.")
else:
    print(f"\nUsing category column: {category_col}")

    # Group by category and calculate average metrics
    metrics = ['views', 'likes', 'comments', 'watch_time']
    available_metrics = [m for m in metrics if m in df.columns]
    
    category_summary = df.groupby(category_col)[available_metrics].mean().sort_values(by='views', ascending=False)
    
    print("\nCategory-wise Average Performance:\n", category_summary)

    # Plotting views per category
    if 'views' in category_summary.columns:
        plt.figure(figsize=(10,6))
        category_summary['views'].plot(kind='bar', color='skyblue')
        plt.ylabel("Average Views")
        plt.title("Category-wise Average Views")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    # Plotting all available metrics per category
    category_summary.plot(kind='bar', figsize=(12, 7))
    plt.title("Category-wise Average Metrics")
    plt.ylabel("Average Value")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
