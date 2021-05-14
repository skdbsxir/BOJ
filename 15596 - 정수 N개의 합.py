import sys

def solve(a=[]) :
    for i in range(len(a)) :
        if a[i] > 1000000 :
            sys.exit(0)
        elif a[i] < 0 :
            sys.exit(0)
        
    total = sum(a)
    return total    