import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image):
    try:
        text = pytesseract.image_to_string(image)

        if text.strip():
            return text.strip()

        return "No readable text detected in the image."

    except Exception as error:
        return f"OCR error: {error}"


def detect_mood(text):
    text = text.lower()

    playful_words = [
        "playful", "happy", "playing", "fun",
        "excited", "sprint", "play", "best feelings"
    ]

    relaxed_words = [
        "relaxed", "calm", "sleepy",
        "resting", "peaceful", "sleep"
    ]

    alert_words = [
        "alert", "attention", "watch out",
        "warning", "danger"
    ]

    scared_words = [
        "scared", "afraid", "fear",
        "nervous", "anxious", "frightened"
    ]

    angry_words = [
        "angry", "aggressive", "attack",
        "attacking", "mad"
    ]

    if any(word in text for word in playful_words):
        return "PLAYFUL"

    elif any(word in text for word in relaxed_words):
        return "RELAXED"

    elif any(word in text for word in scared_words):
        return "SCARED"

    elif any(word in text for word in angry_words):
        return "AGGRESSIVE"

    elif any(word in text for word in alert_words):
        return "ALERT"

    else:
        return "UNKNOWN"

