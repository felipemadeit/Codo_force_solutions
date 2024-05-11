t = int(input())

for cases in range(t):
    count = 0
    distances = [int(x) for x in input().split()]
    for i in range(len(distances)):
        if distances[0] < distances[i]:
            count += 1
    print(count)