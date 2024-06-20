morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '  # Longer time intervals will be represented as 3 spaces
}


def text2morse(text: str):
    text = text.upper()

    morse_code = []
    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            # Handle characters that are not in the dictionary with 8 dits
            morse_code.append('........')

    return ' '.join(morse_code)
