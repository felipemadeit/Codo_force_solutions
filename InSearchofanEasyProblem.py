n = int(input())

results = [int(x) for x in input().split()]

state = 'EASY'

for i in results:
    if i != 0 and i != ' ':
        state = 'HARD'
print(state)