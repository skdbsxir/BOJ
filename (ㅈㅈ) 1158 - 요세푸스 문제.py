"""
1번부터 N번까지 원을 이루며 앉아있다
given K (N 이하)

K번째 사람을 제거
한 사람이 제거되면 남은 사람들이 원을 만들어 다시 앉음
거기서 다시 K번째 사람 제거... 반복

이 과정은 N명의 사람이 모두 제거될때 까지 계속.

원에서 사람들이 제거되는 순서를 (N,K)요세푸스 순열이라 함.

(7,3)요세푸스 순열은 <3,6,2,7,5,1,4> 이다.
"""
# N, K = map(int, input().split())
# myList = []
# for i in range(N):
    # myList.append(i+1)

"""
K번째 사람이 제거 --> 그 뒤에 있는 사람부터 해서 원으로 앉음
그러니까 3 다음에 6이 나오지 ㅅㅂ
1234567
3 / 456712
36 / 71245
362 / 4571
3627 / 145
36275 / 14
이떄 k가 len(list) 이므로 list가 그대로 순열뒤로 감.
따라서 답은 3627514
"""
# josephList = []
"""
josephList.append(myList.pop(K-1))

print(josephList)
print(myList)
# myList를 다시 어떻게 정리할까
# 0 1 2 3 4 5 6 에서 2가 빠짐
# 0 1 2 3 4 5 순서에서 2 3 4 5 0 1 이렇게 넣고싶어요
# 2 3 4 5 넣고 난 뒤에 0 1 넣고? 
myList = myList[K-1:] + myList[:K-1]
# sampList.append(myList[:K-1])
print(myList)

# 다시 저기서 3번째꺼 넣고 이런식으로 반복?
josephList.append(myList.pop(K-1))
myList = myList[K-1:] + myList[:K-1]
print(josephList)
print(myList)
"""
"""
for i in range(len(myList)):
    # 만약 myList 길이가 K보다 작아지면
    print('현재 리스트 생김새는 : ', myList)
    if len(myList) < K:
        # myList 내용을 전부 josephList에 넣고
        print('리스트가 K보다 작아졌어요.')
        for j in range(len(myList)):
            josephList.append(myList[j])
        # for loop 종료.
        break
    else:
        print('\n')
        print('%d번째 있는거 뺄깨요. 내용물은 %d에요.' % (K, myList[K-1]))
        josephList.append(myList.pop(K-1))
        myList = myList[K-1:] + myList[:K-1]
    
    
print('<' + ', '.join(map(str, josephList))+'>')
# print('<' + ', '.join(str(i) for i in josephList)+'>', sep='')
"""
"""
# 원리 1.
    # K-1 번째 index만 참조, 그 위치의 원소만 pop
    # 원본 list가 index 숫자보다 작아지는 경우
    # 해당위치 index에서 list 끝까지 전진,
    # 다시 list 앞으로 와서 남은 index 수 만큼 전진, 해당 위치 원소 pop
    # 반복.
index = K-1
for i in range(len(myList)):
    print('\n')
    print('현재 리스트 생김새는 : ', myList)
    if index >= len(myList):
        print('인덱스가 list보다 커졌어요. index 바꿀게요')
        index %= len(myList)
        print('바뀐 인덱스는 : ', index)
    josephList.append(myList.pop(index))
    print('요세푸스 리스트는 헌재 : ', josephList)
    index += (K-1)
    print('요세푸스 리스트에 넣고 현재 인덱스는 : ', index)
print(josephList)
"""
# 원리 2.
    # collections.deque 이용.
from collections import deque

N, K = map(int, input().split())
myDeque = deque()
for i in range(N):
    myDeque.append(i+1)
    
josephList = []

# Deque가 빌 때 까지 Loop
while myDeque:
    print('\n')
    # K-1 만큼 왼쪽으로 회전시키고
    myDeque.rotate(-(K-1)) 
    print('회전 후 Deque 상태 : ', myDeque)
    
    # Deque의 맨 앞을 josephList에 append 하고 제거.
    josephList.append(myDeque[0])
    print('josephList 내용물 : ', josephList)
    myDeque.popleft()
    print('빼고 난 후 Deque 상태 : ', myDeque)

print('<' + ', '.join(map(str, josephList))+'>')

# 내 패배다. 실5라서 쉬운줄 알았더니 ㅈㄴ어렵네 문제... 너무 헤메었다.