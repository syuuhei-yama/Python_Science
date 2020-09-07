import pandas as pd

df = pd.read_csv('people.csv')

print(df.head(3))
print(df.tail(3))

print(df.columns)

print(df[['first_name','last_name']][0:5])

print(df.iloc[1:4,5:10])

pd.set_option('display.max_columns', None)
print(df.loc[df['first_name'] == 'Michael'])
print(df.loc[df['first_name'] == 'Michael'].to_csv('output.csv',index=False, sep='\t'))

print(df.sort_values(['first_name','last_name'], ascending=[1,0]).\
                     head(20)[['first_name','last_name']])

#集計
print(df.describe())
print(df.age.sum())
print(df.age.min())
print(df.age.agg(['sum','max','mean']))

print("###########")

#絞り込み

print(df.head(5))
print(df.loc[df['first_name'].str.contains('Mi')])
print(df.loc[~df['first_name'].str.contains('Mi')])


print('-' * 100)

print(df.loc[df['first_name'].str.contains('William|Richard')])
print(df.loc[df['first_name'].str.contains('^A[a-z]*')])
print(df.loc[df['first_name'].str.contains('^A[a-z]*a$')])


df.loc[df['country'] == 'Japan','nationality'] = 'Japanese'
print(df.loc[df['country'] == 'Japan'])
print(df.head(3))

#group by

print(df.groupby(['country']).mean().sort_values('age'))





