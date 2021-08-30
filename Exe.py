#https://www.fantacalcio.it/statistiche-serie-a/2015-16/undefined/gol
#https://fbref.com/it/comp/11/Statistiche-di-Serie-A


#import openpyxl
import pandas as pd
from pandas import ExcelWriter

#from openpyxl.worksheet.worksheet import Worksheet
#from openpyxl.workbook import Workbook

def Rol(r,m):
    if(r=='P') :
        if(m==0.0) : return 'N'
        if(m>=5.20): return 'A'
        elif(5.20>m>=5): return 'B'
        elif(5>m): return 'C' 
    if(r=='D'):
        if(m==0.0) : return 'N'
        if(m>6.5) : return 'A'
        elif(6.5>m>6): return 'B'
        elif(6>m): return 'C' 
    if(r=='C'):
        if(m==0.0) : return 'N'
        if(m>=7) : return 'A'
        elif(7>m>=6.5): return 'AB'
        elif(6.5>m>=6): return 'B'
        elif(6>m): return 'C'		
    if(r=='A'):
        if((m==0.0) | (m==0)) : return 'N'
        if(m>=7.80) : return 'A'
        elif(7.80>m>=7.20): return 'AB'
        elif(7.20>m>=6.5): return 'B'
        elif(6.5>m>=6): return 'C'
        elif(6>m): return 'D'	


type_dict={'Id':'str','R':'str','Nome':'str','Squadra':'str','Pg':'int','Gf':'int','Gs':'int','Ass':'int','Amm':'int','Esp':'int','Mv':'float','Mf':'float','Mv2':'float','Mf2':'float','Mv3':'float','Mf3':'float','Mv4':'float','Mf4':'float','Mv5':'float','Mf5':'float'}#,'Nome':'str','Squadra':'str','Pg':'int','Mv':'float','Mf':'float','Gf':'int','Gs':'int','Rp':'int','Rc':'int','R+':'int','R-':'int','Ass':'int','Asf':'int','Amm':'int','Esp':'int','Au':'int'}




header_list = ['Id','R','Nome','Squadra','Pg','Mv','Mf','Gf','Gs','Rp','Rc','R+','R-','Ass','Asf','Amm','Esp','Au']
header_list2= ['Id','R','Nome','Squadra','QtA','QtI','Diff']

df=pd.read_csv("Statistiche_Fantacalcio_2019-20_StatisticoHistory.csv",dtype=type_dict)
dfListone=pd.read_csv("Quotazioni_Fantacalcio.csv",sep=";",names=header_list2,dtype=type_dict)
print(df)
print(dfListone)
df.drop(['R','Nome','Squadra'],axis=1,inplace=True)
dfListone.drop(['QtI','Diff'],axis=1,inplace=True)


dfCombined=dfListone.merge(df, left_on=['Id'], right_on=['Id'],how='left')

print(dfCombined)
dfCombined.fillna(0,inplace=True)
print(dfCombined)


dfCombined.sort_values(by=['Hmf'],inplace=True,ascending=False)
dfCombined.reset_index(inplace=True,drop=True)

print(dfCombined)

dfCombined=dfCombined[(dfCombined['Pg']>15.0) | (dfCombined['Hmf']==0.0)]


dfCombined['ASTA']=dfCombined.apply(lambda x: Rol(x['R'],x['Mf']),axis=1)
dfCombined['ASTAH']=dfCombined.apply(lambda x: Rol(x['R'],x['Hmf']),axis=1)

dfCombined.to_csv("CompleteHistoryList.csv",index=False)

dfPor=dfCombined[dfCombined['R']=='P']
dfPor.reset_index(inplace=True,drop=True)

dfDif=dfCombined[dfCombined['R']=='D']
dfDif.reset_index(inplace=True,drop=True)

dfCen=dfCombined[dfCombined['R']=='C']
dfCen.reset_index(inplace=True,drop=True)

dfAtt=dfCombined[dfCombined['R']=='A']
dfAtt.reset_index(inplace=True,drop=True)


#dfPor=dfPor[dfPor.index<20]
#dfDif=dfDif[dfDif.index<64]
#dfCen=dfCen[dfCen.index<64]
#dfAtt=dfAtt[dfAtt.index<64]

dfPor.to_csv("PortieriH.csv",index=False)
dfDif.to_csv("DifensoriH.csv",index=False)
dfCen.to_csv("CentrocampistiH.csv",index=False)
dfAtt.to_csv("AttaccantiH.csv",index=False)


dfCombined.sort_values(by=['Mf'],inplace=True,ascending=False)
dfCombined.reset_index(inplace=True,drop=True)
print(dfCombined)


	
def f(x,y):
    if(x=='A'):return(y*((1000)/250))
    else : return (y*((1000)/250))

dfCombined['QtA1000']=dfCombined.apply(lambda x: f(x['R'],x['QtA']),axis=1)
dfCombined=dfCombined[['QtA1000','Nome','Squadra','QtA','ASTA','ASTAH','Mv','Mf','Hmf','Pg','Gf','Gs','Ass','Amm','Esp','R']]


#dfCombined['ASTA']=dfCombined.apply(lambda x: Rol(x['R'],x['Mf']),axis=1)

dfPor=dfCombined[dfCombined['R']=='P']


dfPor.reset_index(inplace=True,drop=True)


dfDif=dfCombined[dfCombined['R']=='D']
dfDif.reset_index(inplace=True,drop=True)

dfCen=dfCombined[dfCombined['R']=='C']
dfCen.reset_index(inplace=True,drop=True)

dfAtt=dfCombined[dfCombined['R']=='A']
dfAtt.reset_index(inplace=True,drop=True)

dfCombined.to_csv("CompleteList.csv",index=False)





#dfPor=dfPor[dfPor.index<20]
#dfDif=dfDif[dfDif.index<64]
#dfCen=dfCen[dfCen.index<64]
#dfAtt=dfAtt[dfAtt.index<64]


dfPorF=dfPor[dfPor['ASTA']=='A']
dfPorF.sort_values(by='Nome',ascending=True,inplace=True)
dfPorF.to_csv("PortieriF.csv",index=False)

dfPorM=dfPor[dfPor['ASTA']=='B']
dfPorM.sort_values(by='Nome',ascending=True,inplace=True)
dfPorM.to_csv("PortieriF.csv",index=False)

dfPorS=dfPor[dfPor['ASTA']=='C']
dfPorS.sort_values(by='Nome',ascending=True,inplace=True)
dfPorS.to_csv("PortieriS.csv",index=False)


dfDifF=dfDif[dfDif['ASTA']=='A']
dfDifF.sort_values(by='Nome',ascending=True,inplace=True)
dfDifF.to_csv("DifensoriF.csv",index=False)

dfDifM=dfDif[dfDif['ASTA']=='B']
dfDifM.sort_values(by='Nome',ascending=True,inplace=True)
dfDifM.to_csv("DifensoriM.csv",index=False)


dfDifS=dfDif[dfDif['ASTA']=='C']
dfDifS.sort_values(by='Nome',ascending=True,inplace=True)
dfDifS.to_csv("DifensoriS.csv",index=False)


dfCenF=dfCen[dfCen['ASTA']=='A']
dfCenF.sort_values(by='Nome',ascending=True,inplace=True)
dfCenF.to_csv("CentrocampistiF.csv",index=False)


dfCenM=dfCen[dfCen['ASTA']=='AB']
dfCenM.sort_values(by='Nome',ascending=True,inplace=True)
dfCenM.to_csv("CentrocampistiM.csv",index=False)


dfCenMF=dfCen[dfCen['ASTA']=='B']
dfCenMF.sort_values(by='Nome',ascending=True,inplace=True)
dfCenMF.to_csv("CentrocampistiMF.csv",index=False)


dfCenS=dfCen[dfCen['ASTA']=='C']
dfCenS.sort_values(by='Nome',ascending=True,inplace=True)
dfCenS.to_csv("CentrocampistiS.csv",index=False)


dfAttF=dfAtt[dfAtt['ASTA']=='A']
dfAttF.sort_values(by='Nome',ascending=True,inplace=True)
dfAttF.to_csv("AttaccantiF.csv",index=False)


dfAttM=dfAtt[dfAtt['ASTA']=='AB']
dfAttM.sort_values(by='Nome',ascending=True,inplace=True)
dfAttM.to_csv("AttaccantiM.csv",index=False)

dfAttMF=dfAtt[dfAtt['ASTA']=='B']
dfAttMF.sort_values(by='Nome',ascending=True,inplace=True)
dfAttMF.to_csv("AttaccantiMF.csv",index=False)


dfAttS=dfAtt[dfAtt['ASTA']=='C']
dfAttS.sort_values(by='Nome',ascending=True,inplace=True)
dfAttS.to_csv("AttaccantiS.csv",index=False)


dfPor.sort_values(by='Nome',ascending=True,inplace=True)
dfDif.sort_values(by='Nome',ascending=True,inplace=True)
dfCen.sort_values(by='Nome',ascending=True,inplace=True)
dfAtt.sort_values(by='Nome',ascending=True,inplace=True)

dfPor.to_csv("Portieri.csv",index=False)
dfDif.to_csv("Difensori.csv",index=False)
dfCen.to_csv("Centrocampisti.csv",index=False)
dfAtt.to_csv("Attaccanti.csv",index=False)

writer = pd.ExcelWriter('ListaFantacalcio2021.xlsx',engine='xlsxwriter')

dfPor.to_excel(writer,'Portieri',index=False)

dfDif.to_excel(writer,'Difensori',index=False)

dfCen.to_excel(writer,'Centrocampisti',index=False)

dfAtt.to_excel(writer,'Attaccanti',index=False)

writer.save()
