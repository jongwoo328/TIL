def game(i, j):
    
    if j - i == 1:
        if inputList[i] == inputList[j]:
            return i
        elif inputList[i] == 2:
            return j if inputList[j] == 3 else i
        elif inputList[i] == 1:
            return j if inputList[j] == 2 else i
        elif inputList[i] == 3:
            return j if inputList[j] == 1 else i
    elif  i == j:
        return i

    l = inputList[game(i, (i + j)//2)]
    r = inputList[game((i + j)//2 + 1, j)]
    if l == r:
        return min(game(i, (i + j)//2), game((i + j)//2 + 1, j))
    elif l == 2:
        return game(i, (i + j)//2) if r == 1 else game((i + j)//2 + 1, j)
    elif l == 1:
        return game(i, (i + j)//2) if r == 3 else game((i + j)//2 + 1, j)
    elif l == 3:
        return game(i, (i + j)//2) if r == 2 else game((i + j)//2 + 1, j)
        

t = int(input())

for _t in range(1, t+1):

    n = int(input())

    inputList = list(map(int, input().split()))

    winner = game(0, len(inputList) - 1) + 1

    print('#{} {}'.format(_t, winner))
    