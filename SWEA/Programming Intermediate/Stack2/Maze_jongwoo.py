def miro(now):
    global result

    if now not in visit:
        visit.append(now)
        stack.append(now)
    
    search = [] 
    # 현재위치 기준 map 벗어나지 않는 탐색구역 만들기
    if now[0] != 0 and map[now[0] - 1][now[1]] != 1:
        search.append([now[0] - 1, now[1]])
    if now[0] != n - 1 and map[now[0] + 1][now[1]] != 1:
        search.append([now[0] + 1, now[1]])
    if now[1] != 0 and map[now[0]][now[1] - 1] != 1:
        search.append([now[0], now[1] - 1])
    if now[1] != n - 1 and map[now[0]][now[1] + 1] != 1:
        search.append([now[0], now[1] + 1])

    for m in search:
        if not result: # 백 트래킹 (결과 찾은경우 탐색x)
            if [m[0], m[1]] == end:
                result = 1
                return
            if m not in visit:
                visit.append(m)
                stack.append(m)
                miro(m)
        
    if len(stack) == 0:
        return

t = int(input())

for _t in range(1, t+1):
    result = 0
    n = int(input())
    map = []
    start = []
    end = []

    stack = []
    visit = []
    for _n in range(n):
        tmplist = []
        tmp = input()

        for _m in range(n):
            tmplist.append(int(tmp[_m]))
            if tmp[_m] == '2':
                start.append(_n)
                start.append(_m)
            elif tmp[_m] == '3':
                end.append(_n)
                end.append(_m)
        map.append(tmplist)

    miro(start)
    if result:
        print('#{} {}'.format(_t, 1))
    else:
        print('#{} {}'.format(_t, 0))
