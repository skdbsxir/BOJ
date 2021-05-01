import sys

N = int(input())

# 예외처리
if N > 1000 :
    sys.exit(0)
elif N < 1 :
    sys.exit(0)

# 입력받은 N 만큼의 리스트 생성.
myBox = list(range(N))

# 리스트 원소 1씩 증가. (카드는 1부터 N까지 있으므로.)
for i in range(len(myBox)) :
    myBox[i] += 1

# 카드 역순정렬 후 사용하지 않을 myBox는 삭제.
myBox2 = myBox[::-1]
del myBox

# 결과물 담을 리스트 생성.
resultBox = list()

if len(myBox2) == 1:
    resultBox = myBox2
else : 
    while True :
        # 맨 윗장을 뽑아 결과물 박스에 담고,
        resultBox.append(myBox2.pop())
        # 그 다음장을 맨 아래로 삽입.
        myBox2.insert(0, myBox2[len(myBox2)-1])
        myBox2.pop()
    
        # 카드가 한장 남았으면 바로 결과물 박스에 담는다.
        if len(myBox2) == 1 :
            resultBox.append(myBox2.pop())
            break

# 출력 포맷 맞추기
for i in range(len(resultBox)):
    print(resultBox[i], end= ' ')