# 시각화

## feature 의 종류
    크게 4가지 종류가 있다.
    1. Categorical Feature
     내용 : A,B,C 같은 범주형 데이터
    2. Ordinal Feature
     내용 : 범주형 데이터 중 순서가 있는 데이터
      ex) Height(Tall,Medium,Short)
    3. Continuous Feature
     내용 : 연속적인 데이터 ex) 나이
    4. Discrete Feature(이산형)
     내용 : 정수형으로 딱 끊기는 데이터
     
## 시각화 기본 표현
    1. Figure(도화지 역할)
     내용 : plt.subplots 으로 바탕을 분할하여 그래프 작성
    2. Size 조절 가능 
     by plt.figure(figsize(row,col))
    3. Axes : plot의 공간 조정, Axis = plot의 축
    
### 데이터 특성 파악
    1. 데이터의 성질을 파악하여 적합한 데이터 형태 사용하기
     ex) 시계열 분석 : line, area, bar
         연관성 : scatter
         등등
  
# 수치형 데이터 시각화

## 히스토그램 
    히스토그램은 기본적으로 수치형 데이터의 빈도를 나타냄
    x = '원하는 x파라미터', hue(y라 생각하면됨) : '원하는 y파라미터'
    
## 커널밀도추정 함수
    히스토그램을 매끄럽게 이은 곡선

## 막대 그래프(barplot)
    barplot을 이용하여 작성할 수 있음. 

## 박스 플롯(boxplot)
    박스 플롯은 구체적인 수치를 제공한다
    제 1사분위 수 : 하위 25퍼센트
    제 2사분위 수 : 50%에 해당하는 값(중앙값)
    제 3사분위 수 : 상위 25%에 해당하는값
 ## 바이올린 플롯, 카운트플롯, 파이 그래프 등등이 있다. 
