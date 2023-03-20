# EDA 예습
## Feature
### Feature의 종류
1. Categorical Features(범주형, 명목형)
- 범주형 데이터는 'A', 'B',, 처럼 종류를 표시하는 데이터를 의미한다.
- 범주형 데이터중에 명목형 데이터는 데이터 간의 순서가 없다.

2. Ordinal Features(순서형)
- 범주형 데이터 중 순서를 가지는 데이터를 말한다.
- 명목형 데이터의 반대
- ex) Tall, Medium, Short

3. Continuous Feature(연속형)
- 연속적인 값을 가진 데이터
- 일반적으로 쓰는 float 데이터

4. Discrete Feature(이산형)
- 정수로 떨어지는, 셀 수 있는 데이터
- ex) 사과 개수, 책 페이지 수, 사람 수

## 시각화 기본 표현
- Figure: 그래프를 그리는 바탕
- Size: 바탕의 사이즈 조절
```python
    plt.figure(figsize = (10,8))
```
- Axes: plot이 그려지는 공간
- Axis: plot의 축

### 시각화를 할 때에는 Feature의 종류를 생각하고, 거기에 맞는 plot을 사용해야 한다.

## 주로 사용하는 plot
1. 시간에 따른 변화 -> line, area, bar
2. 비교, 랭킹 -> bar
3. 연관성 -> scatter
4. 분포 -> box plot, histogram

## Matplotlib vs Seaborn
- 본인이 편한 거 사용하기
1. 히스토그램
```python
    sns.histplot(x = "열", hue = "범주별"data = data)
```

2. 커널밀도추정 함수 그래프 - 히스토그램을 곡선으로 연결한 그래프
```python
    sns.kdeplot(x = "열", data = data)
```

3. 막대 그래프
```python
    sns.barplot(x = "x축", y = "y축", data = data)
```

4. 포인트플롯
```python
    sns.pointplot(x = "x축", y = "y축", data = data)
```

5. 박스플롯 -> 사분위수, 이상치
```python
    sns.boxplot(x = "x축", y = "y축", data = data)
```

6. 바이올린 플롯 -> 박스 플롯 + 밀도까지
```python
    sns.violinplot(x = "x축", y = "y축", data = data)
```

7. 카운트 플롯
```python
    sns.countplot(x = "x축", y = "y축", data = data)
```

(진도 외에 자료조사를 조금 해봤습니다!)
## EDA란 무엇인가
- EDA = 탐색적 데이터 분석
### 머신러닝 Work Flow에서의 EDA
- 보통 머신러닝 과제를 할 때에는 과제 정의 (데이터 분석 문제 정의) -> 데이터 수집 및 정제 -> 탐색적 데이터 분석 -> 예측 모델 개발+검증 순서로 진행되게 되는데, 우리가 이전에 한 전처리 등이 2번째 과정이고, EDA는 탐색적 데이터 분석 과정에 속하게 된다.
- 이 단계에서는 데이터의 크기등을 확인하고 서로의 관계를 확인할 수 있는 시각자료등을 제작하게 된다.
- 간혹 feature마다 높은 관계성을 보이거나 하면 모델에 안좋은 영향을 주기도 하기 때문에 시각화 후 drop하기도 한다. -> 다중공선성















