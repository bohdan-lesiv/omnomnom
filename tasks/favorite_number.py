"""
This script is used to get the word of a number from a user.

Author: Will Savage
Date 1/31/2022
"""

from num2words import num2words


def favorite_number():
    """
    Greets a user and asks for favorite number.

    Prints the number.
    """
    number = input("Hello, whats your favorite number?: ")
    print(num2words(number))


if __name__ == "__main__":
    favorite_number()