t  = int(input())

for _ in range (t):
    slides = int(input())
    base = 0
    max_height = 0
    for _ in range(slides):
        dimensions = [int(x) for x in input().split()]
        base += min(dimensions)
        _max = max(dimensions)
        if _max > max_height:
            max_height = _max
    final_base = base + base
    final_height = max_height + max_height
    print(final_base + final_height)
        
    