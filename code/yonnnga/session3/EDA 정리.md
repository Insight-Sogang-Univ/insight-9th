# EDA 정리
---
## 1. 데이터 분석
__데이터 분석의 4가지 유형__

(1) Optimization: 해결해야 할 문제, 분석 방법 모두 아는 경우   
(2) Solution: 해결해야 할 문제만 아는 경우   
(3) Insight: 분석 방법만 아는 경우  
(4) Discovery: 해결해야 할 문제와 분석 방법 모두 모르는 경우

__데이터 분석에서 가장 중요한 부분__   
통찰(Insight)의 발견 !!!  

>데이터 수집 -> 시각화 탐색-> 패턴 도출-> 인사이트 발견   

(*무엇을 분석해야 하는지 이미 알고 있다면 최적화(Optimization)가 중요)

## 2. EDA란?
- EDA(Explorayoty Data Analysis, 탐색적 데이터 분석): 데이터의 특징과 내재하는 구조적 관계를 알아내기 위한 분석 기법   
- EDA 과정에 통계적인 방법, 데이터 시각화 사용    
- EDA를 통해 수집한 데이터를 기반으로 통찰(insight) 얻음 -> EDA 매우 중요!   

## 3. EDA 과정 
>데이터 및 결측치 확인      
-> Feature 분석 및 시각화    
-> Feature Engineering과 Data Cleaning  

### 3.1 데이터 및 결측치 확인
* df.isnull().sum() 으로 결측치 확인   

### 3.2 Feature 분석 및 시각화
#### (1) Feature의 종류   
Categorical Features(범주형): 
- 종류 표시
- 범주형 데이터 중 명목형 데이터에는 순서 X        
---
Ordinal Features(순서형):
- 순서 O    
---
Continuous Feature(연속형):     
- 연속적인 값 O    
---
Discrete Feature(이산형):
- 정수로 딱 떨어져 셀 수 있음   
---         

#### (2) 시각화 기본 표현
- Figure: 그래프 그리는 바탕
- Size 조절: 
    - fig.set_size_inches(18.5,10.5)    
    - plt.figure(figsize=(10,5))   
    - plt.rcParams['figure.figsize']=(10,7)    
- Axes: plot이 그려지는 공간
- Axis: plot의 축

#### (3) 어떤 데이터에 어떤 시각화?
> Numeric Data인지, Categorical Data인지, 빠진 데이터 있는지 확인 -> 어떤 시각화 사용할지 고민 후 결정
- 시간에 따른 변화: line, area bar
- 비교와 랭킹: bar
- 연관성: scatter
- 분포: box plot, histogram
- 부분이 전체에 차지하는 정도: pie, bar
#### (4) Matplotlib과 Seaborn
- 가장 일반적으로 많이 사용   
- 둘 중에 편한 걸로 사용!!!

### 3.3 수치형 데이터 시각화
#### __(1) 히스토그램(Histplot)__
수치형 데이터의 구간별 빈도수를 나타낸 그래프   
*hue 파라미터에 범주형 데이터 넣으면 특정 범주별로 구분해서 보는 것도 가능
#### __(2) 커널밀도추정 함수 그래프(kdeplot)__
히스토그램을 매끄럽게 곡선으로 연결한 그래프   
#### __(3) 막대 그래프(barplot)__
범주형 데이터 값에 따라 수치형 데이터 값이 어떻게 달라지는지 파악할 때 사용   
#### __(4) 포인트 플롯(pointplot)__
막대 그래프랑 모양만 다름
#### __(5) 박스플롯(boxplot)__
5가지 요약 수치 제공
- 제 1사분위 수(Q1) : 전체 데이터 중 하위 25%에 해당하는 값
- 제 2사분위 수(Q2) : 50%에 해당하는 값(중앙값)
- 제 3사분위 수(Q3) : 상위 25%에 해당하는 값
#### __(6) 바이올린 플롯(violin plot)__
박스 플롯 + 커널밀도추정 함수 그래프   
*hue나 split=True 활용 가능
#### __(7) 카운트플롯(countplot)__
#### __(8) 파이그래프(pie)__
