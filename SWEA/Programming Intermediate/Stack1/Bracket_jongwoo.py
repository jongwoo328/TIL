def pop():
    global top
    if len(stack) == 0:
        print('pop 불가')
    else:
        top -= 1
        stack.pop()

def push(value):
    global top
    stack.append(value)
    top += 1

t = int(input())

for _t in range(1, t+1):
    
    input_str = input()

    top = -1
    stack = []
    start = ['(', '{']
    end = [')', '}']
    bracket = start + end
    checked = False
    cnt = 0

    for char in input_str:
        if len(stack) == 0: 
            if char in start:
                push(char)
                cnt += 1
            elif char in end:
                print('#{} {}'.format(_t, 0))
                checked = True
                cnt += 1
                break
        else:
            if char in start:
                push(char)
                cnt += 1
            elif char in end:
                cnt += 1
                if end.index(char) == start.index(stack[top]):
                    pop()
                else:
                    print('#{} {}'.format(_t, 0))
                    checked = True
                    break
                
    # 괄호 하나도 없으면 0출력
    if cnt == 0:
        print('#{} {}'.format(_t, 0))
    # 괄호쌍 남으면 0, 안남으면 1출력
    if checked is not True:            
        if len(stack) == 0:
            print('#{} {}'.format(_t, 1))
        else:
            print('#{} {}'.format(_t, 0))