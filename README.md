# MACHINE-LEARNING-MODEL-IMPLEMENTATION_4

**COMPANY** : CODTECH IT SOLUTIONS
**NAME** : VELIVALA TONY KUMAR
**INTERN ID** : CT12TQS
**DOMAIN** : Python Programming
**BATCH DURATION** : FEB 10 2025 to APRIL 10 2025
**MENTOR NAME** : Neela Santhosh Kumar
#Descrption 



---

Task 4: Machine Learning Model Implementation – Description of Work Performed

As part of the internship with CodTech, Task 4 focused on implementing a machine learning (ML) model using Scikit-learn to predict or classify outcomes based on a dataset. This task was not only an excellent opportunity to understand how machine learning works in real-world applications, but also gave hands-on experience with the complete ML workflow—from data preprocessing to model training and evaluation.


---

Objective of the Task

The goal of this task was to:

Create a predictive machine learning model using the scikit-learn library.

Use a relevant dataset (for example, spam email detection, customer churn prediction, or Iris classification).

Demonstrate the complete ML pipeline including data preprocessing, feature selection, model training, and evaluation.

Deliver the work in the form of a Jupyter Notebook that clearly documents the entire process.



---

Technology Stack Used

Programming Language: Python

Library: Scikit-learn (for ML algorithms), Pandas (for data manipulation), Matplotlib/Seaborn (for visualization)

Platform: Jupyter Notebook

Dataset: SMS Spam Detection Dataset (CSV format)



---

Steps and Execution

1. Importing Libraries and Dataset

The first step involved importing necessary libraries and loading the dataset using Pandas. The dataset contained SMS messages labeled as either “spam” or “ham” (not spam).

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

2. Data Cleaning and Preprocessing

The data required preprocessing before feeding it into the model. This involved:

Removing null values

Converting text to lowercase

Tokenization

Vectorization using CountVectorizer to transform text into numerical data


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']

3. Splitting the Data

The data was split into training and testing sets (typically 80% training, 20% testing) to evaluate model performance properly.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

4. Model Selection and Training

I selected the Multinomial Naive Bayes algorithm because it's well-suited for text classification problems. The model was trained on the training data.

model = MultinomialNB()
model.fit(X_train, y_train)

5. Model Evaluation

After training, the model was evaluated using the test set. Metrics such as accuracy, precision, recall, and F1-score were computed.

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

Sample Output:

Accuracy: 0.98
Precision: 0.97
Recall: 0.95

These results indicated that the model was highly accurate in predicting spam messages.

6. Visualization (Optional)

To visualize the distribution of spam vs ham, I used Matplotlib and Seaborn.

import seaborn as sns
sns.countplot(data=df, x='label')


---

Challenges Faced

Text Preprocessing was tricky, especially cleaning and transforming raw text into features that a model can understand.

Choosing the right ML model was important. I also experimented with Logistic Regression and Decision Trees.

Overfitting had to be monitored by comparing training and testing accuracy.



---

Learning Outcomes

This task helped me gain practical knowledge in:

Understanding real-world datasets

Applying ML techniques to solve classification problems

Preprocessing textual data

Evaluating and tuning machine learning models

Documenting the entire process clearly in a Jupyter notebook



---

Conclusion

Task 4 was one of the most insightful tasks in my internship. It allowed me to move from theoretical understanding of machine learning to actual implementation. I now feel confident in building and evaluating machine learning models using scikit-learn and Python. This hands-on experience has deepened my interest in data science and AI.


---
#output
![Image](https://github.com/user-attachments/assets/c792fb3f-15a4-4e30-b19e-1f0dabfc157f)
