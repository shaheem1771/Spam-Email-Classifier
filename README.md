# Spam Email Classifier

A Machine Learning project that classifies SMS/Email messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing and the Naive Bayes algorithm.

-----

## Project Overview

Spam detection is one of the most practical applications of Machine Learning in the real world. This project applies NLP techniques and a Multinomial Naive Bayes classifier to accurately identify spam messages from a labeled SMS dataset, enabling automated filtering of unwanted content.

-----

## Dataset

**SMS Spam Collection Dataset**

- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- 5,572 SMS messages labeled as **Spam** or **Ham**
- Target Variable: Label (spam / ham)

-----

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes

-----

## Machine Learning Model

**Multinomial Naive Bayes with TF-IDF Vectorization**

```
TfidfVectorizer()  →  MultinomialNB()
```

TF-IDF (Term Frequency–Inverse Document Frequency) converts raw text into numerical features, which are then fed into the Naive Bayes classifier for binary classification.

-----

## Model Performance

|Metric          |Score |
|----------------|------|
|Accuracy        |96.68%|
|Precision (Ham) |0.96  |
|Recall (Ham)    |1.00  |
|F1-Score (Ham)  |0.98  |
|Precision (Spam)|1.00  |
|Recall (Spam)   |0.80  |
|F1-Score (Spam) |0.89  |

-----

## Project Structure

```
Spam-Email-Classifier
│
├── Spam_Email_Classifier_Project.ipynb   # Main notebook
├── requirements.txt                       # Dependencies
└── README.md
```

-----

## Key Findings

- Achieved **96.68%** classification accuracy on the test set.
- TF-IDF vectorization effectively captures important spam-related keywords.
- Multinomial Naive Bayes performs exceptionally well for text classification tasks.
- Spam class precision of 1.00 means virtually zero false positives (legitimate emails never marked as spam).

-----

## Future Improvements

- Hyperparameter tuning for TF-IDF (n-grams, max features)
- Try Support Vector Machine (SVM) for comparison
- Add word cloud visualization for spam vs. ham messages
- Handle class imbalance with oversampling (SMOTE)
- Deploy as a web app using Streamlit

-----

## Author

**Muhammed Shaheem**

B.Tech Computer Science and Engineering

GitHub: [shaheem1771](https://github.com/shaheem1771)
