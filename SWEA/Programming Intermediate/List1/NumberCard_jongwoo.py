t = int(input())
​
for _t in range(1, t+1):
    
    n = int(input())
    cnt = 0
    max = 0
    cards = list( map(int,input()) )
​
    for _i in range(10): 
        if cards.count(max) <= cards.count(_i):
            max = _i
            cnt = cards.count(max)
    
    print('#{} {} {}'.format(_t, max, cnt))