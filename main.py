import pandas as pd

import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

#Читаем файл в датафрейм df и выводим его
df = pd.read_csv("dataset/sgemm_product.csv")
print(df)

print(df.head())

print(df.tail())

print(df.head(20))

print(df.NWG)
print(df['NWG'])

df['Total Runtime'] = df['Run1 (ms)'] + df['Run2 (ms)'] + df['Run3 (ms)'] + df['Run4 (ms)']
print(df)

df.rename(columns={
    'Run1 (ms)': 'run1',
    'Run2 (ms)': 'run2',
    'Run3 (ms)': 'run3',
    'Run4 (ms)': 'run4'
})

df.rename(columns={
    'Run1 (ms)': 'run1',
    'Run2 (ms)': 'run2',
    'Run3 (ms)': 'run3',
    'Run4 (ms)': 'run4'
}, inplace=True)
print(df)

df.to_csv('newcsv.csv', index=False)
df2 = pd.read_csv('newcsv.csv')
print(df2)

print(df[df.run1 < 100.00])

rndStr = ''
for i in range(len(df.index)):
    rndStr += randomword(4) + ' '
df.insert(len(df.columns), 'strcol', rndStr.split())
df2 = df[(df.run1 > 100.00) & (df.strcol.str.contains('a'))]
print(df2)
df2.to_csv('filteredds.csv')

df_web = pd.read_html('https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics')
print(len(df_web))

print(df_web[0])
