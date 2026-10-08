
import pytesseract
from PIL import Image
import os

if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )


def extract_text_from_image(image):
    try:
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"OCR Error: {e}"


def extract_text_from_pdf_image(image):
    try:
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"OCR Error: {e}"

