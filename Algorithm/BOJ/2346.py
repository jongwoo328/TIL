# 2346 풍선 터뜨리기
N = int(input())

data = map(int, input().split())
data_list = []
for idx, value in enumerate(data):
    data_list.append((idx + 1, value))

visit = [0 for _ in range(N)]

answer = []
now = 0
for _ in range(N):
    idx, step = data_list[now]
    answer.append(idx)
    visit[idx - 1] = 1
    while step != 0 and len(answer) != N:
        if step > 0:
            now += 1
        elif step < 0:
            now -= 1
        if now < 0:
            now = -(abs(now) % N)
        else:
            now %= N
        if visit[now]:
            continue
        if step > 0:
            step -= 1
        elif step < 0:
            step += 1
    visit[now] = 1

print(*answer)