t = int(input())

def search(v):
    global ve_dict

    if v not in ve_dict.keys():
        if len(stack) == 0:
            return False
        else:
            return search(pop())
    else:
        if v not in visit:
            visit.append(v)
            push(v)
        for _e in ve_dict[v]:
            if _e == G:
                return True
            elif _e not in visit:
                visit.append(_e)
                push(_e)
                return search(_e)

        if len(stack) == 0:
            return False
        else:
            return search(pop())

def push(value):
    global top
    stack.append(value)
    top += 1

def pop():
    global top
    if len(stack) == 0:
        print('pop불가')
    else:
        result = stack.pop()
        top -= 1
        return result

for _t in range(1, t + 1):
    # 입력
    V, E = map(int, input().split())

    ve_list = [list(map(int, input().split())) for _i in range(E)]

    S, G = map(int, input().split())

    ve_dict = {}
    # key : 노드, value : key에서 갈 수 있는 노드 list
    visit = []
    # 방문 기록을 순서대로 저장 (중복x)
    stack = []
    # 탐색깊이 stack
    top = -1
    # stack 인덱스

    # ve_dict 구성
    for _i in range(len(ve_list)):
        ve_dict[ve_list[_i][0]] = []
    
    for _i in range(len(ve_list)):
        ve_dict[ve_list[_i][0]].append(ve_list[_i][1])

    if S not in ve_dict.keys(): # 시작지점에서 경로가 없는경우
        print('#{} {}'.format(_t, 0))
    else:
        if search(S): 
            print('#{} {}'.format(_t, 1))
        else:
            print('#{} {}'.format(_t, 0))