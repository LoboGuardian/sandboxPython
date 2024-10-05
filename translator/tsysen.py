import sys
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Fijar semilla para la detección de idiomas (opcional)
DetectorFactory.seed = 0

# Diccionario de idiomas con códigos y nombres
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

def main(texto):
    try:
        # Detectar el idioma del texto de entrada
        idioma_detectado = detect(texto)
        nombre_idioma_detectado = idiomas.get(idioma_detectado, "Unknown")

        print(f"Idioma detectado: {nombre_idioma_detectado} ({idioma_detectado})")

        # Traducir el texto solo al inglés
        if idioma_detectado != "en":  # Solo traducir si no es inglés
            traduccion = GoogleTranslator(source=idioma_detectado, target='en').translate(texto)
            print(f"Traducción a Inglés: {traduccion}")
        else:
            print("El texto ya está en inglés. No se necesita traducción.")

    except LangDetectException:
        print("No se pudo detectar el idioma del texto.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, introduce el texto que deseas traducir como argumento.")
    else:
        # Unir todos los argumentos de la línea de comandos en un solo texto
        texto = " ".join(sys.argv[1:])
        main(texto)
