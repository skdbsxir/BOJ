import sys
"""
# 접근 1 (쓸모없는 연산을 한다는 단점.)
 ## str 리스트로 입력을 받고
 ## 새 리스트를 생성한 다음 str 리스트 각 원소를
 ## int형으로 바꾼 다음 새 리스트에 추가.

N = int(input())
myList = list(input())

if len(myList) != N:
    sys.exit(0)

print(myList)
#print(type(myList[0])) # 입력받은건 str type의 숫자.

newList = []
for i in range(len(myList)) :
    newList.append(int(myList[i]))
    
print(newList)
ans = sum(newList)
print(ans)
"""
# 접근 2 
 ## map 함수 이용, 처음부터 int 형으로 입력 받기.
N = int(input())
myList = list(map(int, input()))

if len(myList) != N:
    sys.exit(0)

#print(myList)

print(sum(myList))
    