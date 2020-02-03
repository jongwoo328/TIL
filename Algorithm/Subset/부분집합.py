arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 합이 10이 되는 부분집합 구하기

n = len(arr)

for i in range(1<<n):
    sumlist = []
    for j in range(n):
        if i & (1<<j):
            sumlist.append(arr[j])
    if sum(sumlist) == 10:
        print(sumlist)
