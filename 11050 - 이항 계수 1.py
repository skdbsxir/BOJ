"""
N, K가 주어졌을때 nCk (편의상 - (n,k) 로 표기.)를 구하는 프로그램
"""
n, k = map(int, input().split())

# (n,k) = n! / (n-k)! * k! ok
# (n,k) = (n,n-k)  ok? 근데 자명하게 나올듯.
# (n,k) = (n-1,k-1) + (n-1,k) ?
# (n,0) = (n,n) = 1 ok
# (n,1) = n ok

def Factorial(x) :
    if x == 1 or x == 0 :
        x = 1
    elif x >= 2 :
        x = x * Factorial(x-1)
    
    return x

def Combination(n, r) :
    if r == n or r == 0 :
        return 1
    if r == 1 :
        return n
    
    return Factorial(n) // (Factorial(n-r) * Factorial(r))

print(Combination(n, k))