import torch
import numpy as np
import cv2
from ultralytics import YOLO
from io import BytesIO

model = YOLO("models/yolov8n.pt")  # pakai model ringan dulu

def predict_image(image_bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    results = model(img)
    return results[0].tojson()
