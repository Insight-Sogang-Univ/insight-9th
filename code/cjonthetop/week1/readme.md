
#Jupyter Notebook와 Github에 대한 내용 정리

##1.Jupyter
* jupyter는 웹에서 돌아가는 컴파일러이다.
* 특징은 shell단위로 코드가 돌아가며, shell의 속성은 크게 2가지로 나뉜다.
    * 1) code _ 우리가 주로 사용하는 code입니다.
    * 2) markdown _ 코드를 부연설명하는 문서들입니다. 현재 이 문서도 markdown으로 작성됩니다.

##2.Github
* git과 github는 다르다. 
    * git은 '버전관리'를 위한 분산버전 관리툴이다.
    * github는 git을 외부(웹)으로 확장한 버전이다.
        * github는 각각 'repository(저장소)' 단위로 관리한다.

* 관리를 하려면 크게 4가지 단계가 필요하고, 각각의 터미널 명령어는 아래와 같다.
    1. 접속 _ 터미널에서 github를 접속한다. 아래 순서대로, 깃허브 이름과 이메일을 입력하고, 저장소를 설정한다.
        * git config --global user.name '{이름}'
        * git config --global user.email '{이메일}'
        * git init
    2. add _ 작업 위치에 파일이 있는 경우, add를 통해서 staging area로 옮길 수 있다. (임시저장상태)
        * txt파일 _ git add a.txt
        * 폴더 파일 _ git add myfolder
        * 현재 디렉토리 _ git add
    3. commit _ 커밋은 현재 버전에 대해 명확하게 작성한다.
        * 원격 저장소(remote) 설정
            * origin이라는 이름으로 url을 추가 _ git remote add origin { __url___ }
    4. push _ commit한 이력이 repository로 저장
        * 현재 폴더를 그대로 업로드하는 게 아니고, 지금까지의 이력/버전을 push한다
        * origin 파일 commit 하기 _ git push origin master
        * 따라서, push 전에 $git status, $git log를 통해 확인하는 습관 필요
    5. pull _ 원격저장소 변경 사항(이력)을 받아옵니다.
        * git pull origin master
