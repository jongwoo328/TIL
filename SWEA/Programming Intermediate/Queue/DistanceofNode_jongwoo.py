import queue as q

def bfs(now):
    global cnt

    # if now not in visit:
    #     visit.append(now)
    if not map_info.get(now, False):
        return 0
    for next in map_info[now]:
        Q.put(next)
        visit[now][next] += 1
        visit[next][now] += 1

    while True:
        for idx in range(Q.qsize()):
            next = Q.get()
            if next == G:
                return cnt
            if map_info.get(next, False):
                for v in map_info[next]:
                    if visit[next][v] != _t:
                        Q.put(v)
                        visit[next][v] += 1
                        visit[v][next] += 1
        if Q.qsize() == 0:
            return 0
        cnt += 1 
    
visit = [[0 for i in range(50)] for j in range(50)]

t = int(input())

for _t in range(1, t+1):

    V, E = map(int, input().split())

    map_info = dict()
    tmplist = []
    Q = q.Queue()
    cnt = 1

    for _ in range(E):
        tmplist.append(list(map(int, input().split())))
    for l in tmplist:
        map_info[l[0]] = []
        map_info[l[1]] = []

    for l in tmplist:
        map_info[l[0]].append(l[1])
        map_info[l[1]].append(l[0])
    
    S, G = map(int, input().split())
    # print(map_info)
    print('#{} {}'.format(_t, bfs(S)))