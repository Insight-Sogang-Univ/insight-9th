# EDA2 정리
## INTRO
- 데이터 분석은 4가지로 나뉜다.
> Optimization: 문제도 알고, 분석 방법도 앎  
> Solution: 문제는 알지만 방법을 모름  
> Insight: 기존의 분석방법은 알지만 대상을 모름  
> Discovery: 문제도 모르고 방법도 모름
- 우리는 여기서 인사이트의 발견에 집중한다.

## 주로 사용되는 4가지 라이브러리
```python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
```

## 다양한 기법 정리

### 한 화면에 그래프 여러개 띄우기
1. fig, ax 이용
```python
    fig, ax = plt.subplots(n_rows, n_cols, figsize = (A, B)) # n_rows*n_cols 개의 그래프 생성
    fig.suptitle("title") # 전체 타이틀
    
    # [m,n]에 위치한 그래프에 대한 설정
    ax[m,n].bar(x, y) # 그래프 종류에 따라 . 뒤에 오는게 달라짐!
    ax[m,n].set_title('sub_title') # 작은 title
    ax[m,n].legend() # 범례 설정
```
2. plt.subplot 이용
```python
    plt.subplot(n_rows, n_cols, num) # n_rows*n_cols 개의 그래프 중에 num번째 설정 가능
```

### 파이차트 (pie chart)
```python
    data['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', shadow=True, fontsize=20)
    plt.pie(data["Survived"].value_counts(),~~~)
```

### Count Plot
```python
    sns.countplot(x="Survived", data=data)
```

### 막대 그래프 (수평)
```python
    data[['Sex', 'Survived']].groupby(['Sex']).mean().plot.barh()
```

### 크로스탭 (crosstab)
```python
    pd.crosstab(data.Pclass, data.Survived, margins=True) # 시각화 전에 숫자로 보기 좋음
```

### Cat Plot
```python
    sns.catplot(x="", y="", kind="point" or "box", data=data) # factor plot 대신 하면 point
```

### Violin Plot
```python
    sns.violinplot(x="", y="", hue="", data=data) # hue를 주면 색깔로 나뉜다
```

### 히스토그램 (Histogram)
```python
    data[data['Survived'] == 0].Age.plot.hist(bins=20, edgecolor='black', color='red')
    sns.histplot(data=data, x = "")
```

## 확인해야 할 거
### heatmap
```python
    sns.heatmap(data.corr(), annot=True) # 변수들의 상관관계를 확인 할 수 있다. -> 너무 높으면 다중공선성 생각하기!
```

## 데이터 변환
### 연속형 변수 -> 범주형 변수
```python
    data["new"] = pd.qcut(data["continual"], n) # n개로 나눠준다
```

### 문자열 -> numeric
```python
    data[""].replace(['A', 'B'], [0,1], inplace = True)
```














