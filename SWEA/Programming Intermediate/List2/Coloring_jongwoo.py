t = int(input())

for _t in range(1, t+1):
    
    mapList = [[0 for _j in range(10)] for _k in range(10)]
    cnt = int(input())
    
    inputList = [list(map(int, input().split())) for _ in range(0, cnt)]
    
    for _j in range(cnt):
        y1, x1 = inputList[_j][0], inputList[_j][1]
        y2, x2 = inputList[_j][2], inputList[_j][3]
        color = inputList[_j][4]
        
        for _k in range(10):
            for _l in range(10):
                if (x1 <= _l <= x2) and (y1 <= _k <= y2):
                    mapList[_k][_l] += color
    
    vCnt = 0
    for _k in range(10):
        for _l in range(10):
            if mapList[_k][_l] == 3:
                vCnt += 1
                    
    print('#{} {}'.format(_t, vCnt))