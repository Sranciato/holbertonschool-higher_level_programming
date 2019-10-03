#!/usr/bin/python3
"""Add newlines on specific characters

args: text

"""


def text_indentation(text):
    """
    Seperate text by characters . ? and :
    """

    char = 0

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    while (char < len(text)):
        print("{}".format(text[char]), end='')
        if text[char] == "." or text[char] == "?" or text[char] == ":":
            print("\n")
            if char == len(text) - 1:
                break
            if text[char + 1] == " ":
                char += 1
        char += 1
