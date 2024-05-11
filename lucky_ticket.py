def is_lucky (t:int):
    """If the sum of the first three digits is equal to the las three digits is lucky ticket

    Args:
        t (int): Number of cases
        ticket (str): The number of the ticket
    """
    
    for i in range(t):
        ticket = input()
        if (sum(int(digito) for digito in str(ticket[:3]))) == (sum(int(digito) for digito in str(ticket[-3:]))):
            print("YES")
        else: 
            print("NO")
        
            
        
is_lucky(int(input()))