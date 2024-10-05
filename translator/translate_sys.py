import sys
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Set seed for language detection (optional)
DetectorFactory.seed = 0

# Language dictionary with codes and names
idiomas = {
    "es": "Spanish",
    "en": "English",
    "pt": "Portuguese",
    "de": "German",
    "fr": "French",
    "it": "Italian",
    "zh-TW": "Chinese (Traditional)",
    "ar": "Arabic",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "hi": "Hindi"
}

def main(text):
    try:
        # Detect the language of the input text
        idioma_detectado = detect(text)
        nombre_idioma_detectado = idiomas.get(idioma_detectado, "Unknown")

        # If the language is unknown, set Spanish as the source language
        if nombre_idioma_detectado == "Unknown":
            idioma_detectado = "es"  # Spanish as a source language
            nombre_idioma_detectado = "Spanish"  # Update name

        print(f"Language detected: {nombre_idioma_detectado} ({idioma_detectado})")

        # Translate the text into all languages ​​in the dictionary
        for codigo, nombre in idiomas.items():
            traduccion = GoogleTranslator(source=idioma_detectado, target=codigo).translate(text)
            print(f"TTranslation to {nombre} ({codigo}): {traduccion}")

    except LangDetectException:
        print("The language of the text could not be detected.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter the text you want to translate as an argument")
    else:
        # Combine all command line arguments into a single text
        text = " ".join(sys.argv[1:])
        main(text)
