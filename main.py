import pandas as pd

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
