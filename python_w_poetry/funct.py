
def first_word(text: str) -> str:
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
