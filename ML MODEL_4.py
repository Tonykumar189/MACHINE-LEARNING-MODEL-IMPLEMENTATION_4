import pandas as pd

# Load uploaded CSV
df = pd.read_csv('spam_detection_sample.csv')

# Rename columns if needed
df.columns = ['label', 'message']

# Convert labels to binary
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Drop missing values
df.dropna(inplace=True)

print(df.head())
