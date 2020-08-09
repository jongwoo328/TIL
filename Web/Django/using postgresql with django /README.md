# Django와 PostgreSQL 연동시키기

추후 참고용으로 기록

> Docker PostgreSQL을 이용하는 경우



## 1. PostgreSQL 설치

1. docker pull

   ```bash
   docker pull postgres
   ```

2. docker run

   ```bash
   docker run -ti -d --name {컨테이너이름} -e POSTGRES_PASSWORD={비밀번호} -p 5432:5432 postgres
   ```

3. docker exec를 통한 접속

   ```bash
   docker exec -ti {컨테이너이름} /bin/bash
   ```



## 2. PostgreSQL에 Django용 DB 만들기

1. 1-3 명령어를 통해 접속

2. postgres로 superuser 전환

   ```console
   root@2ea39d7de38c:/# su postgres
   ```

3. psql 실행

   ```console
   postgres@2ea39d7de38c:/$ psql
   ```

4. Django용 유저 생성

   > 비밀번호는 따옴표로 감쌀것

   ```sql
   postgres=# create user {유저이름} with password '{비밀번호}';
   ```
   - 생성한 유저로 로그인하기
   ```console
   postgres@2ea39d7de38c:/$ psql -U {유저이름} {DB이름} -W -h localhost

5. Django용 DB 생성

   ```sql
   postgres=# create databse {DB이름} owner {유저이름} encoding 'utf-8';
   ```

6. 유저 설정

   ```sql
   postgres=# alter role {유저이름} set client_encoding to 'utf-8';
   postgres=# alter role {유저이름} set timezone to 'Asia/Seoul';
   postgres=# grant all privileges on database {DB이름} to {유저이름};
   ```
   
7. 종료

   ```console
   exit
   ```

   

## 3. Django settings.py 수정하기

`DATABASES` 를 아래와 같이 수정

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{DB이름}',
        'USER': '{유저이름}',
        'PASSWORD': '{비밀번호}',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```



## 4. 연결 확인

```console
python manage.py runserver
```

