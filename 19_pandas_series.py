#9/2

import pandas as pd
import numpy as np

sr1 = pd.Series(['A','B','C','D'])
print(sr1)
print(list(sr1))
print(tuple(sr1))

#インデックスを指定
sr = pd.Series([23,24,22,21],
    index= ['Taro','Jiro','Hanako','Yoshiko']
)
sr = pd.Series(
    {
        'Taro':23,
        'Jiro':24,
        'Hanako':22,
        'Yoshiko':21
    }
)
print(sr)


# append
sr2 = pd.Series({'Saburo': 20})
sr = sr.append(sr2)

print(sr)

print(sr.values)
print(sr.index)
filter = sr > 22
print(sr[filter])

sr.name = '年齢'
sr.index.name = '名前'
print(sr)

sr1 = pd.Series(np.random.randint(0,10,10))
sr2 = pd.Series(np.random.randint(0,10,10))
print(sr1)
print(sr1.unique())
print(sr1.value_counts())


print(sr1 + sr2)

##########

sr1 = pd.Series(['A','B','C','D'])
sr1[1:] = ['E','F','G']
print(sr1)

sr1 = sr1.drop(1)
print(sr1)

sr1.reset_index(drop=True, inplace=True)
print(sr1)

sr1 = pd.Series(np.random.randint(0,10,10))
print(sr1)
sr1[5] = pd.NA
print(sr1)

print(sr1[~sr1.isna()])

#統計処理
print(sr1.count())
print(sr1.mean())
print(sr1.max())
print(sr1.var())
print(sr1.std)
print(sr1.quantile(0.8))
print(sr1.min())

print(sr1.describe())