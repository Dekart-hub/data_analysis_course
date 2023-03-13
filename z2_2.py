import pandas as pd
import matplotlib.pyplot as plt
import os

def random_dates(start, end, n=10):

    start_u = start.value//10**9
    end_u = end.value//10**9

    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')

df = pd.read_csv('dataset/sgemm_product.csv')
print(df.shape[0])

num = 1
for i in range(0, df.shape[0], 50_000):
    tmp = df.loc[i:i + 50_000 - 1]
    tmp.to_csv(f'parts/part_{num}.csv', index=False)
    num += 1

df_merge = pd.DataFrame()
for f in os.listdir('parts/'):
    tmp = pd.read_csv('parts/' + f)
    df_merge = pd.concat([df_merge, tmp])
print(df_merge)

df_merge.reset_index(inplace=True, drop=True)
print(df_merge)

df = df \
    .groupby(['MWG', 'NWG', 'KWG', 'MDIMC', 'NDIMC', 'MDIMA', 'NDIMB', 'KWI', 'VWM', 'VWN', 'STRM', 'STRN', 'SA', 'SB'],
             as_index=False) \
    .agg({'Run1 (ms)': 'sum',
          'Run2 (ms)': 'count'}) \
    .rename(columns={
        'Run1 (ms)': 'total time',
        'Run2 (ms)': 'number'
    }) \
    .sort_values('total time', ascending=False)
df.to_csv('group.csv')
print(df)

print(df.info)

start = pd.to_datetime('2015-01-01')
end = pd.to_datetime('2018-01-01')
df.insert(len(df.columns), 'date', random_dates(start, end, df.shape[0]))
print(df)

df['day name'] = df.date.dt.day_name()
print(df)

df_tmp = df.groupby('day name').count().rename(columns={'date': 'count'})
print(df_tmp)

diag = plt.bar(df_tmp.index, df_tmp['count'])
plt.show()
