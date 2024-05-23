def word (word: str):

    upper_letters = 0
    lower_letters = 0

    for i in word:
        if i.isupper():
            upper_letters += 1
        else:
            lower_letters += 1
    

    if upper_letters > lower_letters:
        print(word.upper())
    elif upper_letters < lower_letters:
        print(word.lower())
    else:
        print(word.lower())

word(input())