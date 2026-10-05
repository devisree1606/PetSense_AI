```python
from PIL import Image


def analyze_pet(image):

    try:

        if image is None:
            return {
                "pet": "No image uploaded",
                "description": "Please upload a pet image.",
                "health": "Unable to analyze",
                "care": "Please upload a clear pet image."
            }

        if not isinstance(image, Image.Image):
            image = Image.open(image)

        image = image.convert("RGB")

        width, height = image.size

        if width < 100 or height < 100:
            return {
                "pet": "Image too small",
                "description": "The uploaded image is too small.",
                "health": "Unable to determine.",
                "care": "Please upload a clearer image."
            }

        return {
            "pet": "Pet detected",
            "description": (
                "The uploaded image appears to contain a pet. "
                "Basic visual observations can be made from the image."
            ),
            "health": (
                "No definite medical condition can be diagnosed "
                "from an image alone. Look for visible changes "
                "in the eyes, skin, fur, posture, or behavior."
            ),
            "care": (
                "Provide clean water, proper food, regular grooming, "
                "and veterinary care if unusual symptoms are noticed."
            )
        }

    except Exception:

        return {
            "pet": "Analysis failed",
            "description": "The image could not be processed.",
            "health": "Unable to analyze the image.",
            "care": "Please upload a clear JPG or PNG image."
        }


        
