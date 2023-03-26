# EDA란?

-**EDA(Exploratory Data Analysis, 탐색적 데이터 분석)** 란, 데잍의 특징과 내재하는 구조적인 관계를 알아내기 위한 분석 기법
- 데이터를 직관적으로 바라보기 위한 *통계적 방법과 데이터 시각화* 사용
- EDA를 통해 문제에 대한 통찰을 얻고 향후 분석의 방향을 설정
- EDA 순서:
    1) 데이터 및 결측치 확인
    2) Feature 분석 및 시각화
    3) Feature Engineering과 Data Cleaning
- 본 NoteBook에서는 Tabular data 유형의 'Titanic'을 활용
    
## 데이터 및 결측치 확인
1. 라이브러리 및 파일 불러오기
2. 결측치 확인
    - 데이터 분석에 본격적으로 들어가기 전, 데이터에 결측치(null)가 있는지 확인 후 처리
    - Titanic 데이터 셋에서 결측치가 존재하는 Age, Cabin, Embarked에 대해 각각의 feature를 고려해 처리
   
## Feature 분석 및 시각화

- feature 별 데이터 유형에 따른 시각화 및 결측값 채우기

    1) Survived(생존자 수)
    - PieChart, CountPlot으로 시각화
    - 총 891명의 승객들 중, 350명(38.4%)만이 생존
    
    2) Sex(생존자 성별)
    - 탑승객의 수는 남자가 여자보다 훨씬 많음
    - 하지만, 생존한 수는 여자 승객이 남자 승객보다 거의 두배 많음
    - 여성의 생존율은 약 75%인 반면, 남자는 18-19%
    
    > **주의해야 할 통계지식**: 통계에서 종종 상관관계를 인과관계로 잘못 해석하는 오류를 범하는데, 상관관계는 인과관계를 의미하지 않는다.  
    상관관계: X와 Y, 두 가지 사건에 연관성이 존재하는 상태  
    인과관계: 'A하면 B하다'와 같이 특정한 사건이 다른 사건에 직접적으로 영향을 주는 상태
    
    
    3) Pclass(범주형, 명목형 변수)
    - Pclass 1의 승객들이 생존율이 대략 63%로 가장 높음, Pclass2는 대략 48%
    - 탑승객 수는 Pclass3가 가장 많지만, 이에 비해 Pclass3 생존자는 매우 적음
    - Sex와 Pclass를 crosstab을 통해 살펴보면, Pclass1의 여성 승객 생존율이 대략 95%로 매우 높다는 것, Pclass와 무관하게 전반적인 여성의 생존율이 높다는 것을 알 수 있음
    
    4) Age(연속형 변수)
    - Violin Plot으로 생존 여부에 따른 Pclass별 Age의 분포를 살펴보면, Pclass가 증가할수록 아이들의 수가 많고,  Pclass와 관계없이 10살 이하 승객들의 생존율이 높은 것을 확인
    - Violin Plot으로 생존 여부에 따른 Sex별 Age의 분포를 살펴보면, 60대 이상 남성들의 사망률이 높은 것을 확인할 수 있음
    - Age 결측값 처리: Name feature를 활용해 범주형 feature를 추가하고, 각 그룹별 연령의 평균을 구해서 결측값 채우기
    
    5) Embarked(범주형, 명목형 변수)
    - Port S의 탑승객이 가장 많고, Pclass3/남성 승객의 비율이 높아 생존율이 가장 낮음
    - Port C는 Pclass1, 2의 승객 비율이 높아 생존율이 높음
    - Port Q는 95%가 Pclass3 승객
    - Embarked 결측값 처리: 최빈값이 S로 결측치 대체
    
    6) Sibsp(이산형 변수)
    - 형제/배우자가 없는 탑승객의 생존율은 대략 34.5%
    - 형제의 수가 증가할수록 생존율이 떨어짐, 이는 Sibsp > 3이 모두 Pclass3 이기 때문
    - 형제/배우자가 없는 탑승객보다 1-2명인 탑승객의 생존율이 높음
    
    7) Parch(이산형 변수)
    - 부모/자녀와 함께 탑승한 고객들은 혼자 탑승한 고객보다 높은 생존율
    - 대가족이 Pclass3에 많이 존재하므로 4명 이상의 부모/자녀와 탑승할 때, 생존율 감소
    
    8) Heatmap
    - feature들 간의 상관관계를 열분포 형태의 비주얼그래픽으로 출력
    - 구체적인 수치 없이도 데이터가 시사하는 바를 패턴으로 효과적으로 시각화
    - string이 아닌 numeric feature에 대해서만 상관관계 분석 가능
    - 다중공선성: 두 변수의 상관관계가 매우 높아 두 변수가 거의 동일한 정보를 갖고 있다는 상태
        - 모델 학습 시, 다중공선성을 띄는 변수들 중 불필요한 변수 제거 필요
    
    
    
## Feature Engineering & Data Cleaning

1. Feature Engineering: 초기 데이터의 특징을 가공/생산해 모델의 입력 데이터를 생성하는 과정
    - 문자보다는 숫자, 개별값보다는 범위로 데이터 가공 필요

    1) Age_band
    - 연속형 변수는 모델링 시 문제가 발생하므로, 연속형 feature인 Age를 Binning 해서 새로운 범주형 변수를 생성
    - Age의 범위인 0-80을 5개의 범주로 나눠, 사이즈가 16인 bin 5개 생성
    
    2) Family_Size와 Alone
    - Parch와 SibSp feature를 합쳐 새로운 feature 생성
    - Family_Size는 Parch와 SibSp를 더해 생성
    - Alone은 Family_Size가 0인 행들에 대해 data['Alone']=1
    - alone이거나 family_size >=4 일때 생존율 감소
    
    3) Fare_cat
    - 연속형 변수 Fare를 4개의 구간으로 나눠 순서형 변수로 변환
    - Fare_cat이 증가할수록, 생존율 증가
    
    4) Converting String values into Numeric
    - string을 머신러닝 모델에 사용할 수 없으므로 numeric 값으로 변환: 'Sex', 'Embarked', 'Initial' 
    
    5) Dropping UnNeeded Features


## 시각화 기본 보충

1. Line Plot
- 연속적으로 변화하는 값을 순서대로 점으로 나타내고, 선으로 연결한 그래프
- 시간/순서에 대한 변화에 적합하여 추세를 살피기 위해 활용

2. Scatter Plot
- 데이터 포인트를 흩뿌려놓은 형태로, x축과 y축의 상관관계를 표현할 때 쓰임
- 양의 상관관계/음의 상관관계/무상관을 표시

3. Pair Plot/ Pair Grid
- 비교하려는 변수가 2개 이상일 때 유용
