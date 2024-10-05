from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Fijar semilla para la detección de idiomas (opcional)
DetectorFactory.seed = 0

# Lista de códigos de idiomas
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

# Texto en español para traducir
texto = input("Enter the text you want to translate: ")


# # Traducir y mostrar resultados
# for idioma in idiomas:
#     traduccion = GoogleTranslator(source='es', target=idioma).translate(texto)
#     print(f"Traducción a {idioma}: {traduccion}")

try:
    # Detectar el idioma del texto de entrada
    # idioma_detectado = detect(texto)
    idioma_detectado = 'es'
    nombre_idioma_detectado = idiomas.get(idioma_detectado, "Unknown")

    print(f"Language detected: {nombre_idioma_detectado} ({idioma_detectado})")
    
    traduccion = GoogleTranslator(source=idioma_detectado, target='en').translate(texto)
    print(f"Translation to: {traduccion}")

    # Traducir el texto a todos los idiomas en el diccionario
    # for codigo, nombre in idiomas.items():
    #     traduccion = GoogleTranslator(source=idioma_detectado, target=codigo).translate(texto)
    #     print(f"Traducción a {nombre} ({codigo}): {traduccion}")

except LangDetectException:
    print("No se pudo detectar el idioma del texto.")
except Exception as e:
    print(f"Ocurrió un error: {e}")