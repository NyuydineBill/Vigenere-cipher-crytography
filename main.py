'''
    This task was assigned by the lecturer as an assignmenr 
    for the course "Coding and Cryptographie 
    Engineering" in the University of Bamenda.
    The task was to create a program that can encrypt and
    decrypt a text using the Vigenere cipher.
    The Vigenere cipher is a method of encrypting alphabetic
    text by using a simple form of polyalphabetic substitution.
    A polyalphabetic cipher is any cipher based on substitution,
    using multiple substitution alphabets. The encryption of the
    original text is done using the Vigenère square or Vigenère
    table.
    text = "Cryptography originally deals with the problem of encrypting messages so that nobody but the authorised person can decrypt and read it. It has been used throughout the last"
    keyword = "unconstitutionality"
'''
def vigenere_cipher(text, keyword):
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

def main():
    text = input("Enter the plaintext: ")
    keyword = input("Enter the keyword: ").lower()  # Convert keyword to lowercase
    
    cipher_text = vigenere_cipher(text, keyword)
    print("Cipher Text:")
    print(cipher_text)

if __name__ == "__main__":
    main()
