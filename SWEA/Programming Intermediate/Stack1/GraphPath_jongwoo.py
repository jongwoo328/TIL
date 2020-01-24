t = int(input())

def search(v, ve_dict):
    if v not in ve_dict.keys(): # 해당노드에서 경로가 존재하지 않는 경우
        if len(stack) == 0: # 돌아갈 곳 없으면 (시작지점)
            return False # 불가능
        else: # 돌아갈 곳 있으면
            return search(pop(), ve_dict) # 그 전 노드에서 재탐색
    else:
        if v not in visit: # 방문한적 없는 노드인경우 기록에 추가
            visit.append(v)
            push(v)
        for _e in ve_dict[v]: # 해당 노드에서 방문할 수 있는 노드들 탐색
            if _e == G: # 방문할 수 있는 노드에 목적지가 있으면
                return True # 가능
            elif _e not in visit: # 방문할 수 있는 노드가 가본적 없는경우
                visit.append(_e)
                push(_e)
                return search(_e, ve_dict) # 기록에 추가하고 탐색

        if v == S or len(stack) == 0:
            # 시작지점으로 돌아와 더이상 가볼 곳 없거나
            # 방문할 수 있는곳도, 돌아갈 곳도 없을 때
            return False # 불가능
        else:
            # 갈 수 있는곳은 다 가본 경우
            # 그 전으로 돌아가 재탐색
            return search(pop(), ve_dict)

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
        if search(S, ve_dict): 
            print('#{} {}'.format(_t, 1))
        else:
            print('#{} {}'.format(_t, 0))