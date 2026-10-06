import os
import json
import base64
from io import BytesIO

from PIL import Image
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found in .env file")


client = InferenceClient(
    provider="auto",
    api_key=HF_TOKEN
)


MODEL = "google/gemma-3-4b-it"


def analyze_pet(image):

    buffer = BytesIO()
    image.save(buffer, format="JPEG")

    image_data = base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")

    prompt = """
Analyze this pet image carefully.

Return ONLY valid JSON using exactly these keys:

{
  "mood": "",
  "activity": "",
  "body_language": "",
  "safety": "",
  "interaction": "",
  "visible_clues": ""
}

Instructions:

1. Analyze ONLY what is visible in the image.
2. Do not invent details.
3. Give a POSSIBLE mood, not a confirmed emotion.
4. Describe visible body language such as ears, tail, posture,
   head position and facial appearance when visible.
5. Identify the visible activity.
6. Check the visible surroundings for obvious safety concerns.
7. Give a simple interaction suggestion based on the visible behavior.
8. If something cannot be determined from the image, say:
   "Cannot determine from image".
9. Do not provide a medical diagnosis.
"""

    image_url = f"data:image/jpeg;base64,{image_data}"

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ],
        max_tokens=500
    )

    result = response.choices[0].message.content

    result = result.strip()

    if result.startswith("```"):
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

    return json.loads(result)
