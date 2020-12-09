# 18231 파괴된 도시
N, M = map(int, input().split())

map_arr = [[] for _ in range(N)]

def reset_index(input):
    return int(input) - 1

def add_one(input):
    return input + 1
    
for _ in range(M):
    st, ed = map(reset_index, input().split())
    map_arr[st].append(ed)
    map_arr[ed].append(st)

K = int(input())
destroyed = set(map(reset_index, input().split()))

def is_bombed(input_city):
    city_list = [input_city] + map_arr[input_city]
    for city in city_list:
        if city not in destroyed:
            return input_city, False
    else:
        return input_city, True

answer = set()
destroyed2 = set()

def add_destroy(city):
    destroyed2.add(city)
    for other_city in map_arr[city]:
        destroyed2.add(other_city)

for check_city in range(N):
    target, check = is_bombed(check_city)
    if check:
        answer.add(target)
        add_destroy(target)
        
if destroyed2 == destroyed:
    print(len(answer))
    print(*map(add_one, answer))
else:
    print(-1)