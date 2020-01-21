setA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

subsets = []
for _i in range(1 << 12):
    presubset = []
    for _j in range(12):
        if _i & (1 << _j):
            presubset.append(setA[_j])

    subsets.append(presubset)

t = int(input())

for _t in range(1, t+1):
    cnt = 0
    input_str = list(map(int, input().split()))
    n = input_str[0]
    k = input_str[1]
    if k > 78:
        print('#{} 0'.format(_t))
    else:
        for subset in subsets:
            if sum(subset) == k and len(subset) == n:
                cnt += 1

        print('#{} {}'.format(_t, cnt))