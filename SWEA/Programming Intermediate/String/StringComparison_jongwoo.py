t = int(input())

for _t in range(1, t+1):
    str1 = input()
    str2 = input()

    l1 = len(str1)
    result = dict()
    for chr1 in str1:
        result[chr1] = str2.count(chr1)

    maxvalue = max(result.values())
    print('#{} {}'.format(_t, maxvalue))