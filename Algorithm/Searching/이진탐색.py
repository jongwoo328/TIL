def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:

            return middle

        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1

    # 검색실패
    return False

key = 7
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data, key))