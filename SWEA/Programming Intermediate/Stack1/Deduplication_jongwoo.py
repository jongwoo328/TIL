t = int(input())

def Dedup(string):
    result = string
    for idx in range(len(result) - 1):
        if result[idx] != result[idx+1]:
            continue
        else:
            return Dedup(result[0:idx] + result[idx + 2:])
    return result

for _t in range(1, t+1):

    input_str = input()

    print('#{} {}'.format(_t, len(Dedup(input_str))))