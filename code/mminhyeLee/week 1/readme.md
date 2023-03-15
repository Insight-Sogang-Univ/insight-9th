# [1차 교육세션] Jupyter Notebook, Github



## Jupyter Notebook
1. '셀' 단위로 run
    - Shift + Enter 로 셀 실행
    - [ ] 안 숫자: 셀의 실행 횟수
    - python을 대화식 모드로 실행하는 것과 동일
2. Markdown, Code 두 가지 타입으로 셀의 속성을 지정 가능
3. '셀'을 실행했을 때의 실행 결과는 해당 셀 아래에 출력
4. 출력 결과는 함께 파일에 저장되기 때문에 다른 사용자들이 코드를 실행하지 않고도 결과를 볼 수 있음

jupyter notebook 주소창의 "localhost:8888" -> local 환경(내 컴퓨터)에 있는 페이지
새로운 파일을 만들 때 : new -> python 3 

## Github

### 용어정리
- repostory: 저장소
- local : 내 컴퓨터 (컴퓨터 상의 파일버전관리)
- remote, server : local의 반대 (드라이브 백업)
- OS(Operating System) : 운영체제
window 와 MAC의 SPACE 개행문자가 다르다는 문제를 방지하기 위해 

### GIT / GITHUB란?
- GIT: 버전관리툴
- GITHUB: GIT을 웹(remote, server)으로 확장
- commit
 > 17 commit : 17번의 버전잉 존재
 
### 사용 이유
- 버전관리: 과거 데이터의 백업(원격 저장소에 저장)을 통해 예전 버전을 보존하고 협업을 용이하게 함

### 사용법

1. 로그인
- git config --global user.name "[유저 이름]"
  git config --global user.email "[유저 이메일]"

2. 저장소 만들기
- git init

3. git이 관리할 대상 지정하기
- git add test1.txt : 해당 디렉토리의 test1.txt 파일 추적
- git status : git의 현재 상태 확인

4. 버전 생성하기
- git commit -m "": 새로운 버전 생성 (" "에 메시지 등록 가능)
- git push: 로컬 저장소에서 원격 저장소로 파일 업로드

5. 변경사항 확인하기
- git log -p : 쌓인 변경사항 조회
- git diff : git add 전후의 파일내용 비교

 