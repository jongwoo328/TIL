t = int(input())

def p_check_h(row, idx, m ):
    sliced = maplist[row][idx:idx + m + 1]
    tmp1 = maplist[row][idx:idx + m + 1]
    tmp2 = []
    for _i in range(m):
        tmp2.append(tmp1.pop())
    if tmp2 == sliced:
        result = ''.join(sliced)
        return 1, result, sliced
    else:
        return 0, 'hello', ['world']

def p_check_v(col, idx, m):
    sliced = [maplist[_j][col] for _j in range(idx, idx + m )]
    tmp1 = [maplist[_j][col] for _j in range(idx, idx + m )]
    tmp2 = []
    for _i in range(m):
        tmp2.append(tmp1.pop())
    if tmp2 == sliced:
        result = ''.join(sliced)
        return 1, result, sliced
    else:
        return 0, 'hello', ['world']
        
for _t in range(1, t + 1):
    p_chk = False
    n, m = list(map(int, input().split()))
    
    maplist = [list(input()) for _i in range(n)]

    #가로 탐색
    for row in range(n):
        for col in range(n - m + 1):
            if maplist[row][col] == maplist[row][col + m - 1]:
                chk_h, result, sliced = p_check_h(row, col, m)
                if chk_h:
                    p_chk = True
                    break
        if p_chk:
            break
            
    if not p_chk:
        #세로 탐색
        for col in range(n):
            for row in range(n - m + 1):
                if maplist[row][col] == maplist[row + m - 1][col]:
                    chk_v, result, sliced = p_check_v(col, row, m)
                    if chk_v:
                        p_chk = True
                        break
            if p_chk:
                break
    
    print('#{} {}'.format(_t, result))