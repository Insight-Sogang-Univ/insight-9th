### 느낀점
- 다중 선형 회귀 분석에서는 다중공선성 문제를 모든 변수에서 꼭 확인해봐야겠다!
- 모형의 유의성과 계수의 유의성이 확보되었어도 오차에 대한 가정까지 만족하는지 확인해야겠다! 아니라면 다른 대안을 찾아야 한다.

### 새로 알게 된 점
- 왜도, 첨도
```python
df[val].skew()    
df[val].kurtosis()
```      

- 히트맵에서 반대쪽 삼각형 안 보이게 설정
```python
np.triu_indices_from(mask)
```   
- 선형 모델에 적합시키기
```python
fit()
```
- 다중 선형 회귀분석 
변수들 많이 선별해서 회귀분석 해보고 괜찮은 것을 고르는 게 좋음
- 용어 정리    
R-squared : 결정계수, 1에 가까울 수록 모델의 설명력이 높음 
Adj.R-squared : 조정된 결정계수     
Log-Likelihood : 최대 로그 우드     
아카이케 정보 기준 :  모델의 성능 지표로 작을수록 좋은 모델    
Coef : 계수값     
P>|t| : p-value    

- 정규성 검정 Q-Q 도표
```python
sm.qqplot()
```
- 샤피로-월크 검정
```python
stats.shapiro()
```

