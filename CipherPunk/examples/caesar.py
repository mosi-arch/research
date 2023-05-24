def caesar_cipher(text, shift):
    """Encrypts the given text using the Caesar Cipher technique."""
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the character by the given number of positions
            shifted = chr((ord(char) - 65 + shift) % 26 + 65)
            result += shifted
        else:
            result += char
    return result

# =========================

message = "HELLO WORLD"
shift = int(input("Enter the number of positions to shift the letters by: "))
encrypted_message = caesar_cipher(message, shift)
print("Encrypted message:", encrypted_message)