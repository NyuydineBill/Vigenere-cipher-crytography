# Vigenere Cipher Encryption

This Python script demonstrates how to encrypt a plaintext using the Vigenere cipher technique. The Vigenere cipher is a method of encrypting alphabetic text by using a keyword and rearranging the letters based on a keyword.

## Usage

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Clone or download the repository to your local machine.
4. Navigate to the directory containing the `main.py` file.
5. Open the file in a text editor and modify the `text` and `keyword` variables to suit your requirements.
6. Run the script using the following command:

    ```
    python main.py
    ```

7. The encrypted text will be displayed in the terminal.

## Example

Suppose we want to encrypt the following text using the keyword "unconstitutionality":



After running the script, the output will be the encrypted text.

## How It Works

The script takes the plaintext and a keyword as input. It then iterates through each character in the plaintext. For each alphabetic character, it shifts the character based on the corresponding letter in the keyword. Non-alphabetic characters remain unchanged. Finally, it returns the encrypted text.

## Credits

This script was written by [Nyuydine Bill].

## License

This project is licensed under the [MIT License](LICENSE).