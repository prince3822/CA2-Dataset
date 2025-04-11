import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\HP\Downloads\Python CA ka Dataset.csv")

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Engagement metric (sum of likes, comments, views)
df['engagement'] = df['likes'] + df['comments'] + df['views']

# Scatter plot: Duration vs Engagement
plt.figure(figsize=(10, 6))
plt.scatter(df['duration'], df['engagement'], alpha=0.6, color='mediumblue')
plt.xlabel('Video Duration (in minutes or seconds)')
plt.ylabel('Engagement (Likes + Comments + Views)')
plt.title('Duration vs Engagement')
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter plot: Duration vs Likes
plt.figure(figsize=(10, 6))
plt.scatter(df['duration'], df['likes'], alpha=0.6, color='seagreen')
plt.xlabel('Video Duration')
plt.ylabel('Likes')
plt.title('Duration vs Likes')
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter plot: Duration vs Comments
plt.figure(figsize=(10, 6))
plt.scatter(df['duration'], df['comments'], alpha=0.6, color='darkorange')
plt.xlabel('Video Duration')
plt.ylabel('Comments')
plt.title('Duration vs Comments')
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation matrix for duration and engagement metrics
engage_cols = ['duration', 'likes', 'comments', 'views', 'engagement']
correlation = df[engage_cols].corr()
print("\nCorrelation Matrix:\n", correlation)
