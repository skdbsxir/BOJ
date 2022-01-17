N = int(input())
num = [input() for _ in range(N)]

i = 1 # for counting

while True:
    if len(set(map(lambda x: x[-i:], num))) == N:
        print(i)
        break
    i += 1