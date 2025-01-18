## 환경 설정

1. UH 디렉토리 안에 .env를 생성한다
   - env 파일 내용

```
FLASK_APP=app
FLASK_DEBUG=true
```

2. app.py를 실행한다.

## Windows에서 쉽게 가상환경으로 들어가기
1. C: 드라이브 바로 아래에 venvs 파일을 만들어준다
2. .cmd 파일을 만들어준다. 내가 열고 싶은 가상환경 이름이 back이면 back.cmd 처럼 작성, 내용은 아래와 같이 적어둔다
    ```
    @echo off
    cd C:/Users/name(일반적으로 내 PC의 이름)/algorithm-strudy/back(가상환경이름)/Scripts
    activate
    ```
3. 이후 Win+Q 키를 이용해서 환경변수 편집에 진입한다. (시스템 환경 변수)
4. 오른쪽 아래의 환경 변수에 들어가서 사용자 변수의 Path를 편집으로 들어간다.
5. 이후 새로 만들기를 통해서 위의 C:/venvs 경로를 추가한다.
### 설정이 완료 되었고 이젠 terminal에서 back(가상환경이름)을 치면 가상환경이 열리게 된다.