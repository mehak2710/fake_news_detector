import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("fake_news.csv")

# Features and Labels
X = df["text"]
y = df["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vectorized, y)


def predict_news(news_text):
    news_vector = vectorizer.transform([news_text])
    prediction = model.predict(news_vector)
    return prediction[0]