#https://www.fantacalcio.it/statistiche-serie-a/2015-16/undefined/gol
#https://fbref.com/it/comp/11/Statistiche-di-Serie-A



import pandas as pd

type_dict={'QtA':'int','Id':'str','R':'str','Nome':'str','Squadra':'str','Pg':'int','Gf':'int','Gs':'int','Ass':'int','Amm':'int','Esp':'int','Mv':'float','Mf':'float','Mv2':'float','Mf2':'float','Mv3':'float','Mf3':'float','Mv4':'float','Mf4':'float','Mv5':'float','Mf5':'float'}#,'Nome':'str','Squadra':'str','Pg':'int','Mv':'float','Mf':'float','Gf':'int','Gs':'int','Rp':'int','Rc':'int','R+':'int','R-':'int','Ass':'int','Asf':'int','Amm':'int','Esp':'int','Au':'int'}


header_list2= ['Id','R','Nome','Squadra','QtA','QtI','Diff']

df=pd.read_csv("Statistiche_Fantacalcio_2019-20_StatisticoHistory.csv",dtype=type_dict)
dfListone=pd.read_csv("Quotazioni_Fantacalcio.csv",sep=",",names=header_list2,dtype=type_dict)
print(df)
print(dfListone)
df.drop(['Nome','Squadra'],axis=1,inplace=True)
dfListone.drop(['R','QtI','Diff'],axis=1,inplace=True)


dfCombined=dfListone.merge(df, left_on=['Id'], right_on=['Id'],how='left')

print(dfCombined)
dfCombined.fillna(0,inplace=True)
print(dfCombined)

dfCombined=dfCombined[dfCombined['Pg']>15.0]

dfCombined.sort_values(by=['Mf'],inplace=True,ascending=False)
dfCombined.reset_index(inplace=True,drop=True)

def f(x,y):
    if(x=='A'):return(y*((2000)/250))
    else : return (y*((1000)/250))

dfCombined['QtA1000']=dfCombined.apply(lambda x: f(x['R'],x['QtA']),axis=1)

print(dfCombined)



dfCombined.to_csv("CompleteList.csv",index=False)


dfCombined=dfCombined[['Id','R','Nome','Squadra','QtA1000']]
#dfCombined.sort_values(by=['Nome'],inplace=True,ascending=False)



dfPor=dfCombined[dfCombined['R']=='P']
dfPor.sort_values(by=['Nome'],inplace=True,ascending=True)
dfPor.reset_index(inplace=True,drop=True)

dfDif=dfCombined[dfCombined['R']=='D']
dfDif.sort_values(by=['Nome'],inplace=True,ascending=True)
dfDif.reset_index(inplace=True,drop=True)


dfCen=dfCombined[dfCombined['R']=='C']
dfCen.sort_values(by=['Nome'],inplace=True,ascending=True)
dfCen.reset_index(inplace=True,drop=True)

dfAtt=dfCombined[dfCombined['R']=='A']
dfAtt.sort_values(by=['Nome'],inplace=True,ascending=True)
dfAtt.reset_index(inplace=True,drop=True)


dfPor=dfPor[dfPor.index<20]
dfDif=dfDif[dfDif.index<64]
dfCen=dfCen[dfCen.index<64]
dfAtt=dfAtt[dfAtt.index<64]



dfPor.to_csv("1Portieri.csv",index=False)
dfDif.to_csv("1Difensori.csv",index=False)
dfCen.to_csv("1Centrocampisti.csv",index=False)
dfAtt.to_csv("1Attaccanti.csv",index=False)


