
t= int(input())


def minmax(list):
    l = len(list)
    min = int(list[0])
    max = int(list[0])
    for idx in range(1,l):
        value = list[idx]
        min = min if min < int(value) else int(value)
        max = max if max > int(value) else int(value)

    return max - min
    
    

for i in range(1,t+1):

    n = int(input())

    inputList = input().split(' ')

    gap = minmax(inputList)
    
    # print(inputList)
    
    print('#{} {}'.format(i, gap))

