"""
숫자는 0~9까지
방 번호가 주어지면 필요한 세트 수
6을 뒤집어서 9, 9를 뒤집어서 6.
"""
# 방 번호
# 리스트로 받는게 나을거같다
number = list(map(int, input()))

# print(number)

# 0~9까지 0으로 초기화 한 list를 미리 만들고
# 그 안에 수를 count해서 넣는다?
myList = [0 for i in range(10)]

# print(myList, len(myList))

# 6, 9 쌍은 1개로 처리 가능.
for i in number:
    # 숫자 6, 9이면 9로 몰기
    if i == 6 or i == 9:
        myList[9] += 1
    # 아닌경우 1개씩 카운트
    else:
        myList[i] += 1
    
# print(myList) 

# 69 갯수가 짝수면 짝수만큼만 필요.
if myList[9] % 2 == 0:
    myList[9] //= 2
# 홀수면 +1개만큼은 더 필요.
else:
    myList[9] = (myList[9]//2) + 1

"""
9696 -> 4에서 2
96969 -> 5에서 3
"""
# print(myList)
# 한 세트엔 0~9까지 있으니까
# list의 최대 수가 필요한 세트 수.
print(max(myList))