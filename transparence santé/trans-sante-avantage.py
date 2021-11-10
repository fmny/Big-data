# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:34:25 2021

@author: Francis Mauny
"""

###########################################################
#Importation et traitement de la base transparence sante
#qui est un bon candidat pour le Big data
###########################################################

#path1="C:/Users/Francis/R_new/Python Scripts/Transparence santé"

import time
start = time.time()

import pandas as pd
path="C:/Users/Francis/R_new/transparence santé/data/declaration_avantage_2021_10_26_04_00.csv"
df4=pd.read_csv(path,sep=";")
#semble plus rapide que R

#attention:
#DtypeWarning: Columns (12,13,14,24,25,26,27,28,29) have mixed 
#types.Specify dtype option on import 
#or set low_memory=False.

#len(df4.index)
#Out[31]: 12 827 163

end = time.time()
#elapsed = end - start

elapsed2 = (end - start)/60
print(f'Temps d\'exécution : {elapsed2:}minutes')
#Temps d'exécution : 8 minutes 12 secondes
#peu différent de R


#on ne garde que 4 colonnes sur 35 pour alleger la base et la memoire
#de plus ce sont les seules à traiter pour le moment
mycolumns = ['benef_nom','benef_prenom','avant_date_signature','avant_montant_ttc'] 
df5=df4[mycolumns]

del df4

#chercher l'année 2019
#séparation d'une chaine de caractere
#date=str.split(df5['avant_date_signature'][1], '/')

date=df5['avant_date_signature']

date_sep= date.str.split("/", n = 3, expand = True)

annee=date_sep.loc[:,[2]]             
df5['annee']=annee

#affichage des 10 1eres lignes
df_10=df5[0:10]
df_10
df_11=df_10[ (df_10['annee']== "2016") ]
#ok



df_10['avant_date_signature']=to_numeric(df_10['avant_date_signature'])




#type(df_10['annee'])
#Out[17]: pandas.core.series.Series


del date_sep
del annee
del date


#on ne conserve que l'année 2019 et les personnels soignant 
df6=df5[ (df5['annee']== 2019) ]



df[ (df['Sex'] == 1) & (df['Age'] < 25 )]



#test sur data_small_2019
data_small2<-data_small %>% filter(annee==2019)
nrow(data_small2)
#1 537 320

rm(data_small)

#agreger des donnees de la base des avantages en 2019
resum1<-data_small2%>%select(benef_nom,benef_prenom,avant_montant_ttc)

#laborieux
resum2<-resum1%>%group_by(benef_nom,benef_prenom) %>% summarise(total_avantage=sum(avant_montant_ttc))
resum3<-resum2[order(-resum2$total_avantage),]

#on va retirer la ligne 1 qui n a pas de nom
resum3<-resum3[2:nrow(resum3),]

resum4<-resum3 %>% filter(resum3$total_avantage>30000)

#je ne sais pas pourquoi ca ne marche pas
#resum4<-resum4 %>% dplyr::filter(resum4$total_avantage > 10000)

resum4<-filter(resum3,total_avantage > 30000)


https://www.it-swarm-fr.com/fr/python/changer-le-type-de-donnees-des-colonnes-dans-les-pandas/1072113742/





