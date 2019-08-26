import pandas as pd
map=pd.read_excel('JPM fund')
files=[]
for file in files:
  df=pd.read_excel(file,skiprows=5)[['Date','Nav']]
  df.rename({'Nav':map[map['ISIN']==file[-11:-1]]['SecId']})
  first.join(df.set_index('Date'), on='Date')
first.to_csv('final',index=False)
