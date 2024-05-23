def beatiful_matrix ():
    matrix = []

    for i in range(5):
        line = [int(x) for x in input().split()]
        matrix.append(line)

    one_position = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                one_position.append(i)
                one_position.append(j)
                

    moves = 0

    for i in one_position:
        moves += abs(2-i)
    
    print(moves)

    # 1-4
    # 2-2
    # 1 + 2

    
    


beatiful_matrix()