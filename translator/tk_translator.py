import tkinter as tk
from tkinter import scrolledtext, messagebox
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

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

# Función para detectar y traducir el texto
def detect_and_translate(text, output_box):
    if not text.strip():
        messagebox.showerror("Error", "The text provided is empty.")
        return

    try:
        # Detectar el idioma del texto de entrada
        language = detect(text)
        language_name = idiomas.get(language, "Unknown")

        if language_name == "Unknown":
            messagebox.showwarning("Warning", "The language could not be detected. Defaulting to Spanish.")
            language = "es"
            language_name = "Spanish"

        output_box.insert(tk.END, f"Language detected: {language_name} ({language})\n")

        # Traducir a todos los idiomas excepto el idioma detectado
        for codigo, nombre in idiomas.items():
            if codigo != language:
                traduccion = GoogleTranslator(source=language, target=codigo).translate(text)
                output_box.insert(tk.END, f"Translation to {nombre} ({codigo}): {traduccion}\n")

    except LangDetectException:
        messagebox.showerror("Error", "The language of the text could not be detected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Función para manejar el botón de traducción
def on_translate_click(input_box, output_box):
    text = input_box.get("1.0", tk.END)  # Obtener todo el texto del cuadro de entrada
    output_box.delete("1.0", tk.END)  # Limpiar el cuadro de salida antes de mostrar nuevas traducciones
    detect_and_translate(text, output_box)

# Crear la interfaz gráfica
def create_gui():
    window = tk.Tk()
    window.title("Language Detector and Translator")
    window.geometry("600x600")

    # Etiqueta de entrada
    lbl_input = tk.Label(window, text="Enter the text to translate:")
    lbl_input.pack(pady=10)

    # Cuadro de texto para ingresar el texto
    input_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=10)
    input_box.pack(padx=10, pady=10)

    # Botón para traducir
    btn_translate = tk.Button(window, text="Detect and Translate", command=lambda: on_translate_click(input_box, output_box))
    btn_translate.pack(pady=10)

    # Cuadro de texto para mostrar las traducciones
    output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
    output_box.pack(padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
