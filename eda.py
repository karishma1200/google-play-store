import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("apps_data.csv")

# Example EDA: Show basic info and statistics
print(df.info())
print(df.describe())

# Example visualization: Distribution of app ratings
if 'Rating' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Rating'].dropna(), bins=20, kde=True)
    plt.title('Distribution of App Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.show()
else:
    print("'Rating' column not found in data.")
