#https://www.fantacalcio.it/statistiche-serie-a/2015-16/undefined/gol
#https://fbref.com/it/comp/11/Statistiche-di-Serie-A



import pandas as pd

type_dict={'Id':'str','R':'str'}#,'Nome':'str','Squadra':'str','Pg':'int','Mv':'float','Mf':'float','Gf':'int','Gs':'int','Rp':'int','Rc':'int','R+':'int','R-':'int','Ass':'int','Asf':'int','Amm':'int','Esp':'int','Au':'int'}




header_list = ['Id','R','Nome','Squadra','Pg','Mv','Mf','Gf','Gs','Rp','Rc','R+','R-','Ass','Asf','Amm','Esp','Au']
header_list2= ['Id','R','Nome','Squadra','QtA','QtI','Diff']

df=pd.read_csv("Statistiche_Fantacalcio_2019-20_Statistico.csv",sep=";",names=header_list,dtype=type_dict)
dfListone=pd.read_csv("Quotazioni_Fantacalcio.csv",sep=",",names=header_list2,dtype=type_dict)

#df.drop("Id",axis=1,inplace=True)
dfListone.drop(['R','Nome','Squadra','QtI','Diff'],axis=1,inplace=True)

df1=df[df['Pg']<=15]

df.drop(df1.index,inplace=True)

df['GfT']=df['Gf']+df['R+']


dfCombined=df.merge(dfListone, left_on=['Id'], right_on=['Id'],how='inner')

print(dfCombined)

dfCombined.sort_values(by=['Mf','QtA'],inplace=True,ascending=False)
dfCombined.reset_index(inplace=True,drop=True)

dfPor=dfCombined[dfCombined['R']=='P']
dfPor.reset_index(inplace=True,drop=True)

dfDif=dfCombined[dfCombined['R']=='D']
dfDif.reset_index(inplace=True,drop=True)

dfCen=dfCombined[dfCombined['R']=='C']
dfCen.reset_index(inplace=True,drop=True)

dfAtt=dfCombined[dfCombined['R']=='A']
dfAtt.reset_index(inplace=True,drop=True)


dfPor=dfPor[dfPor.index<20]
dfDif=dfDif[dfDif.index<100]
dfCen=dfCen[dfCen.index<100]
dfAtt=dfAtt[dfAtt.index<100]



dfPor.to_csv("Portieri.csv",index=False)
dfDif.to_csv("Difensori.csv",index=False)
dfCen.to_csv("Centrocampisti.csv",index=False)
dfAtt.to_csv("Attaccanti.csv",index=False)


