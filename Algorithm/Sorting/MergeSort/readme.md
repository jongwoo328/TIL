# MergeSort

병합정렬은 O(NlogN)의 안정정렬이다.

정렬 순서는 다음과 같다

1. 원소의 크기가 2이상이면 데이터를 동일한 크기로 2분할 한다.
   1. 그렇지 않으면 아무것도 하지 않는다.
2. 나눠진 각 원소에 대해 동일한 정렬을 시행한다.
3. 그러면 정렬된 두 데이터를 얻게되고 왼쪽부터 하나씩 비교하면서 작은것 부터 결과로 만든다.



데이터를 재귀적으로 분할하는 부분은 다음과 같다

```python
def mergesort(data):
  if len(data) == 1:
    return data
  # 1
  middle = len(data) // 2
  # 2
  left = mergesort(data[:middle])
  right = mergesort(data[middle:])
  # 3
  return merge(left, right)
```



정렬하는 함수는 다음과 같다

```python
def merge(left, right):
  i = 0
  j = 0
  result = []
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  if j == len(right):
    result.append(left[i:])
  else:
    result.append(right[j:])
  return result
```



완성된 병합정렬은 다음과 같다

```python
def merge(left, right):
  i = 0
  j = 0
  result = []
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  if j == len(right):
    result += left[i:]
  else:
    result += right[j:]
  return result

def mergesort(data):
  if len(data) == 1:
    return data

  middle = len(data) // 2

  left = mergesort(data[:middle])
  right = mergesort(data[middle:])

  return merge(left, right)


data = [1,5,7,5,4,3,2,6,8,9,3,2]
print(mergesort(data))
```

```text
[1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9]
```

