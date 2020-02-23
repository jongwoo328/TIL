def rot():
    global data
    data = data[1:] + data[0]

def selsort(arr, k):
    for i in range(k):
        a = max(arr[i:])
        arr[arr.index(max(arr[i:]))], arr[i] = arr[i], a
    return arr[k-1]
def slce(data):
    global n1, n2, n3, n4
    tmp = []
    for i in range(0, N//4):
        tmp.append(data[i])
    n1 = ''.join(tmp)
    tmp = []
    for i in range(N//4, N//2):
        tmp.append(data[i])
    n2 = ''.join(tmp)
    tmp = []
    for i in range(N//2, (3*N)//4):
        tmp.append(data[i])
    n3 = ''.join(tmp)
    tmp = []
    for i in range((3*N)//4, N):
        tmp.append(data[i])
    n4 = ''.join(tmp)

t = int(input())

for _t in range(1, t+1):

    N, K = map(int, input().split())
    myset = set()
    mylist = list()
    data = input()
    n1 = ''
    n2 = ''
    n3 = ''
    n4 = ''
    slce(data)
    
    myset.add(int(format(int(n1, 16), 'd')))
    myset.add(int(format(int(n2, 16), 'd')))
    myset.add(int(format(int(n3, 16), 'd')))
    myset.add(int(format(int(n4, 16), 'd')))

    for _ in range(N//4):
        rot()
        slce(data)
        myset.add(int(format(int(n1, 16), 'd')))
        myset.add(int(format(int(n2, 16), 'd')))
        myset.add(int(format(int(n3, 16), 'd')))
        myset.add(int(format(int(n4, 16), 'd')))
    
    mylist = list(myset)
    print('#{} {}'.format(_t, selsort(mylist, K)))