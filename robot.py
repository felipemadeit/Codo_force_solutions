def get_data ():
    """Collect data for the solution
    """
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        matrix = []
        for _ in range(n):
            matrix.append(input())
        print(solve(matrix, n, m))
        


def solve (matrix, n ,m):
    
    x = m
    y = n
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'R':
                if j < x:
                    x = j
                if i < y:
                    y = i
    if matrix[y][x] == 'R':
        return "YES"
    else:
        return "NO"
                
                    
            
get_data()
    