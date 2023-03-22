## Feature 분석 및 시각화


### Feature 의 종류

#### Categorial Features(범주형, 명목형)
- 범주형 데이터: 'A', 'B', 'C'와 같이 종류를 표시하는 데이터
- 명목형 데이터: 순서가 없는 범주형 데이터
- ex) 'Sex', 'Embarked' feature

#### Ordinal Features(순서형)
- 순서형 데이터: 순서를 가지는 범주형 데이터
- ex) Height라는 feature가 Tall, Medium, Short라는 값을 갖는다면 Height는 순서형 데이터
- ex) 'PClass' feature

#### Continuous Feature(연속형)
- 연속형 데이터: 연속적인 값을 갖는 데이터
- ex) '키'는 170cm와 171cm 사이에 170.1, 170.2cm 등 무한히 많은 값 존재. 이처럼, 값이 끊기지 않고 연속된 데이터를 연속형 데이터라고 함.
- ex) 'Age' feature

#### Discrete Feature(이산형)
- 이산형 데이터: 정수 단위로 떨어져 셀 수 있는 데이터
- ex) 사과의 개수(3개, 4개), 책의 페이지 수(100pg, 200pg)

### 시각화 기본 표현

#### Figure : 그래프를 그리는 바탕, 도화지
- Figure를 그린 후, plt.subplots로 바탕을 분할하려 각 부분에 그래프를 그리는 방식
- pit.figure를 직접적으로 적어주는 것이 확실하지만, 적지 않아도 자동 생성
- 현재 figure: plt.gcf()

#### Size 조절: fig.set_size_inches(18.5, 10.5)

#### Axes: plot이 그려지는 공간

#### Axis: plot의 축

### 어떤 데이터에는 어떤 시각화를 사용하면 좋을까?

1. 우선 분석할 데이터가 어느 Numerical Data인지, Categorical Data인지 확인해봐야 한다
2. attributes를 파악 후에는 데이터의 성질에 따라 어떤 플롯을 사용할 지 고민

- 시간에 따른 변화: line, area, bar
- 비교와 랭킹 : bar
- 연관성: scatter
- 분포: box plot, histogram
- 부분이 전체에 차지하는 정도: pie, bar

### Matplotlib와 Seaborn

- 일반적으로 EDA를 할 때, Matplotlib와 Seaborn 사용
- Matplotlib: Python 프로그래밍 언어 및 Numpy 라이브러리를 활용한 플로팅 라이브러리
- Seaborn: Matplotlib 기반으로 만들어져 통계 데이터 시각화에 최적화된 라이브러리
- 둘 중에 무엇을, 언제 써야할까? 
    - 답은 없다! Matplotlib에서 α만큼 추가된 것이 Seaborn이기에 편한 라이브러리 사용!


## 수치형 데이터 시각화

### 히스토그램(Histplot)
- 수치형 데이터의 구간별 빈도 수를 나타낸 그래프
- 빈도를 특정 범주 별로 구분해서 보고 싶으면, hue 파라미터에 해당 범주형 데이터를 전달하면 됨

### 커널밀도추정 함수 그래프(kdeplot)
- 히스토그램을 매끄럽게 곡선으로 연결한 그랲

### 막대 그래프(barplot)
- 범주형 데이터 값에 따라 수치형 데이터 값이 어떻게 달라지는지 파악
- ex) sns.barplot(x= 'class', y='fare', data = data) : 범주형 데이터인 class(등급) 피처를 x 파라미터에 수치형 데이터인 fare(비용)를 y 파라미터에 전달해 class에 따라 fare이 어떻게 달라지는지 파악

### 포인트플롯(pointplot)
- 막대그래프와 모양만 다를 뿐, 동일 정보 제공

### 박스플롯(boxplot)
- 막대그리프나 포인트플롯보다 더 많은 정보를 제공
- 5가지 요약 수치 제공
    - 제 1사분위 수(Q1): 전체 데이터 중 하위 25%에 해당하는 값
    - 제 2사분위 수(Q2): 50%에 해당하는 값(중앙값)
    - 제 3사분위 수(Q3): 상위 25%에 해당하는 값

### 바이올린 플롯(violin plot)
- 박스 플롯과 커널밀도추정함수 그래프를 합쳐 놓은 그래프
- 특정 범주 별로 구분해 보고 싶으면 hue 파라미터에 해당 범주형 데이터 전달
    - ex) 성별에 따른 등급별 나이 분포: sns.violinplot(x='class', y='age', hue='sex', data=data)


### 카운트플롯(countplot)
- 범주형 데이터의 빈도 수를 나타낸 그래프

### 파이 그래프(pie)
- 부분이 전체에서 차지하는 정도를 보여주는 그래프


