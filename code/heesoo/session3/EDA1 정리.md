# EDA1 정리

1. Feature 분석 및 시각화
    
    -데이터 유형에 따라 다양한 시각화 방식 사용(-> 많은 양의 데이터 다양한 시각화 방식 사용)
    
    -결측치 처리
    
    -요약 통계보다 더 정확한 데이터 분석 결과 도출 가능
    > *명목형 자료: bar plot, count plot, pie chart
    
    > *자료 개형: histogram, box plot, stem and leaf plot
    
    > *시계열 및 변수 간 관계: time series plot, scatter plot
    

2. Feature의 종류

    -categorical feature (범주형, 명목형): 
    범주형 데이터는 'A', 'B', 'C'와 같이 종류를 표시하는 데이터이며 그 중 명목형 데이터의 경우에는 순서가 없다. 
    
    -Ordinal feature (순서형): 
    범주형 데이터 중에 순서를 가지는 데이터
    
    -continuous feature (연속형): 
    키와 같이 값이 끊기지 않고 연속되는 데이터 
    
    -discrete feature (이산형):
    사과 개수나 책의 페이지 수와 같이 값이 딱 정수 단위로 끊기는 데이터
    

3. 시각화 기본 표현

    -feature: 그래프를 그리는 바탕, 도화지
    
    * figure을 그린다-> plt.subplots로 각 부분에 그래프를 그려 바탕을 분할
    * plt.figure를 직접적으로 적어주는 것이 확실하지만 적지 않는 경우에도 자동으로 생성
    * 현재 figure: plt.gcf()
    
    -size 조절: fig.set_size_inches(18.5, 10.5)
    
    * 또는 plt.figure(figsize=(10,5))
    * 또는 plt.rcParams['figure.figsize']=(10,7)
    
    -Ases : plot이 그려지는 공간
    -Axis: plot의 축
    

4. 데이터 별 시각화 사용

    1. 분석할 데이터가 어느 수치형 Numeric 데이터인지 categorical 데이터인지 확인 (+ 빠진 데이터 유무)
    2. attributes 파악 후 데이터 성질을 고려해 어떤 플롯 사용할 지 고민
    
    >EX)
    >* 시간에 따른 변화 -> line, area, bar
    >* 비교와 랭킹 -> bar
    >* 연관성 -> scatter 
    >* 분포 -> box plot, histogram
    >* 부분이 전체에 차지하는 정도 -> pie, bar
    

5. Matplotlib

    -일반적으로 EDA 시, Matplotlib, Seaborn 사용
    -파이썬 프로그래밍 언어 및 수학적 확장 Numpy 라이브러리 활용 플로팅 라이브러리
    

6. Seaborn

    -seaborn 라이브러리 seaborn은 matplotlib를 기반으로 만들어져 통계 데이터 시각화에 최적화된 라이브러리
    

7. 수치형 데이터 시각화

    -히스토그램: 수치형 데이터의 구간별 빈도수를 나타낸 그래프
    
    -커널밀도추정 함수 그래프: 히스토그램을 매끄럽게 곡선으로 연결한 그래프
    
    -막대 그래프: 범주형 데이터 값에 따라 수치형 데이터 값이 어떻게 달라지는지 파악 시 사용
    
    -포인트플롯: 막대 그래프와 모양만 다를 뿐, 동일한 정보 제공
    
    -박스 플롯: 막대 그래프나 포인트 플롯보다 더 많은 정보(5가지 요약 수치) 제공
    제 1사분위 수(전체 데이터 중 하위 25%), 제 2사분위 수(50%에 해당하는 중앙값), 제 3분위 수(상위 25%에 해당하는 값)
    
    -바이올린 플롯: 박스 플롯과 커널밀도추정 함수 그래프를 합쳐놓은 그래프
    
    -카운트플롯
    
    -파이 그래프
    
    
    
    
    


```python

```


```python

```
