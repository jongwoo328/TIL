# 7568 덩치

N = int(input())

people = []
for _ in range(N):
    people.append(
        tuple(map(int, input().split()))
    )

answer = []
for idx, data in enumerate(people):
    cnt = 0
    for idx2, data2 in enumerate(people):
        if idx != idx2 and data2[0] > data[0] and data2[1] > data[1]:
            cnt += 1
    answer.append(cnt + 1)

print(*answer)