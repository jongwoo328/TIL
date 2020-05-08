

# KMP

KMP 알고리즘은 주어진 문자열 안에서 찾는 문자열을 빠르게 찾을 수 있는 알고리즘이다.

가장 쉬운 방법으로 짰을 때는 항상 모든 index에서 주어진 keyword만큼 검사해야 하기 때문에 O(NM)의 시간복잡도가 필요하지만 KMP를 이용하면 O(N+M)의 시간복잡도로 탐색할 수 있다.

이미 탐색한 부분의 정보를 가지고 중복탐색하는 경우를 없애기 때문에 가능하다



## Prefix & Suffix

prefix는 접두사, suffix는 접미사를 의미한다.`ABBABBABAABBAAB` 라는 문자열에서 `ABBAAB` 를 찾는 경우를 생각해보면 아래와 같다.

### 1.

|   A   |   B   |   B   |   A   |  B   |   B   |  A   |  B   |  A   |  A   |  B   |  B   |  A   |  A   |
| :---: | :---: | :---: | :---: | :--: | :---: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **A** | **B** | **B** | **A** |  A   | **B** |      |      |      |      |      |      |      |      |

처음에 패턴을 검사하면 일치하지 않는다.

이 때 다음 인덱스부터 검사하지 않고 (A), 세 칸 뒤의 인덱스부터 검사해도 된다. (B)

### A

|  A   |  B   |   B   |  A   |  B   |  B   |  A   |  B   |  A   |  A   |  B   |  B   |  A   |
| :--: | :--: | :---: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|      |  A   | **B** |  B   |  A   |  A   |  B   |      |      |      |      |      |      |

### B

|  A   |  B   |  B   |   A   |   B   |   B   |   A   |  B   |  A   |  A   |  B   |  B   |  A   |
| :--: | :--: | :--: | :---: | :---: | :---: | :---: | :--: | :--: | :--: | :--: | :--: | :--: |
|      |      |      | **A** | **B** | **B** | **A** |  A   |  B   |      |      |      |      |

그 이유는 우리가 처음에 탐색을 할 때 했던 검사를 통해 '두 번째 인덱스는 찾으려는 패턴과 일치하지 않는다'라는 정보를 유도할 수 있기 때문이다.

하지만 이 방법 또한 패턴 내 재탐색을 통해 알아낸다면 결국 그만큼 자원을 소모하게 된다.

KMP알고리즘은 DP를 이용해 찾고자 하는 패턴 내에서 각 부분 접두사(Prefix)와 부분 접미사(Suffix)가 일치하는 경우의 최대 길이를 저장하고, 이를 이용해 위에서 말한 정보를 얻어낸다.



더 자세히 설명하기 위해 예시로 들었던 경우를 다시 살펴보면

`ABBAAB` 는 자기 자신을 제외하고

 `A`, `AB`, `ABB`, `ABBA`, `ABBAA`의 다섯 가지 접두사와, `A`, `AA`, `BAA`, `BBAA`, `BBAAB` 의 다섯 가지 접미사가 존재한다.

그리고 패턴의 인덱스 0 부터 n ( n < `len(pattern) `) 의 각 부분문자열에 대해 **자기 자신을 제외하고 접두사와 접미사가 일치하는 최대 길이**를 저장한다. 그리고 그 결과는 아래와 같다.

| 부분 문자열 |            접두사 목록            |           접미사 목록            | 최대 공통 접두/접미사 |  위치  | 저장되는 값 |
| :---------: | :-------------------------------: | :------------------------------: | :-------------------: | :----: | :---------: |
|     `A`     |                 -                 |                -                 |           -           | `p[0]` |      0      |
|    `AB`     |                `A`                |               `B`                |           -           | `p[1]` |      0      |
|    `ABB`    |            `A` , `AB`             |            `B`, `BB`             |           -           | `p[2]` |      0      |
|   `ABBA`    |         `A`, `AB`, `ABB`          |         `A`, `BA`, `BBA`         |          `A`          | `p[3]` |      1      |
|   `ABBAA`   |     `A`, `AB`, `ABB`, `ABBA`      |     `A`, `AA`, `BAA`, `BBAA`     |          `A`          | `p[4]` |      1      |
|  `ABBAAB`   | `A`, `AB`, `ABB`, `ABBA`, `ABBAA` | `B`, `AB`, `AAB`, `BAAB`,`BBAAB` |         `AB`          | `p[5]` |      2      |

 

위 방식이 DP인 이유는 `p[n]` 을 구할 때 `p[n-1]`을 이용해 구할 수 있기 때문이다. 자세한 알고리즘은 아래와 같다

우선, 부분문자열이 크기가 1인 경우는 자기자신을 제외하고 접두사/접미사가 존재하지 않으므로 0이다

### 1. 

:arrow_right: `p[0] = 0`

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| p    | 0    |      |      |      |      |      |



### 2. 

|       |  A   |  B   |
| :---: | :--: | :--: |
| **i** |      |  i   |
| **j** |  j   |      |

`i = 1`

`j = 0`

이 때 `pattern[i] != pattenr[j]` 이므로

:arrow_right: `p[1] = p[0] + 0` 

> 전 단계 까지의 일치하는 최대 크기 + 현재 인덱스의 일치 여부(0 / 1)

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| p    | 0    | 0    |      |      |      |      |



### 3. 

|       |  A   |  B   |  B   |
| :---: | :--: | :--: | :--: |
| **i** |      |      |  i   |
| **j** |  j   |      |      |

`i = 2`

`j = 0`

`pattern[i] != pattern[j]` 이므로

:arrow_right: `p[2] = p[1] + 0`

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| p    | 0    | 0    | 0    |      |      |      |



### 4. 

|       |  A   |  B   |  B   |  A   |
| :---: | :--: | :--: | :--: | :--: |
| **i** |      |      |      |  i   |
| **j** |  j   |      |      |      |

`i = 3`

`j = 0`

`pattern[i] == pattern[j]` 이므로, `j += 1`

:arrow_right: `p[3] = j`

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| p    | 0    | 0    | 0    | 1    |      |      |



### 5. 

|       |  A   |  B   |  B   |  A   |  A   |
| :---: | :--: | :--: | :--: | :--: | :--: |
| **i** |      |      |      |      |  i   |
| **j** |      |  j   |      |      |      |

`i = 4`

`j = 1`

전 단계에서 일치했기 때문에 추가 일치 여부를 판단하기 위해 `j`도 같이 증가했다.

하지만 `pattern[i] != pattern[j]` , 

:arrow_right: `p[4] = p[j-1]`

그리고 일치하던 중에 불일치한 경우 `j = p[j-1] = 0`로 옮긴다. 

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| p    | 0    | 0    | 0    | 1    | 1    |      |



### 6. 

|       |  A   |  B   |  B   |  A   |  A   |
| :---: | :--: | :--: | :--: | :--: | :--: |
| **i** |      |      |      |      |  i   |
| **j** |  j   |      |      |      |      |

`i = 4`

`j = 0` 

`pattern[i] == pattern[j]` 이므로, `j += 1`

:arrow_right: `p[4] = j = 1`

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| p    | 0    | 0    | 0    | 1    | 1    |      |



### 7. 

|       |  A   |  B   |  B   |  A   |  A   | **B** |
| :---: | :--: | :--: | :--: | :--: | :--: | :---: |
| **i** |      |      |      |      |      |   i   |
| **j** |      |  j   |      |      |      |       |

`i = 5`

`j = 0`

`pattern[i] == pattern[j]` 이므로, `j += 1`

:arrow_right: `p[4] = j = 2`

|      | 0    | 1    | 2    | 3    | 4    | 5    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| p    | 0    | 0    | 0    | 1    | 1    | 2    |



```python
def make_kmp_table(keyword, table):
    table[0] = 0
    
    i = 1
    cnd = 0

    while (i < len(keyword)):
        if keyword[i] == keyword[cnd] or keyword[i] == '*' or keyword[cnd] == '*':
            cnd += 1
            table[i] = cnd
            i += 1
        elif cnd > 0:
            cnd = table[cnd-1]
        else:
            table[i] = 0
            i += 1

def kmp(keyword, table, reference):
    index = []
    r = 0
    k = 0
    len_k = len(keyword)
    len_r = len(reference)
    cnt = 0
    while r < len_r:
        if keyword[k] == reference[r] or keyword[k] == '*':
            r += 1
            k += 1
        else:
            if k == 0:
                r += 1
            else:
                k = table[k-1]

        if k == len_k:
            index.append(r-k+1)
            cnt += 1
            k = table[k-1]

    print(cnt)
    for i in index:
        print(i)

T = input()
P = input()
table = [0] * len(P)
make_kmp_table(P, table)
kmp(P, table, T)

```



```
def make_kmp_table(keyword, table):
    table[0] = 0
    
    i = 1
    cnd = 0

    while (i < len(keyword)):
        if keyword[i] == keyword[cnd] or keyword[i] == '*' or keyword[cnd] == '*':
            cnd += 1
            table[i] = cnd
            i += 1
        elif cnd > 0:
            cnd = table[cnd-1]
        else:
            table[i] = 0
            i += 1

def kmp(keyword, table, reference):
    index = []
    r = 0
    k = 0
    len_k = len(keyword)
    len_r = len(reference)
    cnt = 0
    while r < len_r:
        if keyword[k] == reference[r] or keyword[k] == '*':
            r += 1
            k += 1
        else:
            if k == 0:
                r += 1
            else:
                k = table[k-1]

        if k == len_k:
            index.append(r-k+1)
            cnt += 1
            k = table[k-1]

    print(cnt)
    for i in index:
        print(i)

T = input()
P = input()
table = [0] * len(P)
make_kmp_table(P, table)
kmp(P, table, T)

```

