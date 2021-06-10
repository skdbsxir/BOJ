"""
스크린은 N칸으로 나눠짐.
스크린 아래쪽에는 M칸을 차지하는 바구니. (M < N)
(N은 10 이하. M은 N 미만.)
NNNNN (N=5)
M     (M=1)

사과는 N칸중 한칸의 상단에서 바닥까지 직선으로 떨어짐.
바닥에 떨어지면 다른 사과가 떨어짐.

바구니가 사과가 떨어지는 칸을 차지하고 있으면 사과를 담을 수 있음.
사과를 모두 담으려 함. 바구니 이동거리의 최솟값?

입력 : 첫줄엔 N, M. 둘째줄엔 떨어지는 사과 수 J. 다음 J개 줄에는 떨어지는 위치.
출력 : 모든 사과를 담기위해 이동해야하는 거리의 최솟값.

ex) 
5 1
3
1
5
3

6
"""
N, M = map(int, input().split())
J = int(input())
apple = []
for i in range(J):
    apple.append(int(input()))

"""
# N만큼의 공 리스트 생성
# M만큼의 공 리스트 생성
NList = [0 for i in range(N)]
MList = [0 for i in range(M)]

# print(NList)
# print(MList)

# apple에 있는 수랑 일치하는 NList의 index위치 내용을 채우자.
# 순서대로?
#for i in range(len(apple)) :
#    NList[apple[i]-1] = apple[i]    
# print(NList)

# 한번에 바구니를 움직일 수 있는 정도는 M만큼.
# print(N % M)
# N = 5에 대해
# 나머지가 0 : 한번에 1개밖에 못담음. 한번에 1칸.
# 나머지가 1 : 한번에 짝수개 밖에 못담음. 한번에 짝수칸.??
# 나머지가 2 : 한번에 홀수개 밖에 못담음. 한번에 홀수칸.??

# 으아아아아아아아아악 씨ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ
"""
# 바구니는 맨 처음 가장 왼쪽 M만큼의 칸을 차지함.
 # 바구니의 왼쪽위치, 오른쪽 위치를 지정.
 # 오른쪽 위치 = 바구니 크기
# 사과 위치를 입력받을때마다 
 # 왼쪽 위치, 오른쪽 위치 사이로 : 이동X.
 # 왼쪽 위치보다 왼쪽으로 : 왼쪽위치 - 사과위치 한 값을 더함.
 # 오른쪽 위치보다 오른쪽으로 : 사과위치 - 오른쪽 위치 한 값을 더함.
count = 0
left = 1
right = M

print('--------------------------------------------------')
for i in range(len(apple)) :
    # 왼쪽 위치, 오른쪽 위치 사이로 떨어지면 이동 X
    if (left <= apple[i]) and (right >= apple[i]) :
        print('사과는 %d번째에 있으니 바구니 가만히 있을게요.' % apple[i])
        pass
    # 왼쪽 위치보다 왼쪽으로 떨어진 경우
    if left > apple[i] :
        # 바구니를 왼쪽으로 움직임.
        print('바구니 왼쪽갈게요. 사과는 %d 번째 위치에 있어요' % apple[i])
        movement = abs(apple[i] - left)
        print('%d 칸 만큼 왼쪽으로 움직일게요' % movement)
        # count는 움직인 횟수.
        count += movement
        # 바구니 위치는 바뀜. 왼쪽으로 움직이니 -되는 것.
        left -= movement
        right -= movement
    # 오른쪽 위치보다 오른쪽으로 떨어진 경우
    if right < apple[i] :
        # 바구니를 오른쪽으로 움직임.
        print('바구니 오른쪽갈게요. 사과는 %d 번째 위치에 있어요' % apple[i])
        movement = abs(apple[i] - right)
        print('%d 칸 만큼 오른쪽으로 움직일게요' % movement)
        # count는 움직인 횟수.
        count += movement
        # 바구니 위치는 바뀜. 오른쪽으로 움직이니 +되는 것.
        left += movement
        right += movement
    print('--------------------------------------------------')

# 최종 결과
print(count)
        
# 바구니가 한칸씩밖에 이동 못한다는 소리가 어딨지...
# 바구니는 스크린의 경계를 넘어가면 안 된다. 이게 그소린가?