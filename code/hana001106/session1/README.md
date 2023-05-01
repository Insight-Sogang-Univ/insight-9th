# 첫 세션에서 배운 내용입니다.

## 1. Jupyter Notebook의 간단한 사용
- jupyter notebook은 '셀' 단위로 실행하며 대화형입니다.
- 확장자가 .py인 경우, 파일 단위로 실행하게 되지만, .ipynb의 경우 하나의 셀이 코드의 실행범위입니다. => 그러나 다음 셀에서도 위에서 실행한 결과값이 유지됩니다.
- 현재 작성하고 있는 markdown 형식이나, code 형식으로 작성할 수 있습니다.
- 실행한 코드 왼쪽에는 실행 횟수가 뜨며, 실행을 할 때마다 1씩 증가하게 됩니다.
- 셀의 실행은 상단의 Run 버튼 이용할 수도 있지만, shift+enter(셀 하나 증가하면서 실행), ctrl+enter(셀 개수 유지하면서 실행)등 단축키로도 실행할 수 있습니다.
++ 상단의 키보드 모양을 누르면 다양한 단축키를 확인할 수 있습니다. # 세션외 추가
> a = 10  
> a # 출력 O  
> print(a) # 출력 O -> 대화형이기 때문에 print를 사용하지 않아도 출력됩니다.  
=> 그러나 다양한 것들을 한번에 출력하려면 print문을 그대로 사용해야 합니다. # 세션외 추가

- jupyter notebook에 대해 간단히 배운 뒤에, 확장성을 위한 nbextensions를 설치하였습니다. 사용한 코드는 아래와 같습니다
> !pip install jupyter_nbextensions_configurator jupyter_contrib_nbextensions  
  !jupyter contrib nbextension install --user  
  !jupyter nbextensions_configurator enable --user  
  => jupyter notebook의 버전이 안 맞는 경우에 설치가 안되는 일이 발생했습니다. => pip install notebook==6.1.5로 해결 # 세션외 추가

## 2. git과 github의 사용
- git에서 주로 사용하는 용어: repository(저장소), local(내 컴퓨터), remote(원격), server(서버), os(운영체제->Mac과 Windows에서 개행문자의 차이를 보인다.)
- git과 github의 차이: git은 버전 관리 툴 자체를 의미하고 web으로 확장된 것을 Github이라 한다.
- git을 사용하는 이유: 버전관리에 유용, 현재에 와서는 여러 사람끼리 코드를 공유하는데에도 자주 사용된다. -> 우리의 경우 프로젝트나, 과제 제출에 사용

1. 저장소 만들기
    ```python
    git init
    ```
2. git이 관리할 대상(파일) 지정하기
    ```python
    git add file_name #현재 디렉토리의 해당 파일 추적
    git add . #현재 디렉토리의 모든 파일 추적
    ```
3. git의 현재 상태 확인
    ```python
    git status
    ```
4. 버전 생성하기
    ```python
    git commit -m "메시지"
    ```
5. 업로드 및 다운로드
    ```python
    git push
    git pull
    ```

### 과제 제출시 사용되는 프로세스
#### 처음할 때
1. fork 해오기
- 원하는 repository에 들어가 우측 상단에 있는 fork 버튼을 눌러 내 repos로 해당 것들을 가져온다.
2. local에 폴더 만들기 + gitbash 열기
- 전용으로 사용할 폴더를 하나 만들고 거기서 git bash를 연다.
3. git bash와 web 상의 git 연결하기
- 위에서 연 git bash에 아래의 코드를 입력하여 내 계정과 연결한다.
    git config -user.name "내 아이디"
#### 항상 해야하는 것
4. clone 실행
- git bash에 아래 코드를 입력하여 clone화 한다. 따옴표 안에는 아까 그 repos 상단에 있는 <>code에 있는 복사해오면 된다.
    ```python
    git clone "~"
    ```
5. 원하는 파일을 경로에 맞는 폴더에 넣어준다.
6. add 하기
- 아래 코드를 통해 추가된 파일들을 add한다.
    ```python
    git add "파일명"
    ```
7. commit and push
- 하고 싶은 말을 추가하여 commit한 뒤 push한다.
    ```python
    git commit -m "버전에 대해 할 말"
    git push
    ```
8. pull request
- web상의 repos에 들어간 뒤에 동기화 된 것을 확인하고, pull request를 통해 과제를 제출한다.

### 추가 사항
1. branch
- branch는 말그대로 가지라고 생각하면 편하다. 여러 사람이 한 과제에 대해 병렬적으로 작업을 진행할 때, 우선 내 작업 branch에서 작업을 끝내고, 이후 master의 branch에 합쳐 중간중간 기록도 남기면서, 서로의 작업에 방해가 되지 않게 할 수 있다.
- 여기서 master은 중심 branch로 생각하면 된다. (처음 repos를 만들 때 자동으로 생성됨, checkout을 통해 변경도 가능)
2. Markdown에서 자주 쓸 것 같은 기능
- VS에서 연 후에 미리보기 기능을 쓰면 바로 어떻게 변환되는 지 알 수 있다. (단축키: ctrl+shift+V )
- code block의 경우 ` 3개씩으로 감싸면 되는데 위쪽에 언어를 써주면 해당 문법에 맞춰진다.

## 3. NOTION의 사용
- 마지막으로 notion의 사용에 대해 간단하게 학습하였습니다. notion의 경우 기존에 사용한 경험이 있어 그리 어렵지 않을 것으로 예상됩니다.

