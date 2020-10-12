# Python

- 특징
  - 높은 생산성
  - 객체 지향
  - 인터프리터
  - 동적 타이핑
  - **GIL** (Global Interpreter Lock)

- GIL
  - Cpython, PyPy 등 에서 Python Interpreter가 하나의 스레드만 돌아가도록 제한 함.
  - *Why?*
    1. Python은 각 객체마다 reference count를 통해 GC를 구현함
    2. 따라서 여러 Thread가 같은 객체를 사용할 경우를 대비해서 모든 객체의 reference count를 임계구역화 해야 함
       - 즉, 객체 참조가 변경될 때 마다 Lock 필요
    3. 대신 인터프리터 자체에서 한 시점에 하나의 Thread만 동작하도록 Lock을 전역으로 설정함
    4. 여러 개의 Thread가 생성되면 I/O작업 (Network, Disk 등), 또는 일정 tick 마다 context switching을 발생시켜서 lock을 release함.
  - 결국, CPU위주의 작업에서 불리함
    - multiprocessing 모듈을 사용해 Thread 대신 Process를 사용하는 방법도 있음
- 그럼에도 파이썬을 사용하는 이유
  - 분산 컴퓨팅의 발전
    - 한 컴퓨터만 쓸 필요는 없다.
  - 하드웨어의 발전
    - 프로그램 지연의 대부분은 Network I/O.

