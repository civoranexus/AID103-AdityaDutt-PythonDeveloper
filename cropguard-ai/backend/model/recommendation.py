import os
from google import genai

# Create client using API key
client = genai.Client(api_key="AIzaSyA3cNJS6Xg7h-vIkzoD3uqrSz7VjQrcbQk")

def generate_recommendation(crop, disease, confidence):
    prompt = f"""
You are an agricultural expert.

Crop: {crop}
Detected Disease: {disease}
Model Confidence: {confidence}%

Provide:
1. Simple disease explanation
2. Treatment steps
3. Preventive measures
4. Safety tips

Use simple language suitable for farmers.
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text
