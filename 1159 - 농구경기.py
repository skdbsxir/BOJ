"""
성의 첫 글자가 같은 선수 5명을 선발. 
첫 글자가 같은 선수가 5명보다 적으면 기권.

(input)
N : 선수의 수
N개의 줄엔 선수의 성이 주어짐. (only 알파벳 소문자)

(output)
선발이 가능한 경우 그 선수들 성의 첫글자를 합쳐서 출력
선발이 불가능한 경우 PREDAJA 출력.
"""
N = int(input())
myList = []
for i in range(N) :
    # 입력하는 string의 첫글자만 따오면 편할 듯?
    myList.append(input()[0])
    
# 입력받은걸 아예 정렬.
playerList = sorted(myList)
del myList

tempList = []
for i in playerList :
    # 5개 이상있고 temp에 없으면 temp에 추가.
    if playerList.count(i) >= 5 and i not in tempList:
        tempList.append(i)

del playerList

# temp가 비어있으면 선수X. 항복
# temp 차있으면 내용 출력.
if len(tempList) != 0:
    for i in tempList:
        print(i, end='')
else :
    print('PREDAJA')