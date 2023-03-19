# Pandas
## 판다스 기초
1. 판다스란?
* 데이터 처리를 위한 라이브러리
* 수치형 테이블과 시계열 데이터를 조작하고 운영하기 유용
* Numpy의 확장판
* Series(1차원 벡터), DataFrame(2차원 벡터, 행렬) 클래스를 제공

2. 판다스 패키지 import, DataFrame 생성
* import pandas as pd로 임포트 하는 것이 관례
* DataFrame 생성방법
- 데이터를 리스트나 일차원 배열로 준비
- 각각의 열에 대한 이름을 키로 가지는 딕셔너리 생성
- DataFrame 생성자에 넣기

3. DataFrame 확인
* type(df): 데이터 타입 확인
* df.head(n), df.tail(n): 맨 앞, 뒤 n개의 row를 반환
* df.shape: 배열 크기 반환
* df.info(): 메타 데이터 조회

4. DataFrame 데이터 추가, 삭제
* 데이터 생성
- df['prob'] = [0.8, 0.6, 0.4, 0.2]: prob 이름의 column 생성
- df.loc['type'] = ['A', 'B']: type 이름의 row 생성

* 데이터 삭제
- del df['prob']: prob 이름의 column 삭제
- df.drop(labels=None, axis=0, index=None, columns=None, level=None, **inplace=False**, errors='raise')

5. 인덱싱
* 열 인덱싱: df['A']의 표현식을 가짐
* 행 인덱싱: df.loc['가']의 표현식을 가짐
* 행과 열 이름으로 접근하기: loc, iloc, 슬라이싱