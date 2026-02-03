import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-flash-latest")

def generate_recommendation(crop, disease, confidence):
    prompt = f"""
You are an agriculture expert.

Crop: {crop}
Detected Disease: {disease}
Model Confidence: {confidence}%

Provide:
1. Simple disease explanation
2. Treatment steps
3. Preventive measures
4. Safety tips

Use simple language for farmers.
"""

    response = model.generate_content(prompt)
    return response.text
