from converter import text2morse


if __name__=="__main__":
    print("Welcome to Text to Morse Translator!")
    phrase = input("Enter the phrase you would like translated:\n")
    print(f"Your phrase in the Morse code\n{text2morse(phrase)}")