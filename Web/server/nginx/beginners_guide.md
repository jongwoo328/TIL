# Beginner's Guide

> [Nginx document](https://nginx.org/en/docs/beginners_guide.html) 를 공부하기 위해 번역하면서 정리해 놓은 문서입니다.



nginx는 하나의 master process와 여러 개의 worker process를 가지고 있다. master process는 nginx의 환경 설정(configuration)을 reload해서 해석하고 worker process를 관리한다. worker process는 실제로 요청에 대한 처리를 수행한다. nginx는 이런 worker process 사이에서 요청을 효율적으로 분배하기 위해 event-based model을 이용한다. worker process의 수는 configuration file에서 정해지며, 정해진 값이 고정되거나 가용 CPU core 수에 따라 조정된다.

nginx와 nginx module이 하는 일은 configuration file로 정해지는데 이 파일은 기본적으로 `usr/local/nginx/conf`, `etc/nginx` 또는 `usr/local/etc/nginx` 디렉토리 내부의 `nginx.conf` 파일로 지정되어있다.



## Starting, Stopping, and Reloading Configuration

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

