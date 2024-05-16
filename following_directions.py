def movements (n: int):
    for i in range(n):
        base = [0,0]
        _len= int(input())
        s = input()
        check = False
        for j in s:
            if j == 'U':
                base[1] +=1
                if base[0] == 1 and base[1] == 1:
                    check = True
                    break
            elif j == 'D':
                base[1] -= 1 
                if base[0]== 1 and base[1] == 1:
                    check = True
                    break            
            elif j == 'L':
                base[0] -= 1 
                if base[0] == 1 and base[1] == 1:
                    check = True
                    break              
            else:
                base[0] +=1
                if base[0] == 1 and base[1] == 1:
                    check = True
                    break
        if check:
            print("YES")
        else:
            print("NO")

movements(int(input()))
            
