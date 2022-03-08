# 범위와 이동계획 입력
n = int(input())
plans = input().split()

# 초기 위치 설정
x, y = 1, 1

# L = (0, 1)
# R = (0, -1)
# U = (-1, 0)
# D = (1, 0)

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동
for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            moveX = x + dx[i]
            moveY = y + dy[i]
    # 범위를 벗어 나는 계획일 경우
    if moveX < 1 or moveY < 1 or moveX > n or moveY > n:
        continue
    x, y = moveX, moveY

print(x, y)
