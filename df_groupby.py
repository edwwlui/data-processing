import pandas as pd
df=pd.read_csv('tb_col_name.csv',header=None)
df_groupby=df.groupby([0,2,3,4])
for key, item in df_groupby:
    cols=df_groupby.get_group(key).head(1)[[0,2,3,4]].astype(str).values.tolist()[0]
    files=item[5].to_list()
    print(cols+files)
    with open('tb_col_file.csv','a') as fo:
         fo.write('\t'.join(cols+files)+'\n')
