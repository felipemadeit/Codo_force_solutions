n = int(input())

for _ in range(n):
    _len = int(input())
    numbers = [int(x) for x in input().split()]
    moves = 0
    i = 0
    j = len(numbers)-1
    while (i < j):
        if numbers[i] == 1 and numbers[j] == 0:
            moves += 1
            i += 1
            j -= 1
        elif numbers[i] == 0:
            i += 1
        else:
            j -= 1
    print(moves)

    
        