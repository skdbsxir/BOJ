"""
원을 가르는 Pab, Pbc, Pca, Pda

Pab, Pbc, Pca가 주어졌을 때 Pda ?
"""
"""
원 내부 점 P를 잇는 4개의 선 a,b,c,d에 대해
a*c = b*d 만 알면 뭐...
"""
a, b, c = map(int, input().split())
d = a*c/b

print(d)