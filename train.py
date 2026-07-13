import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score,f1_score

import joblib
import os

df = pd.read_csv("dataset/train.csv")
print(df.head())


X = df["description"]
y = df.drop(columns=["description"])

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
x_test = vectorizer.transform(X_test)

model = MultiOutputClassifier(
    RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
)
model.fit(X_train,y_train)

print("Model trained Successfully")

y_pred = model.predict(x_test)
print("Accuracy of each Attribute:\n")

for i,column in enumerate(y.columns):
    acc = accuracy_score(y_test.iloc[:,i],y_pred[:,i])
    print(f"{column}:{acc:.2f}")

f1_scores = []

for i, column in enumerate(y.columns):
    f1 = f1_score(
        y_test.iloc[:, i],
        y_pred[:, i],
        average="macro"
    )

    f1_scores.append(f1)

    print(f"{column}: {f1:.2f}")

overall_f1 = sum(f1_scores) / len(f1_scores)

print(f"\nOverall Macro F1 Score: {overall_f1:.2f}")

os.makedirs("model",exist_ok=True)

joblib.dump(model,"model/attribute_model.pkl")
joblib.dump(vectorizer,"model/tfidf.pkl")

print("Model and tfidf saved successfully")