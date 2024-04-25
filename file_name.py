extension_world = int(input())
world = input()

i = 0
count_xs = 0

while i <= len(world)-3:
    if world[i:i +3]  == 'xxx':
        count_xs += 1
        world = world[:i] + world[i+1:]
    else:
        i+=1
        
        
print(count_xs)
        
        
        

    