"""
두 수가 주어짐.
상수는 주어진 수를 거꾸로 읽고 크기비교.
거꾸로 크기비교한 수 중 큰수를 대답.

입력 : 칠판에 적은 두 수. 같지 않은 세자리 수, 0 포함 X.
출력 : 상수의 대답

ex) 734 893 -> 437
"""
A, B = list(map(str, input().split()))
revA, revB = int(A[::-1]), int(B[::-1])
if revA > revB:
    print(revA)
else:
    print(revB)