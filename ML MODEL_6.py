# Test a sample message
sample = ["Congratulations! You have won a free ticket to Bahamas. Call now!"]
sample_vec = vectorizer.transform(sample)
prediction = model.predict(sample_vec)
print("Prediction:", "Spam" if prediction[0] == 1 else "Ham")
