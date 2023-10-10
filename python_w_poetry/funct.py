"""
This module contains a function for extracting the first word from a given text.
"""

def first_word(text: str) -> str:
    """
    Extracts the first word from a given text.

    Args:
        text (str): The input text

    Returns:
        str: First word found; if no word is found, an empty string is returned.
    """

    index = 0
    for i, char in enumerate(text):
        if char.isalpha():
            index = i
            break
    word1=""
    for char in text[index:]:
        if(char.isalpha() or char=="'"):
            word1+=char
        else:
            break

    return word1
