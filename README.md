# Fashion Attribute Extractor

## Project Overview

This project converts unstructured fashion product descriptions into structured attributes using Natural Language Processing (NLP) and Machine Learning.

The model extracts the following attributes:

- Silhouette
- Fabric
- Neckline
- Sleeve
- Length
- Embellishment
- Color
- Category

---

## Tech Stack

- Python
- Scikit-learn
- FastAPI
- Pandas
- Joblib

---

## Dataset

- Generated 500 labeled fashion product descriptions.
- Each sample contains:
  - Product description
  - Silhouette
  - Fabric
  - Neckline
  - Sleeve
  - Length
  - Embellishment
  - Color
  - Category

---

## Model

- TF-IDF Vectorizer
- MultiOutputClassifier
- RandomForestClassifier

---

## Evaluation

| Attribute | Accuracy |
|-----------|----------|
| Silhouette | 1.00 |
| Fabric | 1.00 |
| Neckline | 0.81 |
| Sleeve | 0.84 |
| Length | 0.82 |
| Embellishment | 1.00 |
| Color | 0.81 |
| Category | 1.00 |

Overall Macro F1 Score: **0.91**

---

## API

### POST /extract

Example Request

```json
{
    "text": "Lace mermaid wedding dress with long sleeves"
}
```

Example Response

```json
{
    "silhouette": "Mermaid",
    "fabric": "Lace",
    "neckline": "Square",
    "sleeve": "Long Sleeves",
    "length": "Tea",
    "embellishment": "Ruched",
    "color": "Sage",
    "category": "Wedding"
}
```

---

## Running the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train.py
```

Run the API

```bash
uvicorn main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Limitations

- The dataset is synthetically generated.
- The model may predict attributes that are not explicitly mentioned.
- Performance may decrease on unseen writing styles.

