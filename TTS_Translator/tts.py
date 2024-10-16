import sys
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from gtts import gTTS
from io import BytesIO
import os
from datetime import datetime
from typing import Optional

# Optional seed for language detection (useful for consistent results in tests)
# DetectorFactory.seed = 0

# Supported languages dictionary
LANGUAGES = {
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

BASE_DIR = "audios"  # Base directory for storing audio files

def clear_console():
    """Clear the console based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def detect_language(text: str) -> Optional[str]:
    """Detect the language of the given text."""
    try:
        return detect(text)
    except LangDetectException:
        print("The language of the text could not be detected.")
        return None

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """Translate the given text using GoogleTranslator."""
    return GoogleTranslator(source=source_lang, target=target_lang).translate(text)

def save_audio(text: str, lang: str, directory: str):
    """Generate and save the audio file for the translated text."""
    try:
        # Generate audio
        mp3_fp = BytesIO()
        tts = gTTS(text=text, lang=lang, tld='com')  # Adjust TLD if needed
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        # Prepare filename and path
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"audio_{lang}.{timestamp}.mp3"
        filepath = os.path.join(directory, filename)

        # Save the audio file
        with open(filepath, 'wb') as f:
            f.write(mp3_fp.read())
        print(f"Generated audio file: {filepath}")

    except Exception as e:
        print(f"Error generating audio for {lang}: {e}")

def detect_and_translate(text: str):
    """Detect language, translate text to multiple languages, and generate audio."""
    if not text.strip():
        print("The text provided is empty.")
        return

    # Detect the language of the input text
    source_language = detect_language(text)
    if not source_language:
        return

    source_lang_name = LANGUAGES.get(source_language, "Unknown")
    print(f"Language detected: {source_lang_name} ({source_language})")

    # Ensure the base directory for audio files exists
    os.makedirs(BASE_DIR, exist_ok=True)

    # Translate and generate audio for each supported language
    for lang_code, lang_name in LANGUAGES.items():
        try:
            translated_text = translate_text(text, source_lang=source_language, target_lang=lang_code)
            print(f"\n{lang_name} ({lang_code}):\n{translated_text}\n")

            # Create directory for the specific language
            lang_dir = os.path.join(BASE_DIR, lang_name.replace(" ", "_"))
            os.makedirs(lang_dir, exist_ok=True)

            # Save the translated audio
            save_audio(translated_text, lang=lang_code, directory=lang_dir)

        except Exception as e:
            print(f"Error processing {lang_name} ({lang_code}): {e}")

def main():
    """Main function to handle user input and call the translation logic."""
    clear_console()

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = input("Enter the text you want to translate: ")

    detect_and_translate(text)

if __name__ == "__main__":
    main()
