t = int(input())

operator = ['+', '-', '/', '*']

for _t in range(1, t+1):
    
    stack = []
    input_str = input().split()
    check = True

    for char in input_str:
        if char == '.':
            if check is True and len(stack) == 1:
                print('#{} {}'.format(_t, stack.pop()))
                break
            else:
                print('#{} error'.format(_t))
                break

        if char in operator:
            if len(stack) <= 1:
                print('#{} error'.format(_t))
                break
            else:
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(a - b)
                elif char == '/':
                    stack.append(int(a / b))
                else:
                    stack.append(a * b)
        else: #숫자
            stack.append(int(char))