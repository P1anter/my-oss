import numpy as np
import pandas as pd
from scipy import stats

#H0 : 𝜇 = 35
#H1 : 𝜇 ≠ 35

data = pd.read_csv("C:/Users/jwoo9/기타/Downloads/스마트폰_이용시간.csv", header=None)
mu=35
n=data.size  #40

t = (np.mean(data)-mu) / (np.std(data,ddof=1) / np.sqrt(n))
p = 1-stats.t.cdf(t, n-1)
print('p값=',p) # 양측이므로 나중에 2*p와 알파 비교해야

result = stats.ttest_1samp(data,mu,alternative='two-sided') #양측
print(result)

if 2*p<0.05: print('H0기각')
else : print('H0를 기각할 수 없음')