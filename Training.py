import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("Emotions.csv")

ve=TfidfVectorizer(
    stop_words="english",
    lowercase=True,
    max_features=6000,
    ngram_range=(1,2))
x=ve.fit_transform(df['sentence'])
le=LabelEncoder()
y=le.fit_transform(df['emotion'])

model=LogisticRegression(max_iter=2000)
model.fit(x, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(ve, open("vectorizer.pkl", "wb"))
pickle.dump(le, open("label_encoder.pkl", "wb"))