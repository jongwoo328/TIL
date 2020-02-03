def calAbs(a, b):
    result = a - b
    if result < 0:
        result = -1 * result
    return result

def isWall(x, y):
    if x < 0 or x > 4 or y < 0 or y > 4:
        return True
    else:
        return False

arr = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
sum = 0

for i in range(5):
    for j in range(5):
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if not isWall(x, y):
                sum += calAbs(arr[i][j], arr[y][x])

print(sum)

