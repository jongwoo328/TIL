# 20057 마법사 상어와 토네이도
from math import floor

N = int(input())

land = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for __ in range(N)]

center = (N // 2, N // 2)

answer = 0

pattern = [(0, 0)]
visit[0][0] = True
dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)

py = (0, 1, 0, -1)
px = (1, 0, -1, 0)
direction = 0

def is_out(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

while True:
    nowy, nowx = pattern[-1]
    if (nowy, nowx) == center:
        break

    newy = nowy + py[direction]
    newx = nowx + px[direction]

    if is_out(newy, newx) or visit[newy][newx]:
        direction = (direction + 1) % 4
        newy = nowy + py[direction]
        newx = nowx + px[direction]

    pattern.append((newy, newx))
    visit[newy][newx] = True

def get_direction(before, after):
    # 좌 하 우 상
    # 0, 1, 2, 3
    by, bx = before
    ay, ax = after
    if by == ay:
        if bx > ax:
            return 0
        else:
            return 2
    elif bx == ax:
        if by > ay:
            return 3
        else:
            return 1

def move(before, after):
    global answer
    # 좌, 하, 우, 상
    # 0, 1, 2, 3
    by, bx = before
    ay, ax = after

    sand_before = land[ay][ax]

    direction = get_direction(before, after)

    if direction == 0 or direction == 2:
        scatter_pattern = [
            (dy[direction] * 2, dx[direction] * 2, 0.05),
            (dy[(direction - 1) % 4] * 2, dx[(direction - 1) % 4] * 2, 0.02),
            (dy[(direction - 1) % 4] * 1, dx[direction] * 1, 0.1),
            (dy[(direction - 1) % 4] * 1, dx[(direction - 1) % 4] * 1, 0.07),
            (dy[(direction - 1) % 4] * 1, dx[(direction - 2) % 4] * 1, 0.01),
            (dy[(direction + 1) % 4] * 1, dx[direction] * 1, 0.1),
            (dy[(direction + 1) % 4] * 1, dx[(direction + 1) % 4] * 1, 0.07),
            (dy[(direction + 1) % 4] * 1, dx[(direction + 2) % 4] * 1, 0.01),
            (dy[(direction + 1) % 4] * 2, dx[(direction + 1) % 4] * 2, 0.02)
        ]
        remain = (dy[direction] * 1, dx[direction] * 1, 0.55)
    else:
        scatter_pattern = [
            (dx[(direction + 1) % 4] * 2, dy[(direction + 1) % 4] * 2, 0.05),
            (dx[direction] * 2, dy[(direction + 2) % 4] * 2, 0.02),
            (dx[(direction + 1) % 4] * 1, dy[(direction - 2) % 4] * 1, 0.1),
            (dx[direction] * 1, dy[(direction - 2) % 4] * 1, 0.07),
            (dx[(direction - 1) % 4] * 1, dy[direction - 2] * 1, 0.01),
            (dx[(direction + 1) % 4] * 1, dy[direction] * 1, 0.1),
            (dx[direction] * 1, dy[direction] * 1, 0.07),
            (dx[(direction - 1) % 4] * 1, dy[direction] * 1, 0.01),
            (dx[direction] * 2, dy[direction] * 2, 0.02)
        ]
        remain = (dx[(direction + 1) % 4] * 1, dy[(direction + 1) % 4] * 1, 0.55)

    sand_out = 0
    for d_y, d_x, r in scatter_pattern:
        nowy = ay + d_y
        nowx = ax + d_x
        sand = floor(r * sand_before)
        sand_out += sand
        if is_out(nowy, nowx):
            answer += sand
        else:
            land[nowy][nowx] += sand
    d_y, d_x, r = remain
    newy = ay + d_y
    newx = ax + d_x
    if is_out(newy, newx):
        answer += sand_before - sand_out
    else:
        land[newy][newx] += sand_before - sand_out

    land[ay][ax] = 0


for idx in reversed(range(1, len(pattern))):
    before = pattern[idx]
    after = pattern[idx - 1]
    move(before, after)
    if after == (0, 0):
        break

print(answer)