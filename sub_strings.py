cases = int(input())

for cases in range(cases):
    world = input()
    new_world = ''
    for index in range(0, len(world), 2):
        new_world += world[index]
    new_world+= world[len(world)-1]
    print(new_world)
        
        