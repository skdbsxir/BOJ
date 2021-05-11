import sys

# 계속 입력받기
for i in sys.stdin.readlines() :
    n, k = map(int, i.split(' '))
    
    toEat = n # 먹을 수 있는 횟수   
    while n >= k :
        stamp = int(n/k) # 도장을 먼저 받고
        
        if stamp > 0 :
            toEat += int(n/k) # 먹고 난 후
            n = stamp + (n % k) # 전부 쿠폰으로 바꾼다.
        else :
            break
        
    print(toEat)