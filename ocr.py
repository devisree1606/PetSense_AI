import os
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text(image):
    try:
        image = image.convert("RGB")
        text = pytesseract.image_to_string(image, lang="eng")
        return text.strip()
    except Exception as e:
        return ""

def detect_mood(text):
    text = text.lower()

    keywords = {
        "PLAYFUL": ["playful", "playing", "excited", "sprint"],
        "RELAXED": ["relaxed", "calm", "sleepy", "peaceful"],
        "ALERT": ["alert", "attention", "warning"],
        "SCARED": ["scared", "afraid", "fear", "nervous"],
        "AGGRESSIVE": ["aggressive", "angry", "attack"]
    }

    for mood, words in keywords.items():
        if any(word in text for word in words):
            return mood

    return "UNKNOWN"
