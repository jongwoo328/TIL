# http://bit.do/fqAvb

def paper(w):
    if w > width:
        return 0
    elif w == width:
        return 1
    return paper(w + 10) + paper(w + 20) *2

t = int(input())

for _t in range(1,t+1):
    width = int(input())

    print('#{} {}'.format(_t, paper(0)))