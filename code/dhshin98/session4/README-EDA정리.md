EDA2 세션 내용 정리

# 1 .데이터 분석

1. Optimization: 해결해야 할 문제를 알고, 분석 방법도 알고 있는 경우
2. Solution: 해결해야 할 문제는 알고 있지만, 분석 방법을 모르는 경우
3. Insight: 기존의 분석 방법은 알고 있지만, 대상이 명확하게 무엇인지 모르는 경우
4. Discovery: 분석 대상과 분석 방법을 모두 모르는 경우

<br> 데이터 수집-> 시각화탐색 -> 패턴도출 -> 인사이트

# EDA(Exploratory Data Analysis, 탐색적 데이터 분석)

## 정의

데이터의 특징과 내재하는 구조적인 관계를 알아내기 위한 분석 기법
<br> 수집한 데이터를 다양한 각도에서 관찰하고 이해하는 과정이라고 할 수 있습니다.

- EDA를 통해 저희는 수집한 데이터를 이해하고 특성을 파악할 수 있으며, 문제에 대한 통찰(Insight)을 얻을 수 있다
- 이를 바탕으로 향후 분석의 방향 을 설정

## 과정

> 데이터 및 결측치 확인
> Feature 분석 및 시각화<br>

    -데이터 유형에 따라 다양한 시각화 방식 사용<br>
    -결측치 처리<br>

> Feature Engineering과 Data Cleaning
> Feature 분석 및 시각화

    - 데이터 유형에 따라 다양한 시각화 방식 사용
    - 결측치 처리

# 시각화 종류

1. 명목형 자료 Bar plot(막대그래프), Count plot, Pie chart
2. 자료 개형 Histogram, Box plot(박스 그림), Stem and leaf plot(줄기 - 잎 그래프)
3. 시계열 및 변수 간 관계 Time series plot(시계열 그래프), Scatter plot(산점도)

# https://matplotlib.org/

# https://seaborn.pydata.org/

## 여러개의 그래프 그리기: subplot() 함수

matplotlib.pyplot 모듈의 plt.subplot(row, column, index)

## Pie Chart

- explode: 부채꼴이 파이 차트의 중심에서 벗어나는 정도
- autopct: 부채꼴 안에 표시될 숫자의 형식
- shadow: 그림자

## Count Plot

- 항목별 개수를 세어줌
- 해당 column을 구성하고 있는 value들을 구분하여 보여줌

## Bar Plot

- bar (세로형)
- barh (가로형) ('h'orizontal)

## Count Plot

- x, y: 데이터의 변수명을 갖는 파라미터
- hue: (optional) 색깔 인코딩을 위해 컬럼명을 갖는 파라미터
- data: (optional) 그래프로 나타내기 위한 데이터셋

## Cross-tabulation

- 카테고리 데이터의 수치를 확인하기에 편리함

## Box Plot

- 분포 확인에 유용함(이상치)

## Violin Plot

-카테고리별 분포를 동시에 확인하기 좋음

## Histogram

- bins: 가로축 구간의 개수
- edgecolor: 막대 테두리 색
- color: 막대 색

## Line Plot

- 연속적으로 변화하는 값을 순서대로 점으로 나타내고, 이를 선으로 연결한 그래프
- 시간/순서에 대한 변화에 적합하여 추세를 살피기 위해 활용

## Scatter Plot

- 이름처럼 각각의 데이터 포인트들을 흩 뿌려놓은 (scatter)형태로,
- x축과 y축의 상관관계를 표현할 때 쓰입니다. -크게 양의 상관관계 (한 변수가 증가할 때 나머지 변수도 같이 증가) 또는 음의 상관관계 (한 변수가 증가할 때 나머지 변수는 감소) 그리고 무상관 (두 변수 간 상관성이 없음)을 나타냅니다.

## Pair Plot

- 비교하려는 변수가 2개 이상일 때 유용

## cross tab

- 각 범주형 데이터의 개수를 열과 행으로 크로스한 표로, 범주형 데이터 2개 이상을 가질때, 각각의 개수를 비교분석하기에 유용

## Correlation Between The Features(heatmap)

- 구체적인 수치 없이도 많은 데이터가 시사하는 바를 패턴으로 나타내는 데 매우 효과적인 시각화 차트로,

- 열분포 형태의 비쥬얼한 그래픽으로 출력합니다.

- annot:셀에 수치 표시 True/False

# Feature Engineering & Data Cleaning

- Feature Engineering이란, 초기 데이터로부터 특징을 가공하고 생산하여 모델의 입력 데이터를 생성하는 과정
- 문자보다는 숫자, 개별값보다는 범위로 구분하도록 데이터를 가공하는 것이 좋음
