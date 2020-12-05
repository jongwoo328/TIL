# 20303 할로윈의 양아치

from collections import deque

N, M, K = map(int, input().split())

candy_per_kid = list(map(int, input().split()))

friends = [list() for _ in range(N)]
visit = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

candy_list = []
def check(kid):
    candy_sum = 0
    kid_count = 0
    queue = deque()
    queue.append(kid)
    visit[kid] = 1
    while queue:
        kid_now = queue.popleft()
        kid_count += 1
        candy_sum += candy_per_kid[kid_now]
        for next_kid in friends[kid_now]:
            if not visit[next_kid]:
                visit[next_kid] = 1
                queue.append(next_kid)
    candy_list.append((kid_count, candy_sum))

for kid in range(N):
    if not visit[kid]:
        check(kid)

memo = [0 for _ in range(K + 1)]

for i in range(len(candy_list)):
    for j in range(K, 0, -1):
        if candy_list[i][0] < j:
            memo[j] = max(memo[j], memo[j-candy_list[i][0]] + candy_list[i][1])

print(memo[-1])