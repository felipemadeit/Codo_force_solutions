def max_table (n: int):
    matrix_base = [1]*n
    final = []
    count = 0
    for lines in range(n-1):
        for i in range(1,n+1):
            final.append(sum(matrix_base[:i]))
        matrix_base = []
        matrix_base = final[count:]
        count += n
    return matrix_base[-1]
print(max_table(int(input())))







