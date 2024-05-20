def define_fair (t:int):
    """Return if the tournament is fair
    

    Args:
        t (int): Number of cases
    """

    for _ in range(t):

        skills  = [int(x) for x in input().split()]
        
        first_winner = max(skills[:2])
        second_winner = max(skills [2:])
        skills.remove(first_winner)
        skills.remove(second_winner)

        max_not = max(skills)


        if max_not > first_winner or max_not > second_winner:
            print("NO")
        else:
            print("YES")
        

        
        

        

define_fair(int(input()))
