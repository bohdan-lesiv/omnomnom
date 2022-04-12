from num2words import num2words


def hello():
    """
    This module greet a user
    :return: greeting
    """
    print("Hello, friend!")


def numbers_translator():
    """
    This module translate the number into words representation
    :return: translation of number into words
    """
    while True:
        number = input("Please enter your number: ")
        if number.isdigit():
            translation = num2words(number)
            print(translation)
            pass
        else:
            print("Sorry, I can translate just numbers")
            continue
        return translation


if __name__ == "__main__":
    hello()
    numbers_translator()
