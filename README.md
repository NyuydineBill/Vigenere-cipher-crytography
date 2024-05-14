# Vigenere and Affine Cipher Encryption

This Python script demonstrates how to encrypt a plaintext using the Vigenere or Affine cipher techniques. Both ciphers are methods of encrypting alphabetic text, each with its own approach.

## Usage

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Clone or download the repository to your local machine.
4. Navigate to the directory containing the `main.py` file.
5. Run the script using the following command:

    ```
    python main.py
    ```

6. Follow the prompts to select the encryption mode (Vigenere or Affine) and enter the plaintext and keyword or key values when prompted.
7. The encrypted text will be displayed in the terminal.

## How It Works

### Vigenere Cipher
The Vigenere cipher encrypts letters of the plaintext by shifting them based on a keyword. The encryption formula is:

\[ E(x) = (x + k) \mod 26 \]

Where:
- \( E(x) \) is the encrypted letter,
- \( x \) is the numerical value of the plaintext letter,
- \( k \) is the numerical value of the corresponding letter in the keyword, and
- \( \mod 26 \) ensures the result wraps around within the range of the alphabet.

Non-alphabetic characters remain unchanged.

### Affine Cipher
The Affine cipher encrypts letters of the plaintext using a mathematical function of the form \( E(x) = (ax + b) \mod m \), where:
- \( E(x) \) is the encrypted letter,
- \( x \) represents the numerical value of a letter in the alphabet,
- \( a \) and \( b \) are integers that serve as the encryption keys, and
- \( m \) is the size of the alphabet.

Non-alphabetic characters remain unchanged.

## Example

Suppose we want to encrypt the following text:
`Cryptography originally deals with the problem of encrypting messages so that nobody but the authorised person can decrypt and read it. It has been used throughout the last`


After running the script and selecting the encryption mode (Vigenere or Affine) and entering the appropriate keyword or key values, the output will be the encrypted text.

## Credits

This script was written by [Nyuydine Bill](https://nyuydine.netlify.app/).

## License

This project is licensed under the [MIT License](LICENSE).
