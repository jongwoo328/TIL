t = int(input())

def bs(p, a):
    cnt = 1
    center = int((1+p)/2)
    l = 1
    r = p
    while center != a:
        if center < a:
            l = center
            center = int((center + r)/2)
            cnt += 1
        else:
            r = center
            center = int((l + center)/2)
            cnt += 1
    return cnt

for _t in range(1, t+1):
    
    p, a, b = map(int, input().split())
    A = bs(p, a)
    B = bs(p, b)
    if A > B:
        print('#{} B'.format(_t))
    elif A < B:
        print('#{} A'.format(_t))
    else:
        print('#{} 0'.format(_t))


    