def vigenere_cipher(text, keyword):
    """
    Encrypts the given text using the Vigenere cipher.

    Args:
        text (str): The plaintext to be encrypted.
        keyword (str): The keyword used for encryption.

    Returns:
        str: The encrypted ciphertext.
    """
    encrypted_text = ""
    keyword_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            keyword_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def affine_cipher(text, a, b):
    """
    Encrypts the given text using the Affine cipher.

    Args:
        text (str): The plaintext to be encrypted.
        a (int): The first encryption key.
        b (int): The second encryption key.

    Returns:
        str: The encrypted ciphertext.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr(((ord(char) - ord('A')) * a + b) % 26 + ord('A'))
            else:
                encrypted_text += chr(((ord(char) - ord('a')) * a + b) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

def main():
    """
    Main function to select encryption mode and perform encryption.
    """
    mode = input("Select encryption mode (Vigenere/Affine): ").lower()
    text = input("Enter the plaintext: ")

    if mode == "vigenere":
        keyword = input("Enter the keyword: ").lower()  # Convert keyword to lowercase
        cipher_text = vigenere_cipher(text, keyword)
    elif mode == "affine":
        a = int(input("Enter value for 'a' in Affine cipher: "))
        b = int(input("Enter value for 'b' in Affine cipher: "))
        cipher_text = affine_cipher(text, a, b)
    else:
        print("Invalid encryption mode.")
        return
    
    print("Cipher Text:")
    print(cipher_text)

if __name__ == "__main__":
    main()
