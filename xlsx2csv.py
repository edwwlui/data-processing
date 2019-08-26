import pandas as pd
map=pd.read_excel('JPM fund.xlsx')
#first=pd.read_csv('first.csv')
files=[]
files.append('JPMAM-HistoricalPrice(LU0945454980).xlsx')
for file in files:
  df=pd.read_excel(file,skiprows=6)
  print(df)
  df=df[['Date','Nav']]
  print(file[-13-5:-1-5])
  SecId=map[map['ISIN']==file[-13-5:-1-5]]['SecId'].item()
  df=df.rename(columns={'Nav':SecId})
  df.to_csv('first.csv',index=False)
  #first.join(df.set_index('Date'), on='Date')
#first.to_csv('final.csv',index=False)
