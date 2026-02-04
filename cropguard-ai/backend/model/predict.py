import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "cropguard_model.h5")

model = load_model(MODEL_PATH)

CLASS_NAMES = [
    "Tomato___Late_blight",
    "Tomato___Early_blight",
    "Tomato___Healthy"
]

def predict_disease(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    confidence = float(np.max(preds)) * 100
    class_index = int(np.argmax(preds))

    return CLASS_NAMES[class_index], round(confidence, 2)
