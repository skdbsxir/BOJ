import sys

N = int(input())
mySit = list(map(int, input().split()))

# 손님 수와 손님이 앉고싶어하는 자리 수가 다르면 exit.
if not len(mySit) == N :
    sys.exit(0)
    
"""
- 순서대로 입력, 중복이 생기면 거절카운트 +1?
- 리스트 안에서 반복 --> 중복 확인 --> 중복이 있다면 거절 카운트 +1
- 전체 리스트에서 i번째랑 중복되는 것이 있는지 확인
 > 리스트를 정렬, 그 안에서 중복 찾기?
 > 딕셔너리를 또 써보자.
 > 결과 딕셔너리에서, 결과값이 2 이상인 것들이 거절당하는 좌석. 거절당하는 수는 이에 -1을 한 것.
"""
refCount = 0

"""
for i in range(len(mySit)) :
    # print('%d번째와 리스트 요소 중 %d번째 요소인 %d을 확인' % (i, i, mySit[i]))
    if i == mySit[i] :
        refCount += 1

# print(refCount)
"""
"""
for i in range(len(mySit)) :
    for j in range(len(mySit)) :
        print('%d번째와 리스트 요소 중 %d번째 요소인 %d을 확인' % (i, j, mySit[i]))
        if mySit[i] == mySit[j] :
            refCount += 1
 
# print(refCount)
"""
# 리스트 요소별 갯수 count, 딕셔너리에 저장.
counter = {}
for i in mySit :
    try:
        counter[i] += 1
    except : counter[i] = 1  
# print(counter)

# 딕셔너리의 (key, value)에서 value가 2 이상인 요소는 중복된 자리. 즉 거절되는 좌석.
# 좌석을 부른 횟수 == value 이므로, 거절 카운트엔 value-1 만큼 더함.
for i, (key, value) in enumerate(counter.items()) :
    # print(i, key, value)
    if value >= 2 :
        refCount += (value - 1)
        
print(refCount)