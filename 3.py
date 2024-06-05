import numpy as np
import pandas as pd
from scipy import stats

#H0 : 𝜇 = 68000
#H1 : 𝜇 > 68000

data = pd.read_csv("C:/Users/jwoo9/기타/Downloads/스마트폰_이용요금.txt", header=None)
mu=68000
n=data.size  #80

t = (np.mean(data)-mu) / (np.std(data,ddof=1) / np.sqrt(n))
p = 1-stats.t.cdf(t, n-1)
print('p값=',p) # 단측이므로 나중에 p와 알파 비교해야

result = stats.ttest_1samp(data,mu,alternative='greater')  #단측
print(result)

if p<0.05: print('H0기각')
else : print('H0를 기각할 수 없음')