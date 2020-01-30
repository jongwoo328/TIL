t = int(input())

for _t in range(1, t+1):
    
    n, m = map(int, input().split())
    
    inputlist = list(map(int, input().split()))
    
    print('#{} {}'.format(_t, inputlist[m%n]))