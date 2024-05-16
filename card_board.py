def card_board (t: int):
    
    for _ in range(t):

        n,c = [int(x) for x in input().split()]

        cards = [int(x) for x in input().split()]


        limit_inf = 1
        limit_max = 10**18


        while limit_inf <= limit_max:

            mid = limit_inf + (limit_max - limit_inf)// 2

            target = 0

            new_mid = 2*mid
            for i in cards:
               target += (i+new_mid)**2
                
            if target == c:
                print(mid)
                break
            else:
                if target > c:
                    limit_max = mid-1
                else:
                    limit_inf = mid+1



card_board(int(input()))   
            
            
            
        