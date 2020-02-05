from collections import deque

def dfs(now):
    global cnt
    if visit[now] == 0:
        visit[now] = 1
        Q.append(now)
        while True:
            # print(Q)
            if len(Q) == 0:
                break
            T.clear()
            for elem in mydict[Q.pop()]:
                if visit[elem] == 0:
                    visit[elem] = 1
                    T.append(elem)
            Q.extend(T)
        cnt += 1
# def bfs(now):
#     global cnt
#     if visit[now] == 0:
#         visit[now] = 1
#         Q.append(now)
#         while True:
#             if len(Q) == 0:
#                 break
#             T.clear()
#             for _ in range(len(Q)):
#                 for elem in mydict[Q.popleft()]:
#                     if visit[elem] == 0:
#                         visit[elem] = 1
#                         T.append(elem)
#             Q.extend(T)
#             # if len(Q) == 0:
#             #     break

#         cnt += 1
            

N, M = map(int, input().split())
data = []
for i in range(M):
    data.append(list(map(int,input().split())))

mydict = dict()

for i in range(1, N+1):
    mydict[i] = []

for d in data:
    mydict[d[0]].append(d[1])
    mydict[d[1]].append(d[0])

Q = deque()
T = deque()
cnt = 0
visit = [0 for i in range(1001)]

for i in mydict.keys():
    # bfs(i)
    dfs(i)

print(cnt)

