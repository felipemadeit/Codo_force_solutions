def soldier_bananas():

    k, n, w = [int(x) for x in input().split()]

    total = 0

    for i in range(1,w+1):
        total += i*k
    
    if total > n:
        print(abs(n - total))
    else:
        print(0)

soldier_bananas()




