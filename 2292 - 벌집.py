N = int(input())

firstRoom = 1

# a = a1 + d, a1 = 6, d = 6
#a1 = 6
#d = 6

# 각 수열의 첫 집단(firstA1, firstA2, firstA3 = 2, 8, 20, 38) -> 얘네는 6, 12, 18씩 늘어남.
# firstAn = A1 + nd // A1 = 2, d = 6, n=1,2,3...
"""
import numpy as np
A1 = np.arange(2, 8, 1)
listA1 = list(A1)
A2 = np.arange(listA1[0] + 6, listA1[5] + 13, 1)
listA2 = list(A2)
print(listA2)
A3 = np.arange(listA2[0] + 12, listA2[11] + 19, 1)
listA3 = list(A3)
print(listA3)
A4 = np.arange(listA3[0] + 18, listA3[17] + 25, 1)
listA4 = list(A4)
print(listA4)
"""
# 2개를 거쳐야하는 방의 개수 = 6
# 3개를 거쳐야하는 방의 개수 = 12
# 4개를 거쳐야하는 방의 개수 = 18
# 카운트가 +6인 셈.
# 초기 카운터 (firstAn 적은데서 n) = 1부터 시작해 1씩 증가. 이게 방을 들르는 횟수.
counter = 1
while N > firstRoom :
    firstRoom += 6 * counter
    counter += 1
    
print(counter)
    