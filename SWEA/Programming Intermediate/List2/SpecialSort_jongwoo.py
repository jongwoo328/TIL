t = int(input())

for _t in range(1, t+1):
    
    sort_chk = True
    n = int(input())

    numList = list(map(int, input().split()))

    for _i in range(n-1):
        if sort_chk:
            select = max(numList[_i:])
        else:
            select = min(numList[_i:])
        numList[numList[_i:].index(select) + _i], numList[_i] = numList[_i], numList[numList[_i:].index(select) + _i]
        sort_chk = not sort_chk
        
    print('#{}'.format(_t), end=' ')

    for _i in range(10):
        if _i == 9:
            print('{}'.format(numList[_i]))
        else:
            print('{}'.format(numList[_i]), end=' ')