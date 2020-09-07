import pandas as pd
import matplotlib.pyplot as plt

fig, axes= plt.subplots(nrows=2, ncols=2)

df = pd.read_csv('people_salary.csv')
print(df.columns)
print(df.head(5))
pd_plt = df.plot(kind='scatter',x='age', y='salary',ax=axes[0,0])
pd_plt.set_ylabel('給料')
pd_plt.set_xlabel('年齢')
pd_plt.set_title('散布図')

#棒グラフ
average_by_countries = df.groupby(['country']).mean()
print(average_by_countries.head(5))
average_by_countries.plot(kind='bar',y='salary', title= '国ごと平均給料',ax=axes[1,0],color='red')


#ヒストグラフ
engineer_in_japan = df.loc[(df['country']== 'japan')\
                           & (df['job'] == 'Engineer')]
engineer_in_japan['age'].plot(
    kind='hist',ax=axes[0,1],title='日本のエンジニアの年齢分布')

#折れ線グラフ
engineer_in_japan.groupby(['age']).mean().plot(kind='line',y='salary',ax=axes[1,1])
plt.show()
