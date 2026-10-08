# PetMood AI

### AI-Assisted Pet Mood and Behavior Assistant

PetMood AI is a simple AI-assisted application designed to analyze pet images and provide an estimated mood, basic care recommendations, and safety reminders for dogs and cats.

## Features

* Upload dog or cat images
* Identify pet type
* Estimate pet mood
* Display mood confidence score
* Extract text using OCR
* Provide pet care recommendations
* Display safety reminders

## Technologies Used

* Python
* Streamlit
* Pillow
* Pytesseract
* Tesseract OCR

## Installation

Install the required Python libraries:

```bash
pip install streamlit pillow pytesseract
```

Install Tesseract OCR separately and configure its executable path in `ocr.py`.

## Run the Application

```bash
streamlit run app.py
```

## Live Demo


## Project Structure

```text
PetMood AI/
├── app.py
├── ocr.py
├── requirements.txt
├── packages.txt
└── README.md
```

## Disclaimer

PetMood AI provides AI-assisted estimates for educational purposes only. It is not a veterinary diagnostic tool. Consult a qualified veterinarian if your pet shows unusual behavior or signs of illness.
