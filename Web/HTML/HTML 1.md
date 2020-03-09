# HTML

Hyper Text Markup Language. 문서를 구조화함



## 1. HTML 문서의 기본 구조

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
        
    </body>
</html>
```

1. **DOCTYPE**

사용하는 문서의 종류를 선언

2. **html 요소**

문서의 root를 알려줌.

html 최상위 요소

head와 body를 포함

3. **head 요소**

문서 제목, 인코딩 같은 문서 정보를 담고있음.

브라우저에 표시되지 않음

css, 외부파일, 메타태그 (og 등)를 선언

4. **body 요소**

브라우저 화면에 표시되는 내용



---



## 2. Tag &  DOM Tree

### 1. Element

```html
<h1> 웹 문서 </h1>
```

1. **여는 태그** : `<h1>`
2. **닫는 태그** : `<h1>`
3. **내용** : 웹 문서



### 2. Self-closing element

```html
<img src="url"/>
```

닫는 태그가 별도로 존재하지 않음



### 3. Attribute (속성)

```html
<a href='google.com'/>
```

1. 속성명 : `href`
2. 속성값 : `'google.com'` 

- id, class, style 은 태그와 상관없이 모두 사용가능



### 4. DOM 트리

태그는 중첩사용 가능함

```html
<body>
    <h1>
        웹 문서
    </h1>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</body>
```

- `<body>` / `<h1>` : 부모-자식 관계
- `<li>` / `<li>` : 형제 관계
-  `<h1>` / `<ul>` : 형제 관계



### 5. 시맨틱 태그

컨텐츠의 의미를 설명하는 태그

문서를 의미적으로 구조화 하기 위한 태그

| 태그    | 설명                                                 |
| ------- | ---------------------------------------------------- |
| header  | 헤더 (문서 전체 or 섹션)                             |
| nav     | 내비게이션                                           |
| aisde   | 사이드 공간                                          |
| section | 컨텐츠의 그룹                                        |
| article | 사이트 내에서 독립적으로 구분되는 영역 (글, 기사 등) |
| footer  | 문서 or 섹션의 푸터                                  |