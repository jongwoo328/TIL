# 20056 마법사 상어와 파이어볼
from math import floor

N, M, K = map(int, input().split())

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

map_dict = {}
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_ball = (m, s, d)
    map_dict[(r, c)] = map_dict.get((r, c), list()) + [fire_ball]

def dprint(dictionary):
    for key in dictionary:
        print(key, dictionary[key])

def move(new_map_dict):
    for key, value in map_dict.items():
        r, c, = key
        fireball_list = value
        for fireball in fireball_list:
            m, s, d = fireball
            rd = dr[d] * s
            rc = dc[d] * s
            newr = r + rd
            newc = c + rc
            if newr > N:
                newr %= N
                if newr == 0:
                    newr = N
            if newc > N:
                newc %= N
                if newc == 0:
                    newc = N
            if newr < 0:
                newr = (newr - 1) % N
                newr += 1
                # if newr == 0:
                #     newr = 1
            if newc < 0:
                newc = (newc - 1) % N
                newc += 1
                # if newc == 0:
                #     newc = 1
            if newr == 0:
                newr = N
            if newc == 0:
                newc = N


            new_map_dict[(newr, newc)] = new_map_dict.get((newr, newc), list()) + [(m, s, d)]
            
def merge(new_map_dict):
    for key, value in new_map_dict.items():
        r, c = key
        fireball_list = value
        length = len(fireball_list)
        if len(fireball_list) >= 2:
            m_sum = 0
            s_sum = 0
            fireball_cnt = 0
            odd_direction_cnt = 0
            even_direction_cnt = 0
            for fireball in fireball_list:
                m, s, d = fireball
                m_sum += m
                s_sum += s
                fireball_cnt += 1
                if d % 2:
                    odd_direction_cnt += 1
                else:
                    even_direction_cnt += 1
            
            new_m = floor(m_sum // 5)
            new_s = floor(s_sum // fireball_cnt)

            if new_m > 0:
                if odd_direction_cnt == length or even_direction_cnt == length:
                    direction_list = (0, 2, 4, 6)
                else:
                    direction_list = (1, 3, 5, 7)

                new_map_dict[key] = [ (new_m, new_s, direction) for direction in direction_list ]
            else:
                new_map_dict[key] = []

def get_mass_sum(map_dict):
    mass_sum = 0
    for fireball_list in map_dict.values():
        for fireball in fireball_list:
            m, s, d = fireball
            mass_sum += m
    return mass_sum

for time in range(K):
    new_map_dict = {} 

    move(new_map_dict)
    merge(new_map_dict)
    # dprint(new_map_dict)

    map_dict = new_map_dict

print(get_mass_sum(map_dict))