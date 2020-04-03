# Union Find

Union Find 알고리즘은 모든 원소가 하나의 그룹에만 속한다고 가정했을 때 (**Disjoing Set**)

 `union`, `find` 연산을 이용하여 **두 원소가 같은 집합에 있는지**를 판단하는 알고리즘이다.



이를 위해서 실제로 트리 구조는 아니지만 트리 구조 처럼 집합을 표현한다.

1 ~ 10 까지의 원소가 있다고 가정한다.

```python
element = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```



이 때 각 원소의 부모노드를 자기 자신으로 설정하여 초기화 한다.

```python
parent = [element[i] for i in range(len(element))]
```

이제 각 원소의 부모노드가 `root`이고, 이제 원소 n 이 속한 트리의 `root`를 `parent[n]`으로 접근한다.



