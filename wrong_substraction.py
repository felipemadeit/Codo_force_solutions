def wrong_substraction ():

    n, k = [int(x) for x in input().split()]

    for i in range(k):
        if str(n)[-1] == '0':
            n = n//10
        else:
            n = n-1
    
    print(n)

wrong_substraction()