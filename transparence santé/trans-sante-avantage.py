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

#len(df4.index)
#Out[31]: 12 827 163

end = time.time()
#elapsed = end - start

elapsed2 = (end - start)/60
print(f'Temps d\'exécution : {elapsed2:}minutes')
#Temps d'exécution : 8 minutes 12 secondes
#peu différent de R


#on ne garde que 18 colonnes sur 35 pour alleger la base et la memoire
mycolumns = ['benef_nom','benef_prenom','avant_date_signature','avant_montant_ttc'] 
df5=df4[mycolumns]



#chercher l'année 2019
#séparation d'une chaine de caractere
#date=str.split(df5['avant_date_signature'][1], '/')


for i in range(0,len(df5)):
    date[i]=str.split(df5['avant_date_signature'][i], '/')



from datetime import datetime

dateString = "31/12/2013"
dateString=df5['avant_date_signature']
dateFormatter = "%d/%m/%Y"
datetime.strptime(dateString, dateFormatter)






annee2<-data_small$avant_date_signature
library(tidyverse)
annee2<-str_split(annee2, "/", simplify = TRUE)
annee<-as.integer(annee2[,3])
data_small<-cbind(data_small,annee)








