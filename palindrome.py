cases = int(input())

for cases in range(cases):
    world = input()
    if world == world[::-1]:
        print("YES")
    else:
        print("NO")
        
