t = int(input())

for _t in range(1, t+1):
    str1 = input()
    str2 = input()
    
    chk = str1 in str2
    
    if chk:
        print('#{} {}'.format(_t, 1))
    else:
        print('#{} {}'.format(_t, 0))
    #n = len(str1)
    #m = len(str2)
    
    #for _i in range(m-n+1):
        #if str2[_i: _i + n] == str1:
            #print('#{} {}'.format(_t, 1))
            #break
    #else:
        #print('#{} {}'.format(_t, 0))