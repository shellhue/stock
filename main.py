import pandas
from item_name import ItemName

df = pandas.read_csv('data/zcfzb000002.csv', index_col='报告日期')

print(df.columns)
for i in df.index:
    print(i)