import sys

# 입력은 쿠폰수 n, 도장수 k.
n, k = map(int, input().split(' '))

# 제한 범위 설정
if k > n :
    sys.exit(0)
elif n > 1000000000 :
    sys.exit(0)
    
# 치킨 한마리에 도장 1개. 도장 k개 모으면 쿠폰 한장
# 쿠폰 한장당 치킨 한마리.
# n=4, k=3 : 쿠폰 4장, 도장 3개가 모이면 쿠폰 한장.
    # 4마리 먹고 도장4개 -> 도장3개는 쿠폰, 남은 도장 1개.
    # 4마리 먹고 쿠폰 1개 추가로 생겼으니 5마리 먹음.
# n=10, k=3 : 쿠폰 10장, 도장 3개가 모이면 쿠폰한장.
    # 10마리 먹고 도장 10개 -> 도장 9개는 쿠폰 3장, 남은도장 1개
    # 3마리 먹고 도장 3개 -> 남은도장 1개 + 먹고 받은 도장 3개 = 도장 총 4개 -> 도장 1개 쿠폰, 남은도장 1개
    # 1마리 먹고 도장 1개 -> 남은도장 1개 + 먹고 받은 도장 1개 = 도장 총 2개
    
"""
반복문
n이 그대로 stamp가 되고, stamp에서 지정된 k만큼 n이 1 증가, stamp-k.
stamp가 지정된 k만큼 안되면 종료. 
"""
# 초기에 n만큼의 치킨을 먹고 n만큼의 도장을 얻음.
stamp = n
toEat = n
i = 0
# while not(stamp < k)
while True :
    #toEat = n 
    #stamp = n
    print('[%d번째 루프]' % i)
    print('처음 소지한 도장개수 == 먹은 수 : %d' % stamp)
    
    n = 0 # 쿠폰을 써서 먹었으니 쿠폰은 0개.
    # stamp가 k개 이상 쌓이면 k당 쿠폰 n이 1 증가.
    """
    if stamp >= k :
        n = stamp-k
        print('도장을 교환한 후 쿠폰의 개수 : %d' % n)
    """
    #while stamp >= k :
    while stamp >= k :
        print('\nwhile문 돌아요')
        print('쿠폰수 : %d' % n)
        print('도장수 : %d' % stamp)
        #print('먹은횟수 : %d' % toEat)
        stamp -= k
        # n이 아니라 stamp가 늘어나는 거지.....
        #n += 1
        stamp += 1
        toEat += 1
        print('%d개 쿠폰으로 교환하고 남은 도장 수 : %d' % (k, stamp))
        print('교환하고 먹은횟수 : %d' % toEat)
        #toEat += int(stamp/k)        
        
    #print('도장 %d개만큼을 모두 교환한 후 쿠폰의 개수 : %d' % (k, n))
    # 교환한 stamp는 k개 만큼 감소.
    #stamp -= k
    
    print('\n쿠폰으로 교환한 후 도장개수 : %d' % stamp)
    
    #toEat += 1
    print('총 치킨 먹은 횟수 : %d' % toEat)
    print('남은 쿠폰 개수 : %d' % n)
    #print('\n')
    i += 1

    if stamp == k :
        print('stamp == k 에서 걸림')
        stamp = 0
        n += 1
        toEat += 1
        break
    
    elif stamp < k:
        print('stamp < k 에서 걸림')
        break

print(toEat)