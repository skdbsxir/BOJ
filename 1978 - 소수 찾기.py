"""
주어진 N개의 수 중 소시가 몇개인지 찾기.
4
1 3 5 7
"""
N = int(input())
myList = list(map(int, input().split()))
# sortedList = sorted(myList)
"""
소수?
2, 3, 5, 7, 11, 13, ...

가장 작은소수는 2.
그리고 1과 자기자신만을 약수로 갖는 수.
 > 5부턴 2, 3으로 나눠떨어지지 않는 수가 소수.
"""
"""
# 이게 아닌가보다. 에라토스테네스의 채?
count = 0
for i in range(len(myList)) :
    if myList[i] == 2 :
        print('리스트에 2있어요')
        count += 1
    if myList[i] == 3 :
        print('리스트에 3있어요')
        count += 1
    if myList[i] % 2 != 0 and myList[i] % 3 != 0 and myList[i] % 5 != 0 and myList[i] % 7 != 0:
        print('다른소수 있어요')
        if myList[i] == 1 :
            print('소수가 아니라 1이었어요')
            continue
        count += 1

print(count)
"""
def findPrime(n) :
    # 1은 소수가 아니에요
    if n == 1:
        return False
    # 2는 짝수이면서 가장 작은 소수에요
    elif n == 2:
        return True
    # 2부터 n-1까지 for문 돌아요
    for i in range(2, n):
        # 만약 n이 2,3,4,5...로 나눠떨어지면 얘는 소수가 아니에요
        # 어케 이런생각을...
        if n % i == 0:
            return False
        # n이 이거로 나눠떨어지지 않으면 얘는 소수에요
    return True # 이 ㅆㅂ 들여쓰기
count = 0
for i in myList:
    # True라면 소수라는 소리죠. count를 +1 해요.
    if findPrime(i) :
        count += 1

print(count)