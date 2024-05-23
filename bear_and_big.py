def bear_big ():

    weights = [int(x) for x in input().split()]

    first_bear = weights[0]
    second_bear = weights[1]
    times = 0

    while first_bear <= second_bear:
        times += 1
        first_bear = first_bear*3
        second_bear = second_bear*2
    
    print(times)

bear_big()