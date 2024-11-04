# morse.py
MORSE_CODE_DICT = {
    # Letters
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    # Numbers
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    # Punctuation
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-'
}

def encode_morse(message):
    """Encodes a message into Morse code."""
    morse_code = []
    for letter in message.upper():
        if letter in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[letter])
        else:
            morse_code.append(' ')  # For spaces or unsupported characters

    return ' '.join(morse_code)

def decode_morse(morse_code):
    """Decodes a Morse code message into plain text."""
    morse_code += ' '  # Add a space to separate the last character
    message = ''
    morse_char = ''
    for char in morse_code:
        if char != ' ':
            morse_char += char
        else:
            message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_char)]
            morse_char = ''
    return message

if __name__ == '__main__':
    message = input("Enter a message: ")
    encoded_message = encode_morse(message)
    print("Encoded message:", encoded_message)

    morse_code = input("Enter Morse code: ")
    decoded_message = decode_morse(morse_code)
    print("Decoded message:", decoded_message)