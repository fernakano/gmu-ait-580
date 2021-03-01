import pandas as pd

df_nasdaq_list = pd.read_csv('nasdaqlisted.txt', delimiter='|')
df_other_list = pd.read_csv('otherlisted.txt', delimiter='|')
df_wsb = pd.read_csv('reddit_wsb.csv')

df_nasdaq_list[['Symbol', 'Security Name']].describe()
df_other_list[['ACT Symbol', 'Security Name']].describe()

df_other_list.rename(columns={'ACT Symbol': 'Symbol'}, inplace=True)
stocks = pd.concat([df_nasdaq_list[['Symbol', 'Security Name']], df_other_list[['Symbol', 'Security Name']]])

print(stocks.describe(include='all'))
print(df_wsb[['title', 'body', 'timestamp']].describe().to_string(max_cols=df_wsb.shape[1]))

