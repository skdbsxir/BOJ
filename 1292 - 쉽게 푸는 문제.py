"""
1을 1번, 2를 2번, 3을 3번, ... 해서 만든 수열 1 2 2 3 3 3 4 4 4 4 5 5 ...


일정 구간을 주어주면 그 구간의 합을 구함.

입력 : 구간의 시작과 끝을 나타내는 정수 A,B
출력 : 수열에서 A번째 숫자부터 B번째 숫자까지의 합

ex) 3 7 -> 15
"""
# 수열을 미리 만들고 
# 거기서 구간 합 구하기?
# print(sum(range(1, 45)))
# print(range(1, 45)) 
# 1~44까지 수열은 990.
# 그 뒤에 45가 10번 더. 그러면 수열 크기가 1000.

myList = []
# 1,2,2,3,3,3,4,4,4,4,5,5,5,5,5 이런식으로?
for i in range(1, 45):
    myList.append(i)

# 숫자를 보고
# 해당 숫자를 숫자만큼 더 추가?
for i in range(1, len(myList)) :
    for j in range(i+1, len(myList)):
        if myList[i] == j:
            myList.append(j)
        i += 1
myList.append(44)        
for i in range(10) :
    myList.append(45)
    
# print(len(myList)) # 문제요구 1000만큼 맞춤.

# 주어진 구간의 합 구하기?
sortList = sorted(myList)
# del myList

# 요소 갯수 확인!!!
# for i in range(1, 46) :
#    print('%d 는 총 %d 개 있어요' % (i, sortList.count(i)))

A, B = map(int, input().split())
total = 0

for i in range(A-1, B):
    # 더해지는 구간 확인
    # print('%d번째에 있는 더할게요 : %d' % (i+1, sortList[i]))
    total += sortList[i]
print(total)
# print(sum(sortList[A-1:B]))