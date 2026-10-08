import pytesseract
from PIL import Image, ImageEnhance, ImageOps

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image):
    try:
        image = image.convert("RGB")
        image = ImageOps.grayscale(image)

        # Resize image
        image = image.resize(
            (image.width * 2, image.height * 2)
        )

        # Improve contrast
        image = ImageEnhance.Contrast(image).enhance(2.5)

        # Extract text
        text = pytesseract.image_to_string(
            image, config="--oem 3 --psm 11"
        )

        return text.strip() if text.strip() else "No readable text found."

    except Exception as e:
        return f"OCR Error: {e}"

