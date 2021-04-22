import sys

N = int(input())

if N > 12 :
    sys.exit(0)
elif N < 0 :
    sys.exit(0)
    
def factorial(N) :
    if (N==1 or N==0):
        N = 1
    elif (N >= 2):
        N = N * factorial(N-1)
    return N

print(factorial(N))
