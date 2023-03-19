#  절대경로, 상대경로

## 절대 경로
절대적인 기준을 기준으로 경유한 경로를 모두 기입하는 방식

그렇다면 기준이 무엇인가? 바로 최초 디렉터리이다. 
Ex) C:\Users\username\Desktop\filename.txt

따라서 절대주소는 내가 작성중인 파일이 어디있던 가네 그 주소가 절대로 변하지 않는다. 

## 상대 경로
최초 디렉토리가 아닌 특정 경로를 기준으로 다른 경로를 표시
주로 현재 작업하고 있는 폴더가 기준이 됨.

예시를 통해 살펴보자

https://soharu.tistory.com/11
https://blog.naver.com/tipsware/221275416466

상대경로는 ../ 한단계 위, ./ 현재를 통해 기준이 되는 위치에서 움직여 경로를 표시함을 확인할 수 있다.


상대경로 가 필요한 이유는 서버나 도메인 주소 또는 운영체제의 영향을 받지않고 로컬에서 작업을 하기때문에 편리하기 때문이다.

#  readfile in python
## 파일 열고 닫기

문법: 파일객체 = open(파일명, 파일모드 문자열)

ex) fp = open('test.txt', 'w')
    fp.close()

## 파일 모드 문자열
해당파일의 사용 용도를 결정

-r(read mode): 읽기 전용 모드 (기본값)

-w(write mode): 쓰기 전용 모드

-a(append mode): 파일 마지막에 새로운 데이터 추가

파일의 데이터를 어떤 방식으로 입출력할지

-t : 해당 파일 데이터를 텍스트 파일로 인식 (기본값)

-b: 해당 파일의 데이터를 바이너리 파일(사진, 그림 등)으로 인식

## 파일 내용 읽기
1. read() 함수
 해당 파일의 모든 내용을 읽어들여 하나의 문자열로 반환
2. readline()함수 
 해당 파일의 내용을 한 라인씩 읽어들여 문자열로 반환
3. readlines()함수
 해당 파일의 모든 라인을 순서대로 읽어들여 각각의 라인을 하나의 요소로 저장하는 하나의 리스트 반환

## 파일 내용 추가하기 
write()함수를 사용하면 파일에 새로운 내용 추가 가능
파일 객체.write("추가할 내용")

주의할점 : 쓰기 전용 모드인 'w'는 만약 같은 이름의 파일이 이미 존재하면, 해당 파일에 저장되어 있는 모든 내용을 제거한 후 파일을 열게 됩니다.

따라서 기존에 존재하는 파일에 새로운 내용을 추가하려면 파일 모드 문자열을 ‘w’가 아닌 ‘a’로 전달해서 파일을 열어야만 합니다.
http://www.tcpschool.com/python2018/python_io_file

## 자동으로 파일 닫아주는 with문 
ex) with open('test.txt', 'r') as fp:

    file_data = fp.read()

    print(file_data)

가독성도 좋고 close()함수도 안써도됨!

## pickle
모든 파이썬 데이터 객체를 저장하거나 읽을 수 있음
파일로 저장: pickle.dump(객체, 파일)
파일 읽기: pickle.load(파일)

텍스트 상태 데이터가 아닌 객체 자체를 파일로 저장
장점 :
1. 객체 형태로 보조기억장치에 저장 기능

2. 데이터베이스 사용 기능

3. 네트워크를 통해 다른 컴퓨터에 전송 기능

# preprocessing in data science
## 결측치 처리 

### 결측치 확인하기
- nan 값이 얼마나 있는지 column별로 확인하기

df.isnull().sum()

- 전체 data 개수 대비 NaN의 비율

df.isnull().sum() / len(df)

### 결측치 날려버리기
- axis 0이면 행, 1이면 열 제거, subset은 특정 행 열 지정
df.dropna(axis = 1, how = 'any', subset = None)


### 결측치 채워버리기
- NaN을 0으로 채워버리기

df.fillna(0)

- 평균값으로 채워버리기

df['col1'].fillna(df['col1'].mean(), inplace=True)

label값이 '1인' '열2의' 평균 값을 구한다 

mean1 = df[df['label1'] == 1]['열2'].mean()

Nan값을 위의 mean1값으로 대체한다

df[df['label1'] == 1]['열2'].fillna(mean1)

## 데이터의 병합
concat
https://ybworld.tistory.com/62


## 범주형 데이터의 변환
정수 기반 범주형 데이터를 표현할 수 있는 특수한 데이터형 
pd.categorical()
