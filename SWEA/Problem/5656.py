import itertools
 
t = int(input())
def isWall(y, x):
    if 0 <= y < H and 0 <= x < W:
        return False
    return True
 
def reset():
    for key, val in ref_dict.items():
        for i, j in val:
            brick[i][j] = key
 
def dest(y, x):
    n = brick[y][x]
    brick[y][x] = 0
    if n == 0:
        return
    elif n == 1:
        brick[y][x] = 0
        return
    for i in range(1, n):
        if isWall(y, x+i) is False:
            dest(y, x+i)
            brick[y][x+i] = 0
        if isWall(y, x-i) is False:
            dest(y, x-i)
            brick[y][x-i] = 0
        if isWall(y+i, x) is False:
            dest(y+i, x)
            brick[y+i][x] = 0
        if isWall(y-i, x) is False:
            dest(y-i, x)
            brick[y-i][x] = 0
 
def drop(w):
    for i in range(H):
        if brick[i][w] != 0:
            dest(i, w)
            return
def grav():
    for j in range(W):
        tmp = []
        for i in range(H):
            t = brick[H-i-1][j]
            if t != 0:
                tmp.append(t)
        while len(tmp) != H:
            tmp.append(0)
        for i in range(H):
            brick[H-i-1][j] = tmp[i]
 
for _t in range(1, t+1):
 
    N, W, H = map(int, input().split())
 
    brick = [list(map(int, input().split())) for _ in range(H)]
    ref_dict = {i:[] for i in range(10)}
    for i in range(H):
        for j in range(W):
            ref_dict[brick[i][j]].append((i, j))
 
    brick = [[0 for i in range(W)] for j in range(H)]
    # beedlist = list(itertools.product(range(W), repeat=N))
    min_cnt = float('inf')
    for beed in itertools.product(range(W), repeat=N):
        reset()
        brcnt = 0
        for w in beed:
            drop(w)
            grav()
        for i in range(H):
            for j in range(W):
                if brick[i][j] != 0:
                    brcnt += 1
        if brcnt is 0:
            min_cnt = 0
            break
        elif brcnt < min_cnt:
            min_cnt = brcnt
 
    print('#{} {}'.format(_t, min_cnt))