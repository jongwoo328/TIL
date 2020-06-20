# QuickSort

퀵 정렬은 O(NlogN)의 빠른 정렬 알고리즘이다.

정렬을 위한 추가적인 메모리가 필요하지 않으며. 불안정정렬이다.

과정은 다음과 같다

1. 임의의 pivot을 정한다.
2. pivot에 대항하는 원소를 제외하고 pivot 값보다 작은 원소는 pivot의 왼쪽으로, 큰 원소는 pivot의 오른쪽으로 보낸다.
3. pivot을 제외한 각 왼쪽, 오른쪽 부분에서 1, 2를 반복한다.



위 과정은 아래와 같다.

```python
def quicksort(data, left, right):
  # 데이터 개수가 2 이상일 경우
  if left < right:
    # partition 함수가 1, 2 단계를 수행
    p = partition(data, left, right)

    quicksort(data, left, p-1)
    quicksort(data, p+1, right)
```



이제 partition함수를 어떻게 구성하느냐가 중요해진다.

피벗을 정하는데 많이 사용되는 호어 알고리즘의 경우

1. 임의의 가장자리 원소를 pivot으로 정한다.
2. 나머지 요소들에서 왼쪽끝을 left, 오른쪽 끝을 right라고 하면
   1. left에 해당하는 값이 pivot보다 크고, right에 대항하는 값이 pivot 보다 작으면 두 원소를 교환하고 left는 증가, right는 감소시킨다.
   2. 둘 중 하나만 해당하는 경우 반대쪽 값만 변화시킨다
   3. 위 둘다 만족하지 않는 경우는 left를 증가시킨다.

위 과정을 left와 right가 교차할 때 까지 반복한다.

교차하고 난 후 right는 pivot보다 작은 영역의 가장 오른쪽을 가리키게 되므로, pivot에 대항하는 원소와 교환한다.

이제 pivot을 기준으로 왼쪽은 작은 원소들, 오른쪽은 큰 원소들이 남게된다.

pivot의 위치인 right를 반환한다.



위 과정은 아래와 같다

```python
def partition(data, left, right):
  pivot = left
  left += 1
  
  while left <= right:
    if data[left] >= data[pivot] and data[pivot] >= data[left]:
      data[left], data[right] = data[right], data[left]
    elif data[left] >= data[pivot]:
      right -= 1
    else:
      left += 1
  data[pivot], data[right] = data[right], data[pivot]
  
  return right
```



완성된 퀵 정렬

```python
def partition(data, left, right):
  pivot = left
  left += 1
  
  while left <= right:
    if data[left] >= data[pivot] and data[pivot] >= data[left]:
      data[left], data[right] = data[right], data[left]
    elif data[left] >= data[pivot]:
      right -= 1
    else:
      left += 1
  data[pivot], data[right] = data[right], data[pivot]
  
  return right

def quicksort(data, left, right):
  if left < right:

    p = partition(data, left, right)

    quicksort(data, left, p-1)
    quicksort(data, p+1, right)

data = [1, 5, 6, 8, 3, 5, 7, 2, 4]
quicksort(data, 0, len(data)-1)
print(data)
```

```
[1, 2, 3, 4, 5, 5, 6, 7, 8]
```

