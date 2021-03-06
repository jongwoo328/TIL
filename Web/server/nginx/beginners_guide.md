# Beginner's Guide

> [Nginx document](https://nginx.org/en/docs/beginners_guide.html) 를 공부하기 위해 번역하면서 정리해 놓은 문서입니다.



nginx는 하나의 master process와 여러 개의 worker process를 가지고 있다. master process는 nginx의 환경 설정(configuration)을 reload해서 해석하고 worker process를 관리한다. worker process는 실제로 요청에 대한 처리를 수행한다. nginx는 이런 worker process 사이에서 요청을 효율적으로 분배하기 위해 event-based model을 이용한다. worker process의 수는 configuration file에서 정해지며, 정해진 값이 고정되거나 가용 CPU core 수에 따라 조정된다.

nginx와 nginx module이 하는 일은 configuration file로 정해지는데 이 파일은 기본적으로 `usr/local/nginx/conf`, `etc/nginx` 또는 `usr/local/etc/nginx` 디렉토리 내부의 `nginx.conf` 파일로 지정되어있다.



## Configuration을 시작, 종료, 다시 불러오기

nginx는 실행파일(executable file)을 작동시켜서 실행한다. 일단 한번 실행된 후에는 `-s` 파라미터를 이용한 명령어를 호출해서 제어할 수 있다.

`nginx -s signal`



*signal* 은 아래 중 하나이다

- `stop` — fast shutdown (즉시 종료)
- `quit` — graceful shutdown (우아한 종료)
- `reload` — reloading the configuration file (설정파일 reload)
- `reopen` — reopening the log files (로그파일 재 생성)



예를 들어, 현재 요청에 대한 응답을 모두 종료한 후 nginx process를 종료하고 싶다면 아래 명령어를 이용하면 된다.

`nginx -s reload`

> 이 명령어는 nginx를 시작한 유저에 의해 종료되어야 한다.



configuration file의 변경점은 아래 명령어로 nginx에 전송시키거나 재시작 하기 전에는 적용되지 않는다.

`nginx -s reload`



master process가 configuration을 reload하라는 명령을 받으면  configuration file의 문법을 검사한 후 적용한다. 이 과정에 성공하게되면 master process는 새로운 worker process들을 실행하고 이전 worker process들 에게는 종료 요청을 보낸다. 이 과정에 실패하게 되면 master process는 변경점을 다시 되돌리고 이전 configuration을 적용한다. 종료 요청을 받은 변경 전의 worker process는 더 이상 새로운 연결을 받아들이지 않고 현재 처리중인 요청을 계속 처리하며, 이 처리가 종료된 후에 worker process를 종료한다.



signal은 `kill`과 같은 Unix tool의 도움으로 전송될 수 있다. 이 경우 signal이 PID를 통해 직접 프로세스로 전달된다.

nginx master process의 PID는 기본적으로 `usr/local/nginx/logs`나 `var/run` 디렉토리 내부에 `nginx.pid`파일로 저장되어았다. 만약 master process의 PID가 1628인 경우, `quit` signal은 아래 명령어를 실행시킨다.

`kill -s QUIT 1628`



현재 실행중인 nginx 프로세스의 리스트를 보기 위해서 `ps`명령이 아래처럼 사용된다.

`ps -ax | grep nginx`



nginx의 signal에 대해 더 자세한 정보는 [Control](https://nginx.org/en/docs/control.html) 에 있다.



## Configuration 파일의 구조

nginx는 configuration file에 적힌 directives(지시자)들에 의해 제어되는 모듈들로 이루어져 있다. 이런 directive는 simple directive와 block directive로 나뉜다. simple directive는 공백으로 구분된 이름과 값으로 구성되어있고, 세미콜론(;)으로 끝나야 한다. block directive는 simple directive와 구조는 같지만 세미콜론(;) 대신 중괄호({})로 감싸진 명령들로 끝나야 한다. block directive가 중괄호 안에서 다른 directive를 가지는 경우에( ex: [events](https://nginx.org/en/docs/ngx_core_module.html#events), [http](https://nginx.org/en/docs/http/ngx_http_core_module.html#http), [server](https://nginx.org/en/docs/http/ngx_http_core_module.html#server), [location](https://nginx.org/en/docs/http/ngx_http_core_module.html#location)) 이 block directive를 context라고 한다.



configuration file의 directive 중 어떠한 context 내에도 속해있지 않은 directive를 main context라고 한다. `events`와 `http` directive는 main context 내부에, `server`는 `http` 내부에, `location`은 `server` 내부에 존재한다.

`#` 로 시작하는 줄은 주석으로 간주한다.



## 정적 콘텐트(Static Content) 제공하기

웹 서버의 주요 임무는 image나 정적 HTML 문서와 같은 파일을 제공하는 것이다. 요청에 따라 아래 처럼 서로 다른 로컬 디렉토리에서 파일을 제공하는 예시를 실행할 수 있을 것이다. (HTML 파일이 있을 `/data/www`디렉토리와 이미지 파일을 포함할 `data/images` 처럼) 이것은 configuration file의 수정을 필요로 하며 `http` block 내부에 두 개의 `location` block으로 `server` block을 설정해야 한다.



처음에, `/data/www` 디렉토리를 만들고 `index.html`을 넣는다. 그리고 `/data/images` 디렉토리에 이미지파일을 넣는다.

다음으로 configuration 파일을 연다. 모든 block을 주석처리하고 새 block을 작성한다

```nginx
http {
  server {
  }
}
```

보통 configuration 파일은 서로 다른 port와 server이름을 가지는 여러 개의 `server` block 을 포함하는데 nginx가 요청을 처리할 `server`를 결정하면 `server` block 내부에 정의된 `location` directive의 매개변수에 요청 헤더의 URI를 테스트한다. 



`server` block 안에 아래  `location` block을 추가한다

```nginx
location / {
  root /data/www;
}
```

이 `location` block은 접두사인 `/`를 명시하고 있는데, 요청을 매칭하기 위해 root directive에 명시된 경로 뒤에 URI를 추가한다. 따라서 로컬 디렉토리 `data/www `로 경로를 형성한다.

만약 여러개의 매칭 `location` block이 존재하는 경우, nginx는 가장 긴 접두사를 선택한다. 위의 `location` block은 가장 짧은 접두사를 제공하는 block이며, 따라서 다른 모든 `location` block들이 매칭에 실패했을 경우 사용된다.

다음으로 두 번째 `location` block을 추가한다

```nginx
location /images/ {
  root /data;
}
```

이 block은 `/images/`로 시작하는 요청에 매칭된다. (`location /` 은 여전히 해당 요청에 매칭되지만 더 짧은 접두사를 가지고 있으므로 무시된다.)

configuration의 결과는 아래와 같을 것이다

```nginx
server {
  location / {
    root /data/www;
  }
  
  location /images/ {
    root /data;
  }
}
```

이 것은 표준 80번 포트를 수신하는 서버에서 이미 작동 중인 설정이고 로컬에서는 `http://localhost/`로 접근할 수 있다. `/images`로 시작하는 URI의 응답에서 서버는 `/data/images/` 디렉토리의 파일을 제공할 것이다. 예를들어 `http://localhost/images/example.png` 요청의 응답으로 nginx는 `/data/images/example.png` 파일을 보낼 것이다. 만약 해당하는 파일이 존재하지 않는다면 nginx는 404에러를 보낸다. 반대로 `/images/`로 시작하지 않는 URI를 가진 요청은 `/data/www` 디렉토리로 연결되어 `http://localhost/some/example.html` 의 요청에 `/data/www/some/example.html` 파일을 응답할 것이다.



아직 nginx를 시작하지 않았다면 새 configuration을 적용하기 위해 시작하고, 이미 시작한 상태라면 `reload` signal을 nginx master process에 보낸다

`nginx -s reload`

> 원하는 대로 동작하지 않는 경우에, 그 이유를 찾기 위해  `/usr/local/nginx/logs` 또는 `var/log/nginx`에 존재하는 `access.log` 파일과 `error.log` 파일을 참고할 수 있다.



## 간단한 프록시 서버 설정하기

nginx를 사용하는 이유 중 하나는 서버가 받은 요청을 다른 서버로 넘겨주고, 다시 응답을 받아서 클라이언트로 보내주는 프록시 서버로 사용하기 위함이다. 

여기서 로컬 디렉토리에 있는 이미지 파일은 제공하고, 다른 모든 요청은 프록시 서버가 대상 서버로 넘겨 줄 기본적인 프록시 서버를 구성할 것이다. 이 예시에서, 두 서버는 모두 하나의 nginx instance로 정의될 것이다.

첫번째로, nginx configuration 파일에 `server` block을 추가한다.

```nginx
server {
  listen 8080;
  root /data/up1;
  
  location / {
  }
}
```



이것은 8080 포트를 수신하는 간단한 서버이다. (전 예시에서는 표준 80포트를 수신했기 때문에 `listen` directive를 사용하지 않았다.)  그리고 모든 요청은 `/data/up1` 디렉토리로 연결된다. `/data/up1`을 만들고 `index.html`을 넣는다. `root` directive가 `server` context에 있다는 것을 기억하라. 이런 `root` directive는 `location` block이 자신만의 `root` directive를 정의하지 않았을 때 이용된다.



다음으로, 이전 예시의 서버 configuration을 프록시 서버로 사용하기 위해 수정한다. 첫 `location` block을[proxy_pass](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass) directive를 사용해 수정한다. 프록시 대상 서버의 이름과 포트는 매개변수로 명시된다. (여기서는 `http://localhost:8080`)

```nginx
server {
  location / {
    proxy_pass http://localhost:8080;
  }
  
  location /images/ {
    root /data;
  }
}
```



여기서 두 번째 `location` block을 특정한 파일 확장자만 매칭해 주기 위해 수정할 것이다. 아래와 같이 수정된다.

```nginx
location ~ \.(gif|jpg|png)$ {
  root /data/images;
}
```

이 매개변수는 정규 표현식으로 `.gif` `.jpg` `.png` 로 끝나는 모든 URI를 매칭한다. 정규 표현식은 `~` 뒤에 위치해야 하며 이 표현식에 맞는 요청은 `/data/images` 디렉토리로 매칭될 것이다.



nginx가 요청에 대한 응답을 전송할 `location` block 을 선택하면 가장 긴 매개변수를 갖는 `location` directive를 검사한다. 만약 정규 표현식으로 매칭되는 경우, 해당하는 `location`을 선택하고 그렇지 않으면 그 전에 기억했던 `location`으로 돌아갈 것이다.

여기서 프록시 서버의 configuration 결과는 아래와 같다

```nginx
server {
  location / {
    proxy_pass http://localhost:8080/;
  }
  
  location ~ \.(gif|jpg|png)$ {
    root /data/images;
  }
}
```



이 서버는 `.gif` `.jpg` `.png` 로 끝나는 요청들만 걸러내어 `/data/images` 디렉토리로 매칭하고 모든 다른 요청은 위에 설정했던 프록시 대상 서버로 전송할 것이다. 

새 configuration을 적용하기 위해 이전에 했던것 처럼  `reload` signal을 보낸다. 

이 예시에서 했던 directive 말고도 프록시 서버 연결을 위한 더 [많은](https://nginx.org/en/docs/http/ngx_http_proxy_module.html) directive가 존재한다.



## FastCGI 프록시 설정하기

PHP처럼 서로 다른 프레임워크나 프로그래밍 언어로 짜여진 어플리케이션을 실행시키는 FastCGI 서버를 라우팅하기 위해 nginx를 사용할 수도 있다.

nginx에서 FastCGI 서버를 사용하는데 가장 기본적인 configuration은 `proxy_pass`처럼 사용되는 [fastcgi_pass](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html#fastcgi_pass) 와  FastCGI 서버로 넘겨줄 매개변수를 설정하는 [fastcgi_param](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html#fastcgi_param) directive이다.

`localhost:9000`으로 접근할 수 있는 FastCGI서버가 있다고 하자. 전 예시에 사용했던 프록시 configuration에서 `proxy_pass`를 `fastcgi_pass`로 변경하고 값을 `localhost:9000`으로 설정한다. PHP에서는 `SCRIPT_FILENAME` 이라는 매개변수로 실행할 스크립트를 명시해주고 `QUERY_STRING` 매개변수로 request parameter를 전송한다. 그 결과는 아래와 같을 것이다.

```nginx
server {
  location / {
    fastcgi_pass localhost:9000;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    fastcgi_param QUERY_STRING $query_string;
  }
  
  location ~ \.(gif|jpg|png)$ {
    root /data/images;
  }
}
```



이것으로 정적 이미지 요청을 제외한 모든 요청들은 프록시 대상 서버인 `localhost:9000` 으로 FastCGI 프로토콜을 통해 전송될 것이다.