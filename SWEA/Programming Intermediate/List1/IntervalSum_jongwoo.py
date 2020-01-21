t = int(input())
​
def rangeSumMinMax(list, M, N):
    
    min = sum(list[0:M])
    max = min
    tmp_before = max
    for _i in range(0, N - M):
        tmp_after = tmp_before + list[M + _i] - list[_i]
        max = tmp_after if tmp_after > max else max
        min = tmp_after if tmp_after < min else min
        tmp_before = tmp_after
    return max - min
​
for _t in range(1, t + 1):
    
    n, m = map( int, input().split())
    
    numlist = list( map( int, input().split()))
​
    print('#{} {}'.format(_t, rangeSumMinMax(numlist, m, n)))