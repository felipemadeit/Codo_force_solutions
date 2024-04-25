cases = int(input())
dict_letters = {}


for cases in range(cases):
    string = ''
    len_world = int(input())
    world = input()
    for index, letters in enumerate(world) :
        dict_letters[letters] = index%2
    for letters in world:
        string += str(dict_letters[letters])
    for l in range(len(string)-1):
        if string[l] == string[l+1]:
            print("NO")
        else:
            print("YES")
        
        
        
    


    



    

    
        