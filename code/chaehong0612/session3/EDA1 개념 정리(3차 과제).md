# Feature의 분석 및 시각화


시각화를 통해서 더 많은 양의 데이터를 효과적으로 확인할 수 있다  
요약 통계보다 더 정확한 데이터 분석 결과를 도출할 수 있다.  

## Feature의 여러가지 종류

**범주형(명목형)데이터(Categorical Features)**  

- 종류를 표시하는 데이터를 의미  
- 범주형 데이터 중에서 명목형 데이터는 순서가 없다.  

**순서형 데이터(Ordinal Features)**  

- 범주형 데이터 중에서 순서를 가지는 데이터 

**연속형 데이터(Continuous Feature)**  

- 연속적인 값을 가진 데이터  
- 끊기지 않고 연속된 데이터를 연속형 데이터라고 함  

**이산형 데이터(Discrete Feature)**  

- 정수 단위로 값이 끊기는 데이터  


## 시각화의 기본 표현

Figure : 그래프를 그리는 바탕, 도화지를 의미 (figure: plt.gcf())  
Size 조절 : fig.set_size_inches  
Axes: plot이 그려지는 공간
Axis: plot의 축

## 데이터에 따라서 사용하는 시각화 방법이 다르다

분석할 데이터가 어떤 데이터인지 유형을 파악하고, 이후에 어떤 플롯을 사용해 시각화 할지를 결정한다.  

시간에 따른 변화를 나타낼 때 :  line, area, bar  
비교와 랭킹을 나타낼 때 :  bar  
연관성을 나타낼 때 :  scatter  
분포를 나타낼 때 : box plot, histogram  
부분이 전체에 차지하는 정도를 알고 싶을 때 :  pie, bar

## 라이브러리

일반적으로 EDA를 할 때 Matplotlib과 Seaborn을 사용한다.  
자신이 사용하기에 편리한 라이브러리를 선택하면 된다.  

- Matplotlib :  Python 프로그래밍 언어, 수학적 확장 NumPy 라이브러리를 활용한 플로팅 라이브러리
- Seaborn :  matplotlib을 기반으로 만들어진, 통계 데이터 시각화에 최적화된 인기 라이브러리

# 수치형 데이터의 시각화


## 히스토그램

수치형 데이터의 구간별 빈도수를 나타낸 그래프 : **sns.histplot(x='age',data = data)**  


## 커널밀도추정 함수 그래프  

히스토그램을 매끄럽게 곡선으로 연결한 그래프 : **sns.kdeplot(x='age', data=data)**  


## 막대 그래프  

범주형 데이터 값에 따라 수치형 데이터 값이 어떻게 달라지는지 파악할 때 사용 : **sns.barplot(x='class',y='fare', data=data)**  


##  포인트플롯  

막대 그래프와 모양은 다르지만 동일한 정보를 제공 : **sns.pointplot(x='class', y='fare', data=data)**  


## 박스플롯  

막대 그래프나 포인트플롯보다 더 많은 정보, 구체적으로 5가지 요약 수치를 제공 : **sns.boxplot(x='class', y='age', data=data)**  

- 제 1사분위 수(Q1) : 전체 데이터 중 하위 25%에 해당하는 값  
- 제 2사분위 수(Q2) : 50%에 해당하는 값(중앙값)  
- 제 3사분위 수(Q3) : 상위 25%에 해당하는 값  

## 바이올린 플롯  

박스 플롯과 커널밀도추정 함수 그래프를 합쳐 놓은 그래프 : **sns.violinplot(x='class', y='age', data=data)**  


## 카운트플롯  

**sns.countplot(x='class', data=data)**  


## 파이 그래프  

**plt.pie(x, labels=labels, autopct='%.1f%%')**  


```python

```
