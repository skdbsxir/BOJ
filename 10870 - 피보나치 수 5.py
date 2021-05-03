import sys

n = int(input())

if n < 0 :
    sys.exit(0)
elif n > 20 :
    sys.exit(0)
    
def fibonacci(x) :
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(n))

# 너무 쉽다..
# 실3 피보나치 함수가 여기서 뇌를 좀 더 굴려야되는 문제이긴 한듯 확실히. 