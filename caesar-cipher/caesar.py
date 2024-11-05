def caesar_cipher(text, shift):
    """Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text (str): The message to be encrypted or decrypted.
        shift (int): The number of positions to shift the letters.

    Returns:
        str: The encrypted or decrypted message.
    """

    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted_char.upper() if is_upper else shifted_char
        else:
            result += char
    return result

# Example usage:
text = "HELLO, WORLD!"
shift = 3

encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text:", decrypted_text)