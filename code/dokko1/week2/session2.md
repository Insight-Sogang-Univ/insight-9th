# 읽기 및 전처리 예습

## 데이터 입출력
  1. 읽고 싶을 때는 read_file format, 쓰고 싶을 때는 write_file formoat 형태로 쓴다.
  2. **csv** 파일은 데이터의 크기가 작고 압축이 용이하기 때문에 가장 널리 사용되는 형식이다.
  3. excel은 판다스 형식으로 구체적인 col에 접근할 수 있다.





## 데이터 전처리
   전처리 순서는 크게 데이터 셋 확인 => 결측값 처리 => 이상값 처리 => Feature Enginerring 으로 진행된다. 

    1.데이터 셋 확인
        1) 유효값 갯수는 info() 메소드로 파악 
        2) Nan 값 개수는 value_counts(dropna=False), isnull(),not null 이용하여 확인. 보통 isnull.sum() 사용
        
    2.결측값 처리 
         1) dropna(axis=축 설정, thresh(임계치)) 삭제
         2) fillna를 이용하여 누락 데이터 대체 가능
         3) drop_duplicates를 이용하여 중복 제거
    
    3.이상값(Outlier) 처리
         1) df.describe()를 통해 확인하구
         2) 시각화 진행 후, 사분범위를 이용하여 Outliner 제거 

