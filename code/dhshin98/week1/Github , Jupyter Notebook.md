# Github

## git이란?

- Git은 컴퓨터 파일의 변경 사항을 추적하고 여러명의 사용자들 간에 해당 파일의 작업들을 조율하는 데에 사용되는 분산 버전 관리 시스템이다.
- 주로 소프트웨어 개발 과정에서 소스코드 관리 (버전 관리, 협업 등)을 위하여 주로 사용된다
- 어떠한 집합의 파일의 변경 사항을 지속적으로 추적하기 위해 사용될 수 있다.
- 분산 버전 관리 시스템으로서 빠른 수행 속도에 중점을 둔다
- 즉, Git이란 소스 관리를 위한 분산 버전 관리 시스템이라고 할 수 있다


## git 명령어

1. git init: 로컬 저장소를 생성한다. 
2. git clone “원격 저장소 주소”: 원격 저장소를 생성한다. 
3. git remote add origin “원격 저장소 주소”: 로컬 저장소와 원격 저장소를 연결한다. 
4. git status: 아직 반영되지 않은 파일을 확인해본다. (반영되지 않은 파일은 빨간색으로 뜬다.)
5. git add <filename>: 파일을 업로드 해준다. 
6. git commit -m “commit 한 내용 설명” : commit 을 기준으로 버전이 관리된다. 
7. git push origin ‘branch”: 해당 branch에서 commit한 내용을 원격 저장소에 올린다. 
8. git branch <branchname>: 새로운 branch를 생성한다. 
9. git push origin <branchname>: 새로 생성한 branch이름으로 push할 수 있다. 
10. git merge <branchname>: 다른 가지의 변경 내용을 현재 가지에 병합할 수 있다. 
11. git checkout <branchname>: 해당 branchname으로 branch를 변경해 그 상태에서 작업을 수행한다.  



# Jupyter Notebook

## 특징
1. 셀단위로 실행한다
2. markdown, code의 두가지 방식으로 나뉜다.
- Edit 모드를 시작하려면 셀을 클릭하거나 키보드에서 Enter를 누르면 되고, Edit 모드일 때만 셀에 내용을 입력할 수 있다.
- Command 모드를 시작하려면 셀 외부의 아무 곳이나 클릭하거나 키보드에서 Esc를 누르면 됩니다. 
- command 모드에서 키보드 m를 눌러서 code 입력창을 markdown 입력창으로 변경할 수 있다.
- 다시 code 입력창으로 돌아오려면 y를 누르면 된다.


```python

```
