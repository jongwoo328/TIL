STAT = 0; VALUE = 1; REF = 2
NA = 0; ACT = 1; DEAD = 2

def isValid(y, x):
    if cell.get((y, x), -1) == -1:
        return True
    return False

t = int(input())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _t in range(1, t+1):
    time = 0
    N, M, K = map(int, input().split())
    cell = dict()

    for i in range(N):
        data = list(map(int, input().split()))
        for j, elem in enumerate(data):
            if elem != 0:
                cell[(i, j)] = [NA, elem, elem]

    while time != K:
        time += 1
        tmp_dict = dict()
        for pos, status in cell.items():
            if status[STAT] == NA:
                if status[VALUE] == 1:
                    status[STAT] = ACT
                    status[VALUE] = status[REF]
                else:
                    status[VALUE] -= 1
            elif status[STAT] == ACT:
                y ,x = pos
                for mode in range(4):
                    newy, newx = y+dy[mode], x+dx[mode]
                    if isValid(newy, newx):
                        if tmp_dict.get((newy, newx), 'N') == 'N' or tmp_dict.get((newy, newx), float('inf')) <= status[VALUE]:
                            tmp_dict[(newy, newx)] = status[REF]
                status[VALUE] -= 1
                if status[VALUE] == 0:
                    status[STAT] = DEAD

        for pos, value in tmp_dict.items():
            cell[pos] = [NA, value, value]

    cnt = 0
    for value in cell.values():
        if value[STAT] != DEAD:
            cnt += 1

    print('#{} {}'.format(_t, cnt))