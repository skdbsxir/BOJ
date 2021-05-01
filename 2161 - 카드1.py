import sys

N = int(input())

if N > 1000 :
    sys.exit(0)
elif N < 1 :
    sys.exit(0)

# 입력받은 N 만큼의 리스트 생성
myBox = list(range(N))

# 리스트 원소 1씩 증가 (카드는 1부터 N까지.)
i = 0
for i in range(len(myBox)) :
    myBox[i] += 1
    
print(myBox, '\n')

"""
1. 맨 윗장을 버린다 -> pop은 맨 뒤에꺼가 나옴. -> 역순정렬? -> 뽑
2. 그 아래 장을 맨 아래로 내린다 -> 0번째에 끝원소값 삽입 -> 끝원소 pop. 그래야 맨아래로 넣은게 됨.
3. 맨 윗장을 버린다
4. 그 아래 장을 맨 아래로 내린다
5. 1장이 남으면 끝.
"""
myBox2 = myBox[::-1] # 역순 정렬
print(myBox2, '\n')
del myBox
#myBox3 = myBox2.pop()
#print(myBox3)

myBox3 = list()
"""
for j in range(len(myBox2)) :
    if len(myBox2) :
        myBox3.append(myBox2.pop())
        myBox2.insert(myBox2[j], myBox2[len(myBox2)-1])
        print('Box3 내용물 : ', myBox3)
        print('Box2 내용물 : ', myBox2)
        print('\n')
    else :
        break
"""
"""
myBox3.append(myBox2.pop())
print(myBox3)
#print(myBox2)
myBox2.insert(0, myBox2[5])
myBox2.pop()
print(myBox2)

myBox3.append(myBox2.pop())
print(myBox3)
#print(myBox2)
myBox2.insert(0, myBox2[4])
myBox2.pop()
print(myBox2)

myBox3.append(myBox2.pop())
print(myBox3)
#print(myBox2)
myBox2.insert(0, myBox2[3])
myBox2.pop()
print(myBox2)
print('\n...\n')
myBox3.append(myBox2.pop())
myBox2.insert(0, myBox2[2])
myBox2.pop()
myBox3.append(myBox2.pop())
myBox2.insert(0, myBox2[1])
myBox2.pop()
myBox3.append(myBox2.pop())
myBox2.insert(0, myBox2[0])
myBox2.pop()
print(myBox3)
print(myBox2)

result = myBox3 + myBox2
print(result)

while len(myBox2) != 1 :
"""

while True :
    myBox3.append(myBox2.pop()) # 맨 윗장을 뽑고,
    # 그 다음장을 맨 아래로 내림.
    print('결과담은 박스 내용물 : ', myBox3)
    print('옮기기 전 원본박스 내용물 : ', myBox2)
    myBox2.insert(0, myBox2[len(myBox2)-1]) 
    myBox2.pop()
    print('옮긴 후 원본박스 남은 내용물 : ', myBox2)
    print('\n')
    
    if len(myBox2) == 1 :
        myBox3.append(myBox2.pop())
        break

print('최종 결과물 : ', myBox3)

# 출력형식 맞추자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(len(myBox3)):
    print(myBox3[i], end= ' ')
