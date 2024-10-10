import sys
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from gtts import gTTS
from io import BytesIO
import os
from os import system, name
from datetime import datetime

# Optional seed for language detection
# DetectorFactory.seed = 0

# Language dictionary
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

# Define clear function to clear the console
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def detect_and_translate(text):
    if not text.strip():
        print("The text provided is empty.")
        return

    try:
        # Detect language
        language = detect(text)
        language_name = idiomas.get(language, "Unknown")
        print(f"Language detected: {language_name} ({language})")

        # Create base directory for saved audios
        base_dir = 'audios'
        os.makedirs(base_dir, exist_ok=True)

        # Translate and generate audio for each language
        for codigo, nombre in idiomas.items():
            traduccion = GoogleTranslator(source=language, target=codigo).translate(text)
            print(f"{nombre} ({codigo}) \n{traduccion} \n")
            
            # Generate audio for the translation
            lang, tld = codigo, 'com'  # Default TLD; modify as needed based on logic
            mp3_fp = BytesIO()
            tts = gTTS(text=traduccion, lang=lang, tld=tld)
            tts.write_to_fp(mp3_fp)

            # Create a directory for the language if it doesn't exist
            lang_dir = os.path.join(base_dir, nombre.replace(" ", "_"))
            os.makedirs(lang_dir, exist_ok=True)

            # Save audio file
            now = datetime.now()
            timestamp = now.strftime("%Y%m%d_%H%M%S")
            mp3_fp.seek(0)
            filename = f"audio_{lang}.{tld}.{timestamp}.mp3"
            filepath = os.path.join(lang_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(mp3_fp.read())
            print(f"Generated audio file: {filepath}")

    except LangDetectException:
        print("The language of the text could not be detected.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    clear()
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        detect_and_translate(text)
    else:
        text = input("Enter the text you want to translate: ")
        detect_and_translate(text)
