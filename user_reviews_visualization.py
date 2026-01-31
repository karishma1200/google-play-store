import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the user reviews dataset
file_path = "googleplaystore_user_reviews (1).csv"
df = pd.read_csv(file_path)

# Drop rows with all NaN values
if 'Sentiment' in df.columns:
    df = df.dropna(subset=['Sentiment'])

# Plot sentiment distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Sentiment', data=df, order=df['Sentiment'].value_counts().index)
plt.title('Sentiment Distribution of User Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('sentiment_distribution.png')
plt.show()

# Plot sentiment polarity distribution
if 'Sentiment_Polarity' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Sentiment_Polarity'].dropna(), bins=30, kde=True)
    plt.title('Sentiment Polarity Distribution')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('sentiment_polarity_distribution.png')
    plt.show()

# Plot sentiment subjectivity distribution
if 'Sentiment_Subjectivity' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Sentiment_Subjectivity'].dropna(), bins=30, kde=True)
    plt.title('Sentiment Subjectivity Distribution')
    plt.xlabel('Sentiment Subjectivity')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('sentiment_subjectivity_distribution.png')
    plt.show()
