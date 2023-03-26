# 데이터 분석의 이해(EDA2 정리)

데이터 분석의 4가지 유형  
1. __Optimization__: 해결해야 할 문제를 알고, 분석 방법도 알고 있는 경우  
2. __Solution__: 해결해야 할 문제는 알고 있지만, 분석 방법을 모르는 경우  
3. __Insight__: 기존의 분석 방법은 알고 있지만, 대상이 명확하게 무엇인지 모르는 경우  
4. __Discovery__: 분석 대상과 분석 방법을 모두 모르는 경우

# EDA란?

EDA(Exploratory Data Analysis, 탐색적 데이터 분석)란, 데이터의 특징과 내재하는 구조적인 관계를 알아내기 위한 분석 기법

1. 데이터 및 결측치 확인

    > 라이브러리 및 파일 불러오기
    import numpy as np
    import pandas as pd
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    plt.style.use('seaborn')  # matplotlib style 설정
    
    > 데이터 설명 Data Description
    
    > 결측치 확인
    -데이터 분석을 본격적으로 들어가기 전에, 반드시 데이터에 결측치(null)가 있는지 확인하고, 있다면 처리를 해 주어야 합니다.


2. Feature 분석 및 시각화 (데이터 유형에 따라 다양한 시각화 방식 사용)
3. 결측치 처리
4. Feature Engineering과 Data Cleaning(얻은 insight로 새로운 feature를 만들기 machine learning을 위한 cleaning)

    >
    - 데이터 유형에 따라 다양한 시각화 방식 사용
    - 결측치 처리
    - 시각화를 통해, 많은 양의 데이터를 효과적으로 확인할 수 있음 (infographics) 
    - 요약 통계보다 더 정확한 데이터 분석 결과 도출 가능
    
    ![image.png](attachment:image.png)
    
    > Feature의 종류
    1. Categorical Features(범주형,명목형):‘A’, ‘B’, ‘C’와 같이 종류를 표시하는 데이터 (범주형 데이터 중에서 명목형 데이터에는 순서가 없다.)
    2. Ordinal Features(순서형):범주형 데이터 중에서 순서를 가지는 데이터
    3. Continuous Feature(연속형
    4. Discrete Feature(이산형)
    
    > 피처별 시각화 및 결측값 채우기
    1. 여러개의 그래프 그리기: matplotlib.pyplot 모듈의 subplot() 함수 <기본사용: plt.subplot(row, column, index)>
    2. 여러개의 그래프 그리기: matplotlib.pyplot 모듈의 subplot() 함수 <기본사용: plt.subplot(row, column, index)>
    3. Count Plot :항목별 개수를 세어줌, 해당 column을 구성하고 있는 value들을 구분하여 보여줌
    *Bar Plot (가로형)-> bar (세로형) barh (가로형) ('h'orizontal, 수평의)
    
    *Count Plot-> x, y: 데이터의 변수명을 갖는 파라미터
    hue: (optional) 색깔 인코딩을 위해 컬럼명을 갖는 파라미터
    data: (optional) 그래프로 나타내기 위한 데이터셋
    
    *Cross-tabulation-> 카테고리 데이터의 수치를 확인하기에 편리함
    
    *Box Plot-> 분포 확인에 유용함
    
    *FactorPlot-> 범주형 변수들을 분리하여 표현에 용이
    
    *Violin Plot-> 
    x
    y
    hue
    :카테고리별 분포를 동시에 확인하기 좋음
    
    *Histogram->
    bins: 가로축 구간의 개수
    edgecolor: 막대 테두리 색 
    color: 막대 색
    
    *Embarked: Categorical Value (Factor/CountPlot)
    cross tab : 각 범주형 데이터의 개수를 열과 행으로 크로스한 표로, 범주형 데이터 2개 이상을 가질때, 각각의 개수를 비교분석하기에 유용
    
    *factor plot : X축 또는 Y축 한 축을 지정하여 범주형(카테고리형) 데이터를 표현하기 용이
    
    *Cat Plot : 숫자형 변수와 하나 이상의 범주형 변수의 관계를 보여줌
    
    *Dist Plot: matplotlib의 hist 그래프와 kdeplot을 통합한 그래프로, 분포와 밀도를 확인 가능
    
    *heatmap:
    구체적인 수치 없이도 많은 데이터가 시사하는 바를 패턴으로 나타내는 데 매우 효과적인 시각화 차트로, 열분포 형태의 비쥬얼한 그래픽으로 출력 (annot:셀에 수치 표시 True/False)

5. 시각화 보충
    >1. Line Plot: 연속적으로 변화하는 값을 순서대로 점으로 나타내고, 이를 선으로 연결한 그래프
    시간/순서에 대한 변화에 적합하여 추세를 살피기 위해 활용
    >2. Scatter Plot: 이름처럼 각각의 데이터 포인트들을 흩 뿌려놓은 (scatter)형태로,x축과 y축의 상관관계를 표현할 때 쓰임
    크게 양의 상관관계 (한 변수가 증가할 때 나머지 변수도 같이 증가) 또는 음의 상관관계 (한 변수가 증가할 때 나머지 변수는 감소) 그리고 무상관 (두 변수 간 상관성이 없음)을 나타냄.
    >3.Pair Plot: 비교하려는 변수가 2개 이상일 때 유용함


```python

```


```python

```
