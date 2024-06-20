# Text to Morse Code Converter

This project provides a simple Python program that converts text input into Morse code. It includes a dictionary for Morse code translation and handles edge cases such as characters not found in the Morse code dictionary.

## Project Structure

- **converter.py**: Contains the Morse code dictionary and the `text2morse` function which performs the conversion.
- **main.py**: Provides a command-line interface for users to input text and see the converted Morse code output.

## Files

- **converter.py**
- **main.py**

### converter.py

This file contains the Morse code dictionary and the `text2morse` function. The dictionary maps each alphanumeric character and space to its corresponding Morse code representation. The text2morse function converts a given text string to Morse code.

### main.py

This file provides a command-line interface for the Morse code converter. It prompts the user to input a phrase and then prints the Morse code translation.

## How to Run

Ensure you have Python installed on your system.

Download the converter.py and main.py files to the same directory.

Open a terminal or command prompt.

Navigate to the directory containing the files.

Run the following command:

```sh
python main.py
```
Follow the on-screen instructions to enter a phrase and see its Morse code translation.

### Example
```vbnet
$ python main.py
Welcome to Text to Morse Translator!
Enter the phrase you would like translated:
Hello World
Your phrase in the Morse code:
.... . .-.. .-.. ---   .-- --- .-. .-.. -..
```
## License
This project is licensed under the MIT License.
