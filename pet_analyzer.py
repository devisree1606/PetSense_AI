
from PIL import Image


def analyze_pet(image, pet_type="Dog"):
    width, height = image.size

    if width > 1000 and height > 1000:
        quality = 90
    elif width > 500 and height > 500:
        quality = 80
    else:
        quality = 70

    if pet_type == "Dog":
        mood = "PLAYFUL"
        score = quality
        description = "The dog may be showing playful or energetic behavior."
        recommendation = "Provide safe play time, exercise and positive interaction."

    elif pet_type == "Cat":
        mood = "RELAXED"
        score = quality
        description = "The cat may be showing calm or relaxed behavior."
        recommendation = "Allow the cat to rest comfortably and provide a quiet environment."

    else:
        mood = "UNKNOWN"
        score = 0
        description = "The pet mood could not be estimated reliably."
        recommendation = "Observe the pet's body language and behavior carefully."

    return {
        "mood": mood,
        "score": score,
        "description": description,
        "recommendation": recommendation,
        "pet": pet_type
    }

