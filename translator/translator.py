import sys
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Set seed for language detection (optional)
# DetectorFactory.seed = 0

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

def detect_and_translate(text):
    # Validate if the text is empty or too short
    if not text.strip():
        print("The text provided is empty.")
        return
    # if len(text) < 20:
    #     print("The text is too short to detect the language.")
    #     return
    
    try:
        # Detect the language of the input text
        language = detect(text)
        language_name = idiomas.get(language, "Unknown")

        # If the detected language is unknown, set Spanish as the default
        # if language_name == "Unknown":
        #     language = "es"
        #     language_name = "Spanish"

        print(f"Language detected: {language_name} ({language})")
        
        #  # Translate to English if not already in English
        # if language != "en":
        #     traduccion_en = GoogleTranslator(source=language, target='en').translate(text)
        #     print(f"Translation to English: {traduccion_en}")
        # else:
        #     print("The text is already in English.")

        # Optionally, translate to all other languages
        for codigo, nombre in idiomas.items():
            if codigo != language:  # Avoid redundant translation
                traduccion = GoogleTranslator(source=language, target=codigo).translate(text)
                print(f"Translation to {nombre} ({codigo}): {traduccion}")

    except LangDetectException:
        print("The language of the text could not be detected.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If text is provided as a command-line argument
        text = " ".join(sys.argv[1:])
        detect_and_translate(text)
    else:
        # Interactive input if no argument is provided
        text = input("Enter the text you want to translate: ")
        detect_and_translate(text)