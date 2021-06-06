"""
나이가 17세보다 많거나 몸무게가 80kg 이상이면 성인부. 그 외에는 청소년부.

입력 - 이름과 두 자연수(나이, 몸무게)
입력의 마지막은 # 0 0

출력 - 이름 뒤에 Senior, Junior 출력.

ex)
Joe 16 34
Bill 18 65

Joe Junior
Bill Senior
"""
T = []
while True:
    T.append(input().split())
    
    # # 0 0 이 입력으로 오면 삭제하고 break.
    if T[-1] == ['#', '0', '0']:
        T.pop(-1)
        break    
# print(T)

# str로 받아진 나이, 몸무게는 int로.
for i in range(len(T)) :
    T[i][1] = int(T[i][1])
    T[i][2] = int(T[i][2])

# print(T)
# 조건에 맞춰서 출력.
for i in range(len(T)) :
    if T[i][1] > 17 or T[i][2] >= 80 :
        print(T[i][0] + ' Senior')
    else :
        print(T[i][0] + ' Junior')