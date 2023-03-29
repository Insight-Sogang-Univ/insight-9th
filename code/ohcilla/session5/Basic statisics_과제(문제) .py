#!/usr/bin/env python
# coding: utf-8

# # 통계 세션 과제!

# ## 과제 1
# - list_A와 list_B 각각의 평균, 분산, 중간값을 구하시오
# - list_A와 list_B의 공분산, 상관계수를 구하시오
# <br><br>HINT!
# <br>1. 공분산, 상관계수 구할때 둘을 합쳐서 데이터프레임으로 만들고 해보세요!
# <br>2. 공분산과 상관계수는 어떤 값이지 데이터프레임 형태가 아닙니다!

# In[18]:


import pandas as pd
list_A = [10, 3, 6, 17, 12, 1, 14, 19, 7, 15, 3, 4, 15, 8, 5, 13, 11, 2, 20, 16]
list_B = [17, 2, 6, 14, 10, 16, 1, 8, 3, 7, 7, 12, 20, 18, 4, 11, 5, 19, 15, 9]
a = {"list_A" : list_A, "list_B" : list_B}
df = pd.DataFrame(data = a)
print(df)


# In[22]:


from statistics import mean, variance, median
print(mean(list_A))
print(mean(list_B))
print(variance(list_A))
print(variance(list_B))
print(median(list_A))
print(median(list_B))
print(df.cov())
print()
print(df.corr())


# ## 과제 2
# - 표본집단의 크기가 커지면 그 표본평균이 모평균에 가까워지는 현상을 무엇이라고 하나요?

# In[ ]:


중심 극한 정리(CLT : Central Limit Theorem)


# ## 과제 3
# - 이산확률분포 예시 1개, 연속확률분포 예시 1개를 적어주세요!
# 1. 사과의 개수
# 2. 사람의 키

# 

# ## 과제 4
# OX문제
# - 3-(1)번 : 귀무가설이 참임에도 거짓이라고 판단하는 오류를 제 2종 오류라고 한다 (O / X)
# - 3-(2)번 : 모집단이 이항 분포일때 그 모집단에서 추출한 표본 10000개의 각 평균들이 이루는 분포는 이항분포이다. (O / X)
# - 3-(3)번 : 검정 통계량 T가 매우 크면 귀무가설을 기각한다 (O / X)
# - 3-(4)번 : 1종 오류를 작게끔 설정하면 2종 오류가 커진다 (O / X)
# - 3-(5)번 : p-value가 유의수준보다 크면 귀무가설을 기각한다  (O / X)

# In[ ]:


1. x
2. x
3. x
4. o
5. x


# ## 과제 5
# - 아래 코드의 결과대로면 광고 전략은 실패했는지, 실패하지 않았는지 검정하시오

# In[23]:


import numpy as np
import scipy.stats as stats

# 실험 데이터 생성 
np.random.seed(42)
data = np.random.normal(loc=2, scale=1, size=50)

# 귀무가설(H0) : 광고 전략이 실패한 것이 아니다
# 대립가설(H1) : 광고 전략이 실패했다

# 유의수준 설정
alpha = 0.01

# 검정 통계량 계산
t_stat, p_value = stats.ttest_1samp(data, 1.5)
print(f't_stat : {t_stat}, p_value : {p_value}')


# In[ ]:


t_stat > p_value => reject H0

