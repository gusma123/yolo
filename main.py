from fastapi import FastAPI, File, UploadFile
from app.predict import predict_image

app = FastAPI()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    result = predict_image(contents)
    return result
