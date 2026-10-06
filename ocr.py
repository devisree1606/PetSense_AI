
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image):
    try:
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return ""


def detect_mood(text):
    text = text.lower()

    playful_words = [
        "playful", "happy", "playing", "fun",
        "excited", "sprint", "play", "joy",
        "energetic", "running"
    ]

    relaxed_words = [
        "relaxed", "calm", "sleeping", "sleep",
        "resting", "peaceful", "quiet", "comfortable"
    ]

    angry_words = [
        "angry", "aggressive", "attack", "growling",
        "barking", "furious", "threat"
    ]

    scared_words = [
        "scared", "afraid", "fear", "frightened",
        "hiding", "nervous", "anxious"
    ]

    if any(word in text for word in playful_words):
        return "PLAYFUL"

    if any(word in text for word in relaxed_words):
        return "RELAXED"

    if any(word in text for word in angry_words):
        return "ANGRY"

    if any(word in text for word in scared_words):
        return "SCARED"

    return "UNKNOWN"

