# 1번
import numpy as np
import pandas as pd
from scipy import stats

#H0 : 𝜇 = 6300
#H1 : 𝜇 ≠ 6300

data = pd.read_excel("C:/Users/jwoo9/기타/Downloads/S기업_점심비용.xlsx")
mu=6300
n=data.size #100

t = (np.mean(data)-mu) / (np.std(data,ddof=1) / np.sqrt(n))
p = 1-stats.t.cdf(t, n-1)
print('p값=',p) #0.11가 나왔는데 양측이므로 나중에 2*p=0.22와 알파 비교해야

result = stats.ttest_1samp(data.lunch,mu,alternative='two-sided') #양측
print(result)

if 2*p<0.05: print('H0기각')
else : print('H0를 기각할 수 없음')