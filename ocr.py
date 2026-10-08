
import pytesseract
from PIL import Image, ImageEnhance, ImageOps

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image):
    try:
        image = ImageOps.grayscale(image)
        image = ImageEnhance.Contrast(image).enhance(2.0)

        text = pytesseract.image_to_string(
            image, config="--oem 3 --psm 6"
        )
        return text.strip() if text.strip() else "No text found"

    except Exception:
        return ""


def detect_mood(text):
    text = text.lower()

    moods = {
        "PLAYFUL": ["playful", "happy", "playing", "excited", "running"],
        "RELAXED": ["relaxed", "calm", "sleeping", "resting", "peaceful"],
        "ANGRY": ["angry", "aggressive", "growling", "furious"],
        "SCARED": ["scared", "afraid", "frightened", "nervous"]
    }

    for mood, words in moods.items():
        if any(word in text for word in words):
            return mood

    return "UNKNOWN"
    
