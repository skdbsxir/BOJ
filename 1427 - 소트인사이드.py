"""
각 자리수를 내림차순으로 정렬
"""
myNum = list(input())
sortNum = sorted(myNum, reverse=True)

for i in range(len(sortNum)):
    print(sortNum[i], end='')
