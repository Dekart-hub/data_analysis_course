import pandas as pd

import random, string

#Функция для генерирования строки длины <length> со случайными символами
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

#Задача 1
#Читаем файл в датафрейм df и выводим его
df = pd.read_csv("dataset/sgemm_product.csv")
print(df)

#Задача 2
#Выводим первые 5 элементов dataframe
print(df.head())

#Задача 3
#Выводим последние 5 элементов dataframe
print(df.tail())

#Задача 4
#Выводим первые 20 элементов dataframe
print(df.head(20))

#Задача 5
#Выводим колонку 'NWG' 2-мя разными способами
print(df.NWG)
print(df['NWG'])

#Задача 6
#Добавление новой колонки, сгенерированной из существующих
df['Total Runtime'] = df['Run1 (ms)'] + df['Run2 (ms)'] + df['Run3 (ms)'] + df['Run4 (ms)']
print(df)

#Задача 7
#Переименовывание колонок (без сохранения в dataframe)
df.rename(columns={
    'Run1 (ms)': 'run1',
    'Run2 (ms)': 'run2',
    'Run3 (ms)': 'run3',
    'Run4 (ms)': 'run4'
})

#Задача 8
#Переименовывание колонок (сохраненяя в dataframe)
df.rename(columns={
    'Run1 (ms)': 'run1',
    'Run2 (ms)': 'run2',
    'Run3 (ms)': 'run3',
    'Run4 (ms)': 'run4'
}, inplace=True)
print(df)

#Задача 9
#Сохранение dataframe(df) в csv файл; чтение из этого файла в новый dataframe(df2)
df.to_csv('newcsv.csv', index=False)
df2 = pd.read_csv('newcsv.csv')
print(df2)

#Задача 10
#Вывод dataframe с фильтром
print(df[df.run1 < 100.00])

#Добавление колонки со случайноыми строковыми значениями, т.к. в исходном наборе данных такой не было
#Но по заданию таковая требуется
rndStr = ''
for i in range(len(df.index)):
    rndStr += randomword(4) + ' '
df.insert(len(df.columns), 'strcol', rndStr.split())

#Задача 11
#Прмиенение 2-ух фильтров к dataframe (строковый и численный)
df2 = df[(df.run1 > 100.00) & (df.strcol.str.contains('a'))]
print(df2)
#Сохранение dataframe с применёнными фильртами в файл
df2.to_csv('filteredds.csv')

#Задача 12
#Считывание таблицы с сайта
df_web = pd.read_html('https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics')
print(len(df_web))

#Задача 13
#Вывод таблицы
print(df_web[0])
