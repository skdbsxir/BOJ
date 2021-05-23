"""
앞에서 읽은거랑 뒤에서 읽은게 같으면 팰린드롬수.

입력은 여러개의 테스트케이스.
팰린드롬수 이면 yes, 아니면 no.
0이 입력되면 종료.
"""
"""
# 문자열 리스트를 입력받고
# 리스트와 이를 거꾸로한 리스트를 비교?
myList = list(input())

reverseList = list(reversed(myList))

#print(myList)
#print(reverseList)

if myList == reverseList :
    print('yes')
else:
    print('no')
"""
# 제출용으로 수정.
while True :
    myList = list(input())
    
    if myList[0] == '0':
        break
    
    reverseList = list(reversed(myList))
    
    if myList == reverseList :
        print('yes')
    else :
        print('no')