"""
분자 A, 분모 B
A/B 를 했을때 나오는 소숫점 아래 N번째 자리수 찾기.

3 4 1 인경우 3/4 = 0.75, 1위치는 7.
25 7 5 인경우 25/7 = 3.571428571428517, 5 위치는 2.
121 4
"""

# 첫 접근
 ## A/B를 str 형태 그대로 저장해 str변수로 저장
 ## for문을 굴려서
 ## '.'을 만나면 해당 위치를 기록
 ## 해당위치 + N의 index위치를 갖는 str변수의 값 출력.
 # !! 소수점 아래 .75 인 경우 .750000.... 같은 경우 생각을 못하게 된다.
 # !! 당연히 IndexError 남.
"""
A, B, N = map(int, input().split())

# repr : 객체의 인쇄 가능한 표현을 포함한 문자열을 돌려줍니다.
# https://python.flowdas.com/library/functions.html#repr
res = repr(A / B)

# 소수점 아래에서 위치만 찾으면 됨.
"""
"""
try:
    print(res[6])
except:
        print('0')
"""
"""
count = 0
for i in range(len(res)) :
    # 소수점을 만나면 거기부터 세면된다. 근데 how?
    # '.'를 만나면 해당 index를 count에 저장만 하자.
    if res[i] == '.':
        count = i

# 그렇게 해서 출력할 부분은 소수점위치(count) + N만큼 떨어진 값.

if A % B == 0:
    print('0')
else :
    print(res[count+N])


# 나눠 떨어지면 뒷부분이 0인경우 어떠카냐. 
# 당연하게 IndexError뜸.
# 이게 아닌가?? 
"""


# 두번째 접근
 ## list 범위 초과하면 IndexError 니까
 ## 초과된 범위 아래론 0이란 소리일것?
 ## try-except써서 try에서 출력시도, 안되면 except로 0을 출력하면 되지 않을까?
"""
try:
    if A % B == 0:
        print('0')
    else :
        print(res[count+N])
except:
    print('0')
    
이렇게 아래 넣었는데 틀리대 ㅠㅠㅠㅠㅠ
"""

# 세번째 접근 (https://jsy-coding-blog.tistory.com/37)
 ## A를 B로 나누는 과정을 자세히 살펴보면
 ## A가 B보다 작다면 --> A에 0을 붙인다. (A * 10을 하는 셈.)
 ## A가 B보다 커졌으니 B로 나눈다.
 ## 나머지를 다시 A라 하고, B로 나눈다.
 ## A가 B보다 작다면 --> A에 0을 붙인다.
 ## 이를 쭉~ 반복하다가 나머지가 0이 되면 다 나누게 된 셈.
 ### 다시 정리해보면
  ## 1. A가 B보다 작으면 A에 10을 곱한다.
  ## 2. A를 B로 나눈 몫과 나머지를 구한다.
  ## 3. 몫은 소수점의 자리가 되고, 나머지는 다시 A로 갱신된다.
  ## 4. 다시 1번으로 돌아간다. 
  ## 이를 나머지가 0이될때 까지 반복.
# 하...자괴감 오지게드네.. 발상의 전환 ㅅㅂ...
  
# Task 수행할 함수를 그냥 만들자.
def Divide(a, b, n) :
    myList = []
    index = 0 
    
    # 주어진 숫자 N+1 까지 나누기 반복.
    while index != n+1:
        # A가 B보다 작으면 
        # A에 10을 곱함.
        if a < b:
            a *= 10
            myList.append(0) # 10곱해서 나눈거니 얘는 소수점 아래 수. 리스트에 추가.
        # 몫과 나머지를 구해서 저장.
        quotient = int(a / b)
        remainder = int(a % b)
        
        # 리스트에 몫 추가.
        myList.append(quotient)
        
        # 나머지에 대해 A를 다시 갱신.
        # N+1까지 나누기를 해야되니까 index 증가.
        a = remainder * 10
        index += 1
      # 출력해서 보면 요구한 N만큼 0이 늘어난걸 볼 수 있음.
      # 나눠떨어지지 않고 쭉 이어지면
      # 원하는 위치 N까지 나눈 값이 들어간걸 볼 수 있음.
    # return myList, index
    return myList[n]

A, B, N = map(int, input().split())
print(Divide(A,B,N))

# 처참하게 패배... 