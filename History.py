#https://www.fantacalcio.it/statistiche-serie-a/2015-16/undefined/gol
#https://fbref.com/it/comp/11/Statistiche-di-Serie-A



import pandas as pd
import numpy as np
type_dict={'Id':'str','R':'str'}#'Mv':'float','Mf':'float'}#,'Nome':'str','Squadra':'str','Pg':'int',,'Mf':'float','Gf':'int','Gs':'int','Rp':'int','Rc':'int','R+':'int','R-':'int','Ass':'int','Asf':'int','Amm':'int','Esp':'int','Au':'int'}

header_list = ['Id','R','Nome','Squadra','Pg','Mv','Mf','Gf','Gs','Rp','Rc','R+','R-','Ass','Asf','Amm','Esp','Au']
header_list2= ['Id','R','Nome','Squadra','QtA','QtI','Diff']

def stfMv (a):
    a1=a.split(",")
    if(len(a1)==2):
        return float(a1[0]+"."+a1[1])
    elif(len(a1)==1): 
        return float(a1[0])

df1920=pd.read_csv("Statistiche_Fantacalcio_2019-20_Statistico.csv",sep=";",names=header_list,dtype=type_dict)
df1920['Gf']=df1920['Gf']+df1920['R+']
df1920['Ass']=df1920['Ass']+df1920['Asf']

df1920.drop(['Rp','Rc','R+','R-','Asf','Au'],axis=1,inplace=True)


df1920['Mv']=df1920.apply(lambda x: stfMv(x['Mv']), axis=1)
df1920['Mf']=df1920.apply(lambda x: stfMv(x['Mf']), axis=1)

df1819=pd.read_csv("Statistiche_Fantacalcio_2018-19_Statistico.csv",sep=";",names=header_list,dtype=type_dict)
df1819['Mv']=df1819.apply(lambda x: stfMv(x['Mv']), axis=1)
df1819['Mf']=df1819.apply(lambda x: stfMv(x['Mf']), axis=1)
df1819.rename(columns={'Mv':'Mv1819','Mf':'Mf1819'},inplace=True)


df1718=pd.read_csv("Statistiche_Fantacalcio_2017-18_Statistico.csv",sep=";",names=header_list,dtype=type_dict)
df1718['Mv']=df1718.apply(lambda x: stfMv(x['Mv']), axis=1)
df1718['Mf']=df1718.apply(lambda x: stfMv(x['Mf']), axis=1)
df1718.rename(columns={'Mv':'Mv1718','Mf':'Mf1718'},inplace=True)

df1617=pd.read_csv("Statistiche_Fantacalcio_2016-17_Statistico.csv",sep=";",names=header_list,dtype=type_dict)
df1617['Mv']=df1617.apply(lambda x: stfMv(x['Mv']), axis=1)
df1617['Mf']=df1617.apply(lambda x: stfMv(x['Mf']), axis=1)
df1617.rename(columns={'Mv':'Mv1617','Mf':'Mf1617'},inplace=True)

df1516=pd.read_csv("Statistiche_Fantacalcio_2015-16_Statistico.csv",sep=";",names=header_list,dtype=type_dict)
df1516['Mv']=df1516.apply(lambda x: stfMv(x['Mv']), axis=1)
df1516['Mf']=df1516.apply(lambda x: stfMv(x['Mf']), axis=1)
df1516.rename(columns={'Mv':'Mv1516','Mf':'Mf1516'},inplace=True)

#df1920.drop(['R','Nome','Squadra','Pg','Gf','Gs','Rp','Rc','R+','R-','Ass','Asf','Amm','Esp','Au'],axis=1,inplace=True)
df1819.drop(['R','Nome','Squadra','Pg','Gf','Gs','Rp','Rc','R+','R-','Ass','Asf','Amm','Esp','Au'],axis=1,inplace=True)
df1718.drop(['R','Nome','Squadra','Pg','Gf','Gs','Rp','Rc','R+','R-','Ass','Asf','Amm','Esp','Au'],axis=1,inplace=True)
df1617.drop(['R','Nome','Squadra','Pg','Gf','Gs','Rp','Rc','R+','R-','Ass','Asf','Amm','Esp','Au'],axis=1,inplace=True)
df1516.drop(['R','Nome','Squadra','Pg','Gf','Gs','Rp','Rc','R+','R-','Ass','Asf','Amm','Esp','Au'],axis=1,inplace=True)

HP20_18=df1920.merge(df1819, left_on=['Id'], right_on=['Id'],how='inner')
HP20_17=HP20_18.merge(df1718, left_on=['Id'], right_on=['Id'],how='inner')
HP20_16=HP20_17.merge(df1617, left_on=['Id'], right_on=['Id'],how='inner')
HP20_15=HP20_16.merge(df1516, left_on=['Id'], right_on=['Id'],how='inner')

HP20_15['Mv5'] = HP20_15[['Mv','Mv1819','Mv1718','Mv1617','Mv1516']].mean(axis=1)
HP20_15['Mf5'] = HP20_15[['Mf','Mf1819','Mf1718','Mf1617','Mf1516']].mean(axis=1)

HP20_15.drop(['Mv1819','Mv1718','Mv1617','Mv1516','Mf1819','Mf1718','Mf1617','Mf1516'],axis=1,inplace=True)

HP20_16['Mv4'] = HP20_16[['Mv','Mv1819','Mv1718','Mv1617']].mean(axis=1)
HP20_16['Mf4'] = HP20_16[['Mf','Mf1819','Mf1718','Mf1617']].mean(axis=1)

HP20_16.drop(['Mv1819','Mv1718','Mv1617','Mf1819','Mf1718','Mf1617'],axis=1,inplace=True)


HP20_17['Mv3'] = HP20_17[['Mv','Mv1819','Mv1718']].mean(axis=1)
HP20_17['Mf3'] = HP20_17[['Mf','Mf1819','Mf1718']].mean(axis=1)

HP20_17.drop(['Mv1819','Mv1718','Mf1819','Mf1718'],axis=1,inplace=True)

HP20_18['Mv2'] = HP20_18[['Mv','Mv1819']].mean(axis=1)
HP20_18['Mf2'] = HP20_18[['Mf','Mf1819']].mean(axis=1)

HP20_18.drop(['Mv1819','Mf1819'],axis=1,inplace=True)


#HP20_18.to_csv("HP20_18.csv",index=False)
#HP20_17.to_csv("HP20_17.csv",index=False)
#HP20_16.to_csv("HP20_16.csv",index=False)
#HP20_15.to_csv("HP20_15.csv",index=False)


##File Save
HP20_18.drop(['Mv','Mf','R','Nome','Squadra','Pg','Gf','Gs','Ass','Amm','Esp'],axis=1,inplace=True)
HP20_18.to_csv("HP20_18.csv",index=False)
print(HP20_18)
HP20_17.drop(['Mv','Mf','R','Nome','Squadra','Pg','Gf','Gs','Ass','Amm','Esp'],axis=1,inplace=True)
HP20_17.to_csv("HP20_17.csv",index=False)
print(HP20_17)
HP20_16.drop(['Mv','Mf','R','Nome','Squadra','Pg','Gf','Gs','Ass','Amm','Esp'],axis=1,inplace=True)
HP20_16.to_csv("HP20_16.csv",index=False)
print(HP20_16)
HP20_15.drop(['Mv','Mf','R','Nome','Squadra','Pg','Gf','Gs','Ass','Amm','Esp'],axis=1,inplace=True)
HP20_15.to_csv("HP20_15.csv",index=False)
print(HP20_15)

#df2018['Mvr']=df.apply(lambda x: f1(x[str(i-1)],x[str(i)]), axis=1)

#def f (x)
#    if (x>0) : return x 
#    else: return '0'  
      
    
HP20_18=HP20_18.merge(HP20_17,left_on='Id',right_on='Id',how='left')
print(HP20_18)
HP20_18=HP20_18.merge(HP20_16,left_on='Id',right_on='Id',how='left')
print(HP20_18)
HP20_18=HP20_18.merge(HP20_15,left_on='Id',right_on='Id',how='left')
print(HP20_18)

df1920=df1920.merge(HP20_18,left_on='Id',right_on='Id',how='left')


df1920.fillna(0,inplace=True)

df1920=df1920[['Id','R','Nome','Squadra','Pg','Gf','Gs','Ass','Amm','Esp','Mv','Mf','Mv2','Mf2','Mv3','Mf3','Mv4','Mf4','Mv5','Mf5']]

print(df1920)


df1920['Mv5']=df1920['Mv5'].round(decimals=2)
df1920['Mf5']=df1920['Mf5'].round(decimals=2)

df1920['Mv4']=df1920['Mv4'].round(decimals=2)
df1920['Mf4']=df1920['Mf4'].round(decimals=2)

df1920['Mv3']=df1920['Mv3'].round(decimals=2)
df1920['Mf3']=df1920['Mf3'].round(decimals=2)

df1920['Mv2']=df1920['Mv2'].round(decimals=2)
df1920['Mf2']=df1920['Mf2'].round(decimals=2)

def f(a,b,c,d):
    if(a)!=0: return a 
    elif(b!=0): return b
    elif(c!=0): return c
    elif(d!=0): return d
    else: return 0 

df1920['Hmf']=df1920.apply(lambda x: f(x['Mf5'],x['Mf4'],x['Mf3'],x['Mf2']),axis=1)


df1920.to_csv("Statistiche_Fantacalcio_2019-20_StatisticoHistory.csv",index=False)


print(df1920)


# n=0,1,2,3   
#tra lista 3 e lista 2 voglio: nella lista 23 devono esserci tutti i giocatori presenti in lista 2, tutti quelli della 3 con il valore di Mvn più elevato 


#HP20_18.drop(['Mv1819','Mf1819'],axis=1,inplace=True)

#res1=HP20_18.merge(HP20_15, left_on=['Id'], right_on=['Id'],how='left')
#def f (a,b,c,d):
#    if(a==b):
#        return c



#df2018['Mvr']=df.apply(lambda x: f1(x[str(i-1)],x[str(i)]), axis=1)
    
#df[str(i)] = np.where(df['aa'] == True,0, df[str(i)])
#print(res1)

#res1['aaaa']=result.Mvt_y.isnull()
#print(res1)
#df2=result[result['aaaa']==False]
#print(df2)
#res1.drop(df2.index,inplace=True)
#print(res1)


#result.to_csv("AA3.csv")



#print(HP20_15)
#print(HP20_18)
#print(res1)