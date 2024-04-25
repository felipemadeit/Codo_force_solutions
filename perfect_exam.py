n,m = [int(x) for x in input().split()]

total = 0

answers_all = []
for _ in range(n):
    answers_all.append(input())
points = [int(x) for x in input().split()]
    
for letters in range(m):
    ocurrences = {}
    max_ocurrences = 0
    for person in range(n):
        letter = answers_all[person][letters]
        if answers_all[person][letters] in ocurrences:
            ocurrences[letter] += 1
        else:
            ocurrences[letter] = 1
        if ocurrences[letter] > max_ocurrences:
            max_ocurrences = ocurrences[letter]
    total += max_ocurrences*points[letters]


print(total)
    
        
        



    
    



    
    