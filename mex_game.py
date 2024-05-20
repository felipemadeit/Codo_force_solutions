from collections import OrderedDict

def get_data (t: int):
    """ This function get the problem data

    Args:
        t (int): Test
    """
    
    for _ in range(t):
        n = int(input())
        nums = [int(x) for x in input().split()]

       
def get_contadores (nums:list):

    count = OrderedDict()

    for i in nums:
        if i in nums:
            count[i] +=1
        else:
            count[i] = 1
    return count

