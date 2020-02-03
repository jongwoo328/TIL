# 가장 작은 원소부터 위치를 교환

# 전체 자료를 정렬
def selectionSort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

# k 번째로 작은 값 찾기
def selection(a, k):
    for i in range(k):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a[k-1]

data = [64, 25, 10, 22, 11]

selectionSort(data)
print(data)

print(selection(data, 3))