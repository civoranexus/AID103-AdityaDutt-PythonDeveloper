from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
from model.predict import predict_disease
from model.recommendation import generate_recommendation

load_dotenv()

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({"status": "CropGuard AI backend running"})

@app.route("/predict", methods=["POST"])
def predict():
    image = request.files.get("image")
    crop_type = request.form.get("crop_type")
    growth_stage = request.form.get("growth_stage")

    if not image or not crop_type:
        return jsonify({"error": "Image and crop type required"}), 400

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    disease, confidence = predict_disease(image_path)
    recommendation = generate_recommendation(crop_type, disease, confidence)

    return jsonify({
        "crop": crop_type,
        "disease": disease,
        "confidence": confidence,
        "recommendation": recommendation
    })

@app.route("/result")
def result():
    return render_template(
        "result.html",
        crop=request.args.get("crop"),
        disease=request.args.get("disease"),
        confidence=request.args.get("confidence"),
        recommendation=request.args.get("recommendation")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
