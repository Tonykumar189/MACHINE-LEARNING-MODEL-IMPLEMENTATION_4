import pandas as pd

# Create a simple dataset
data = {
    'label': ['ham', 'spam', 'ham', 'spam', 'ham'],
    'message': [
        "Hey, how are you doing?",
        "Congratulations! You've won a $1000 Walmart gift card.",
        "Are we still meeting later?",
        "You have been selected for a free cruise. Call now!",
        "Let's catch up tomorrow."
    ]
}

df = pd.DataFrame(data)
df.to_csv('spam_detection_sample.csv', index=False)

from google.colab import files
files.download('spam_detection_sample.csv')
