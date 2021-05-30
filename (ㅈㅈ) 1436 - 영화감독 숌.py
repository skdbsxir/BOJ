"""
6이 적어도 3개이상 연속으로 들어가는 수.
제일 작은게 666.

666(N=1)
1666(N=2) 2666 3666 4666 5666 6666 7666 8666 9666
16666 26666 36666 46666 56666 66666 76666 86666 96666
166666 266666 366666 466666 566666 666666 76666 866666 966666
...

N번째 영화제목에 들어가는 숫자 찾기.
N 은 10,000보다 작거나 같은 자연수.
"""

"""
리스트 생성? 해서 그 안에 N번째 원소 찾기?
어떻게 생성?

666 - 1666 - ... - 9666 - 16666

1~9까지 붙고난 후에 -> 16~96 붙고 -> 166 ~ 966 붙고 -> 1666 ~ 9666 붙고...

1 ~ 9 까지 붙이고 -> 리스트 카피한다음 -> 뒤에 6을 하나 늘리기? 메모리낭비 조땔거같은데

1 ~ 9 까지 붙이고 -> 이 리스트 써서 다시 6 하나씩 붙이고 -> 이 리스트 써서 다시 66 하나씩 붙이고 -> 어케 다붙이지

1 ~ 9 까지 붙이고 -> i = 11 ~ 20에서 6 하나 붙이고 -> 21 ~ 30에서 6하나 붙이고...
"""
N = int(input())

number = 666

# 브루트 포스 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
while N!=0 :
    if '666' in str(number):
        N -= 1
    number += 1

print(number-1)
"""
# 설명
 N = 2를 넣으면
 number는 666부터 1씩 증가.
 number가 666을 포함하고 있으니 N이 1 감소
 number는 다시 667부터 1씩 증가.
 그렇게 증가하다가 1666이 되면 N=0이 되고 while문 종료.
 최종계산된 number-1이 N에 해당하는 원소.
"""

"""
# 이게 아닌가벼
titleList = []
titleList.append(number)

for i in range(1, 10):
    titleList.append(str(i) + number)
    if i == 5:
        for j in range(0, 10):
            titleList.append(number + str(j))
"""
"""
for i in range(1, 10):
    titleList.append(titleList[i] + '6')
    
for i in range(10, 19):
    titleList.append(titleList[i] + '6')
    
for i in range(19, 28):
    titleList.append(titleList[i] + '6')
    
for i in range(28, 37):
    titleList.append(titleList[i] + '6')
"""
"""
# 범위가 9씩 늘어나네?
a = 1
b = 10
while True:
    if len(titleList) == 10000:
        break
    
    for i in range(a, b):
        titleList.append(titleList[i] + '6')
    a += 9
    b += 9
    
print(titleList[N-1])
"""
"""
이런 경우를 생각못했네 ㅅㅂ 
5666
6661 6662 6663 6664 6665 6666 6667 6668 6669
7666

...

56666
66661 66662 66663 66664 66665 66666 66667 66668 66669
76666

...
"""
"""
# print(titleList[6][0]) # 앞자리가 6
for i in range(1, 10):
    # 앞자리가 6이면 6661 6662 6663 6664 6665 6666 6667 6668 6669 을 넣고?
    print('%d번째 for문 돕니다.' % i)
    if titleList[i][0] == '6' :
        print('if문 걸렸나요?')
        for j in range(1, 10) :
            print('안쪽 for문 걸렸나요?')
            titleList.append(number + '6' + str(j))
            print('더해졌나요?')
    titleList.append(titleList[i] + '6')
"""
"""
# 괜히 머리만 박살나겟다
print(titleList)    
for i in range(1, 10):
    titleList.append(titleList[i] + '6')
"""