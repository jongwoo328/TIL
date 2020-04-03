# Union Find

Union Find 알고리즘은 모든 원소가 하나의 그룹에만 속한다고 가정했을 때 (**Disjoing Set**)

 `union`, `find` 연산을 이용하여 **두 원소가 같은 집합에 있는지**를 판단하는 알고리즘이다.



이를 위해서 실제로 트리 구조는 아니지만 트리 구조 처럼 집합을 표현한다.

1 ~ 10 까지의 원소가 있다고 가정한다.

```python
element = [1, 2, 3, 4, 5, 6, 7, 8]
```



## `find`

이 때 각 원소의 부모노드를 자기 자신으로 설정하여 초기화 한다.

```python
parent = [element[i] for i in range(len(element))]
```

이제 각 원소의 부모노드가 `root`이고, 이제 원소 n 이 속한 트리의 `root`를 `parent[n]`으로 접근한다.

그러면 원소 `n`이 속한 트리의 `root`를 찾는 함수 `find`를 다음처럼 정의할 수 있다.

```python
def find(n):
    if n == parent[n]:
        return n
    return find(parent[n])
```

위 함수는 재귀를 사용해서 `n`의 부모노드 `parent[n]`을 가져오고,  `parent[n] == n` 인지를 검사한다.

`parent[n] == n`이라면 `n`이 최상단 노드일 것이므로 `root`는 `n`이고, `n`을 반환한다.

하지만 그렇지 않다면 다시 부모노드의 값 `parent[n]`를 사용해 `find(parent[n])`를 계산한다.



위 처럼 `find`를 구현하면 트리 깊이가 길어지고, `root` 까지 경로가 겹치는 원소들을 인자로 전달할 때 마다 계산을 중복으로 하게 되기 때문에 다음과 같이 최적화할 수 있다.

```python
def find(n):
    if n == parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]
```

위 처럼 `find`를 정의하면 한번 `root`를 찾았던 원소는 `parent[n]`을 `root`로 바꿔주기 때문에 다음에 다시 같은 원소를 인자로 전달하면 한 번 만에 `root`를 찾을 수 있다.



## `union`

이제 `find`를 이용해 두 집합을 합치는 `union` 함수를 구현할 수 있다.

```python
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[a] = root_b
```

`union`을 통해 `b`가 속한 집합의 `root` 노드가 `a`가 속한 집합의 `root` 노드로 변경되었기 때문에 두 집합은 하나로 합쳐졌고, `find`를 이용하면 `find(a) == find(b)`일 것이다.

