# Vigenere Cipher Encryption

This Python script demonstrates how to encrypt a plaintext using the Vigenere cipher technique. The Vigenere cipher is a method of encrypting alphabetic text by using a keyword and rearranging the letters based on a keyword.

## Usage

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Clone or download the repository to your local machine.
4. Navigate to the directory containing the `main.py` file.
5. Run the script using the following command:

    ```
    python main.py
    ```

6. Follow the prompts to enter the plaintext and keyword when prompted.
7. The encrypted text will be displayed in the terminal.

## How It Works

The script takes the plaintext and a keyword as input. It then iterates through each character in the plaintext. For each alphabetic character, it shifts the character based on the corresponding letter in the keyword. Non-alphabetic characters remain unchanged. Finally, it returns the encrypted text.

## Example

Suppose we want to encrypt the following text:


After running the script and entering the keyword "unconstitutionality", the output will be the encrypted text.

## Credits

This script was written by [Nyuydine Bill](https://nyuydine.netlify.app/).

## License

This project is licensed under the [MIT License](LICENSE).
