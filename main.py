from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_attributes

app = FastAPI(title="Fashion feature extractor")

class ProductRequest(BaseModel):
    text:str

@app.post("/extract")
def extract(product:ProductRequest):
    return predict_attributes(product.text)    