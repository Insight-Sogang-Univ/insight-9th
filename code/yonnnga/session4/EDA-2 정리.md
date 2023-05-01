# EDA-2 정리

## EDA 기본 정보
EDA: Exploratory Data Analysis 탐색적 데이터 분석. __수집한 데이터를 다양한 각도에서 관찰하고 이해하는 과정__
EDA의 순서:
1. 데이터 및 결측치 확인
2. Feature 분석 및 시각화 (다양한 시각화 방식 활용 및 결측치 처리)
3. Feature Engineering과 Data Cleaning


## EDA 실습
### 2. 데이터 및 결측치 확인
#### 2.1 라이브러리 불러오기
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
#### 2.2 데이터 설명
#### 2.3 결측치 확인
```python
data.isnull().sum()
```


### 3. Feature 분석 및 시각화
__데이터 유형에 따라 다양한 시각화 방식을 사용하는 것이 중요__
분류| 내용 
---|---|
명목형 자료 | Bar plot(막대그래프), Count plot, Pie chart
자료 개형 | Histogram, Box plot(박스 그림), Stem and leaf plot(줄기 - 잎 그래프)
시계열 및 변수 간 관계 | Time series plot(시계열 그래프), Scatter plot(산점도) 
#### __3.1 Feature의 종류__
__Categorical Features(범주형,명목형):__
- 종류를 표시하는 데이터
- 범주형 데이터 중 명목형 데이터에는 순서 X
---
__Ordinal Features(순서형):__
- 범주형 데이터 중 순서를 가지는 데이터 
---
__Continuous Feature(연속형):__
- 연속적인 값을 갖는 데이터
---
__Discrete Feature(이산형):__
- 정수로 딱 떨어져 셀 수 있는 데이터
---
            

#### __3.2 시각화 방식__
___그래프 여러 개 만들기__
```python
fig,ax=plt.subplots(m,n,figsize=(x,y))
: 사이즈 x*y에 m행 n열 개의 그래프
ply.subplot(m,n,i)
: m행,n열,i번째
```

__Count Plot__
```python
sns.countplot('열', hue='', data=data)
```
- hue: (optional) 색깔 인코딩을 위해 컬럼명을 갖는 파라미터
- data: (optional) 그래프로 나타내기 위한 데이터셋
- 항목별 개수를 세어줌
- 해당 column을 구성하고 있는 value들을 구분하여 보여줌

__Bar Plot__    
* bar (세로형)
* barh (가로형) ('h'orizontal, 수평의)

__Pie Chart__    
* explode: 부채꼴이 파이 차트의 중심에서 벗어나는 정도
* autopct: 부채꼴 안에 표시될 숫자의 형식
* shadow: 그림자
    
__Cross-tabulation__    
* 카테고리 데이터의 수치를 확인하기에 편리

__Box Plot__    
* 분포 확인에 유용

__Factor Plot__
* X축 또는 Y축 한 축을 지정하여 범주형(카테고리형) 데이터를 표현하기 좋음
```python
sns.factorplot(x,y,hue='',data=data)
```

__Violin Plot__
* 카테고리별 분포를 동시에 확인하기 용이
```python
sns.violinplot(x,y,hue='',data=data,split=True)
```

__Historgram__
* bins: 가로축 구간의 개수
* edgecolor: 막대 테두리 색
* color: 막대 색

__Cat Plot__
* 숫자형 변수와 하나 이상의 범주형 변수의 관계를 보여줌   

__Dist Plot__
* matplotlib의 hist 그래프와 kdeplot을 통합한 그래프
* 분포와 밀도를 확인 가능

__heatmap__
* 각 변수들 간의 상관관계 확인 가능
* 구체적인 수치 없이도 많은 데이터가 시사하는 바를 패턴으로 나타내는 데 매우 효과적인 시각화 차트
* annot:셀에 수치 표시 True/False


#### __3.3 Feature Engineering & Data Cleaning__
__연속형 feature 순서형으로 변환하기__
```python
data[]=pd.qcut(data[],n)
```


#### __3.4. Converting String Values into Numeric__
* string을 머신러닝 모델에 사용할 수 없음!! numeric 값으로 변환해야 함