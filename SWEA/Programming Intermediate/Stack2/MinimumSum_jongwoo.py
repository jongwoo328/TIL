def track(s):
    global _sum
    localsum = 0
    if s == n:
        for idx in selected:
            localsum += mapList[selected.index(idx)][idx]
        _sum = _sum if _sum < localsum else localsum
    else:
        for _i in range(n):
            if _i not in selected:
                # 유망하지 않는 경우 탈출
                localsum = 0
                for _idx in selected:
                    localsum += mapList[selected.index(_idx)][_idx]
                if localsum > _sum:
                    break
                # 유망한 경우
                else:
                    selected.append(_i)
                    track(s + 1)
                    selected.pop()
    return

t = int(input())

for _t in range(1, t+1):
    _sum = 100
    n = int(input())
    mapList = [list(map(int, input().split())) for _i in range(n)]
    sumList = []

    selected = []
    track(0)

    print('#{} {}'.format(_t, _sum))