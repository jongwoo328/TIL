def bfs(now):
    global visit
    global cnt
    global Q
    if visit[now[0]][now[1]] == 0:
        visit[now[0]][now[1]] = 1
    Q.extend(search(now))

    while True:
        tmp = []
        tmp2 = []
        for next in Q:
            if next == end:
                return cnt
            elif visit[next[0]][next[1]] == 0:
                visit[next[0]][next[1]] = 1
                tmp.extend(search(next))
        Q = tmp[:]
        cnt += 1

        if len(Q) == 0:
            return 0

def search(now):
    global Q
    result = []
    r, c = now[0], now[1]
    if r > 0 and map_list[r - 1][c] != 1 and [r - 1, c] and visit[r - 1][c] == 0:
        result.append([r - 1, c])
    if r < n - 1 and map_list[r + 1][c] != 1 and [r + 1, c] and visit[r + 1][c] == 0:
        result.append([r + 1, c])
    if c > 0 and map_list[r][c - 1] != 1 and [r, c - 1] and visit[r][c - 1] == 0:
        result.append([r, c - 1])
    if c < n - 1 and map_list[r][c + 1] != 1 and [r, c + 1] and visit[r][c + 1] == 0:
        result.append([r, c + 1])
    return result

t = int(input())

for _t in range(1, t + 1):
    
    n = int(input())

    map_list = []
    visit = [ [0 for _ in range(n)] for __ in range(n)]
    Q = []
    cnt = 0
    start = list()
    start = list()

    for _ in range(n):
        tmp = []
        input_str = input()
        for idx in range(len(input_str)):
            tmp.append(int(input_str[idx]))
            if tmp[idx] == 2:
                start = [_, idx]
            elif tmp[idx] == 3:
                end = [_, idx]
        map_list.append(tmp)
    result = bfs(start)
    print('#{} {}'.format(_t, result))