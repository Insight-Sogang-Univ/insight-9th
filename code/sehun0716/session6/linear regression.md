# House Sales in King Country, USA

- 중간값: median
- 결측치: null
- 왜도: skewness
- 첨도: kurtosis

- df['price'].hist()를 했을 때, 한쪽으로 치우쳐 있을 경우, 자연로그를 활용하여 분포를 조정할 필요가 있음
- np.log(df['price']).hist()

- date column 을 앞에서 4자리만 추출하고 type를 int64로 변경하고 column명을 date2로 저장하기
- df_obj['date2'] = df_obj['date'].apply(lamda x: x[0:4])
- lamda: 한 줄짜리 함수가 완성됨

- 종속변수(price)와 선형 관계가 있을 것 같은 독립 변수들을 선정하여 **산점도(scatter plot)** 그래프를 그려보기
    - 산점도를 통해서 종속 변수와 독립 변수들 사이의 선형 관계를 대략적으로 파악 가능
- 히트맵을 통해 종속 변수와 상관관계가 높은 변수들 확인 가능

- 설명 변수(x)1개, 반응 변수(y) 1개일 때 사용하는 대표적인 방법론: 단순 선형 회귀분석
- 종속변수와 가장 상관관계가 높은 변수를 독립 변수로 단순 선형 회귀 분석을 실시

- 회귀분석을 할 때는 항상 상수항을 추가해야 함
- add_constant 함수를 활용해 상수항을 추가 
- ex) x = df[['sqft_living']]
y = df[['price']]<br>
x = sm.add_constant(x, has_constant="add")

- Dep.varialbe: 종속 변수, 타겟값
- model: 학습 모델 / OLS(ordinary least squares), 잔차 제곱합(손실)을 최소로 하는 파라미터를 선택하는 방법
- method: Least Squeares / 잔차 제곱합(손실)을 최소로 하는 파라미터를 선택하는 방법
- No.Observation: 데이터 셋의 크기
- Df Residuals: 데이터 셋의 크기 - 추정된 파라미터 수를 뺀 것
- Df Model: 독립 변수의 숫자
- Df Model: 독립 변수의 숫자
- Covariance Type: 공분산의 종류
- R-squared: 결정계수
- Adj. R-squared: 조정된 결정계수
- Std.error: 계수의 표준 오차
- F-statistic: F value
- Prob (F-statistic): p-value
- Log-Likehood: 최대 로그 우도
- Coef: 계수값
- P>|t|: p-value

- P>|t|(p-value) 항목의 유의 확률이 유의 수준 0.05 보다 훨씬 작아 유의 수준 0.05 이하에서 귀무 가설은 기각 됨
- 모형 통계학적 유의성이 확보됨

## 다중 선형 회귀
연속형 반응 변수 하나에 설명 변수가 둘 이상인 모형<br>
    - 다중공선성 문제와 차원의 저주 문제 등을 고려해야 함<br>
    - 단순 선형 회귀와 달리 다중 선형 회귀분석에서는 모든 변수의 다중공선성 문제를 확인해야 함<br>
        - 설명 변수가 다수이기 때문에 모형에 포함된 설명 변수의 정보가 중첩(상관관계를 가짐)으로, 다중공선성 문제가 발생하는 것을 확인 가능

## 회귀 모형의 가정 진단
회귀 모형은 반응 변수와 설명 변수의 선형 관계를 전제로 함<br>
오차에 대한 독립성, 정규성, 등분산성 가정을 전제로 함

# 느낀점 및 새로 알게된 점 
    1. 회귀 분석의 개념을 이해하는 것이 쉽지 않은 것을 많이 느낀 것 같습니다.
    2. 주요하게는, 상관관계가 존재한다고 해서 이것만으로 유의미하게 끌고 가면 안되고, 명확한 인과관계가 존재하는지, 설명변수와 반응 변수 간에 관계를 살펴보고, 최대한 오차를 줄여나가야 하며, 다중 공선성, 차원의 문제 등을 고려해야 한다는 점을 알게되었습니다.
