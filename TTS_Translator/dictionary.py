import sys
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import json
import os

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

def generate_full_dictionary(words):
    complete_dictionary = {}

    for word in words:
        try:
            # Detecting the language (using Spanish as default if the input is not in Spanish)
            language = detect(word)
            translations = {}

            # Translate the word into each available language
            for code in idiomas.keys():
                translation = GoogleTranslator(source=language, target=code).translate(word)
                translations[idiomas[code]] = translation

            # Add to the complete dictionary
            complete_dictionary[word] = translations
        except LangDetectException:
            print(f"Could not detect language for: {word}. Skipping.")
        except Exception as e:
            print(f"An error occurred while translating '{word}': {e}")

    return complete_dictionary

if __name__ == "__main__":
    # List of words to be translated
    words_to_translate = ["hello", "world", "goodbye", "friend", "thank you"]

    full_dictionary = generate_full_dictionary(words_to_translate)

    # Optionally, save the dictionary to a JSON file
    with open('complete_dictionary.json', 'w', encoding='utf-8') as f:
        json.dump(full_dictionary, f, ensure_ascii=False, indent=4)

    print("Translation complete. Dictionary saved as 'complete_dictionary.json'.")
