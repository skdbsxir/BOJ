import sys, math

# A : 낮에 올라가는 길이
# B : 밤에 떨어지는 길이
# V : 나무 길이
# A, B, V = map(int, sys.stdin.readline().split())
A, B, V = map(int, input().split())

if B > A :
    sys.exit(0)
elif A > V :
    sys.exit(0)
elif V > 1000000000 :
    sys.exit(0)
    
# V에서 마지막 B를 빼면 매일 A-B만큼씩 올라가는 셈. s=vt, t=s/v
    # s(거리) = v(속력) * t(시간), t (시간) = s (거리) / v (속력) 이므로
    # total day = (V - B) / (A - B)
total_day = math.ceil((V - B) / (A - B)) # 반올림 해줘야 한다.
print(total_day)