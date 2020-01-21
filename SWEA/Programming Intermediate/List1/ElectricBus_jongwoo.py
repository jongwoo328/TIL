t= int(input())

for _t in range(1, t+1):
    
    # 입력
    movMax, stMax, chgNum = input().split(' ')
    movMax = int(movMax)
    stMax = int(stMax)
    chgNum = int(chgNum)

    chgList = list(input().split(' '))
    for _i in range(len(chgList)):
        chgList[_i] = int(chgList[_i])

    station = [ bool(chgList.count(i)) for i in range(0, stMax + 1) ]

    
    chgCnt = 0 # 충전횟수
    now = 0 # 현재 정류장 번호
    fail_chk = True # 충전기 위치 검증

    #충전기 위치 검증
    chgList.append(stMax)
    maxDist = 0
    for idx in range(len(chgList)-1):
        dist = chgList[idx+1] - chgList[idx]
        maxDist = maxDist if maxDist > dist else dist
        if maxDist > movMax:
            fail_chk = False
            break

    if fail_chk:
        while now < stMax - movMax:
            for _i in range(movMax, 0, -1):
                if station[now + _i]:
                    now += _i
                    chgCnt += 1
                    break
    
    print("#{} {}".format(_t, chgCnt if fail_chk else 0))