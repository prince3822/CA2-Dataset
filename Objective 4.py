import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\HP\Downloads\Python CA ka Dataset.csv")

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Create controversy metrics
df['dislike_like_ratio'] = df['dislikes'] / (df['likes'] + 1)
df['dislike_view_ratio'] = df['dislikes'] / (df['views'] + 1)

# Top 10 controversial videos
top_controversial = df.sort_values(by='dislike_like_ratio', ascending=False).head(10)
print(top_controversial[['dislikes', 'likes', 'views', 'dislike_like_ratio', 'dislike_view_ratio']])

# Histogram of dislike/like ratio
plt.figure(figsize=(10, 6))
plt.hist(df['dislike_like_ratio'], bins=30, color='crimson', edgecolor='black')
plt.title("Distribution of Dislike-to-Like Ratio")
plt.xlabel("Dislike/Like Ratio")
plt.ylabel("Number of Videos")
plt.grid(True)
plt.tight_layout()
plt.show()

# Dislike/like ratio over time
df['upload_date'] = pd.to_datetime(df['upload_date'], errors='coerce')
df = df.sort_values('upload_date')

plt.figure(figsize=(12, 6))
plt.plot(df['upload_date'], df['dislike_like_ratio'], marker='o', linestyle='-', alpha=0.7, color='darkred')
plt.title("Dislike-to-Like Ratio Over Time")
plt.xlabel("Upload Date")
plt.ylabel("Dislike/Like Ratio")
plt.grid(True)
plt.tight_layout()
plt.show()

# Category-wise average controversy
df['category'] = df['category'].astype(str)  # ensure category is string
cat_group = df.groupby('category')[['dislike_like_ratio', 'dislike_view_ratio']].mean().sort_values(by='dislike_like_ratio', ascending=False)

cat_group.plot(kind='bar', figsize=(12, 6), color=['orangered', 'gold'])
plt.title("Average Dislike Ratios by Category")
plt.ylabel("Ratio")
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.tight_layout()
plt.show()
