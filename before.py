s = input()

vocabulary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
final_string = ''

for letters in s:
    if s.islower():
        lower_vocabulary = vocabulary.lower()
        index = lower_vocabulary.find(s)
        final_string += lower_vocabulary[: index+1]
    else:
        index = vocabulary.find(s)
        final_string += vocabulary[: index +1]
print(final_string)
    
    

    


       