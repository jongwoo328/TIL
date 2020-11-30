# 20055 컨베이어 벨트 위의 로봇

from collections import deque

N, K = map(int, input().split())
input_data = tuple(map(int, input().split()))

belt = deque([n, False] for n in input_data)

step_cnt = 0
zero_cnt = 0

up = 0
down = N - 1

def zero_cnt_up():
    global zero_cnt
    zero_cnt += 1
    if zero_cnt == K:
        print(step_cnt)
        exit()

def upload():
    if belt[up][0] > 0:
        belt[up][1] = True
        belt[up][0] -= 1
        if belt[up][0] == 0:
            zero_cnt_up()

def download():
    if belt[down][1] == True:
        belt[down][1] = False

def move():
    for idx in reversed(range(down + 1)):
        if idx == down:
            download()
        elif belt[idx][1] and belt[idx + 1][0] > 0 and belt[idx + 1][1] is False:
            belt[idx + 1][1] = True
            belt[idx + 1][0] -= 1
            if belt[idx + 1][0] == 0:
                zero_cnt_up()
            belt[idx][1] = False

def check():
    download()
    cnt = 0
    for nagudo, _ in belt:
        if nagudo <= 0:
            cnt += 1
            if cnt == K:
                print(step_cnt)
                exit()

while True:
    # 1
    step_cnt += 1
    belt.rotate(1)
    download()

    # 2
    move()
    download()

    # 3
    upload()
    