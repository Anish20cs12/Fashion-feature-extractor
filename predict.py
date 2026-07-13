import joblib


model = joblib.load("model/attribute_model.pkl")
vectorizer = joblib.load("model/tfidf.pkl")

print("Model and Vectorizer loaded successfully")

columns = [
    "silhouette",
    "fabric",
    "neckline",
    "sleeve",
    "length",
    "embellishment",
    "color",
    "category"
]

def predict_attributes(description:str):
    X = vectorizer.transform([description])

    prediction = model.predict(X)[0]

    result = dict(zip(columns,prediction))

    return result



if __name__ == "__main__":
    text = input("Product description: ")
    print(predict_attributes(text))