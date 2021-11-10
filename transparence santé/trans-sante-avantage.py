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

#affichage des 11 1eres lignes et test filtre par année
#test
#df_10=df5[0:10]
#df_10
#df_11=df_10[ (df_10['annee']== "2016") ]
#avantage1=pd.to_numeric(df_10['avant_montant_ttc'])
#df_10['avant_montant_ttc']=avantage1.loc[:]

#<ipython-input-83-c4214ed348be>:1: SettingWithCopyWarning: 
#A value is trying to be set on a copy of a slice from a DataFrame.
#Try using .loc[row_indexer,col_indexer] = value instead

#See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#  df_10['avant_montant_ttc']=avantage1.loc[:]
#ok
#penser au .loc lors du remplacement d'une colonne

#Filtre sur l'année 2019 
df6=df5[ (df5['annee']== "2019") ]
avantage=pd.to_numeric(df6['avant_montant_ttc'])
df6['avant_montant_ttc']=avantage.loc[:]

#sum(avantage)

df_test=df6[0:9]

del date_sep
del annee
del date
del df6['avant_date_signature']



df7=df6.groupby(by='avant_montant_ttc', axis=0, level=None, as_index=True, sort=True, group_keys=True, observed=False, dropna=True)

df7=df6.groupby(by=['benef_nom','benef_prenom']).sum()

df8=df7[df7['avant_montant_ttc'] > 30000 ]


df9=df8.sort_values(by = 'avant_montant_ttc',ascending = False)

import csv

# open the file in the write mode
f = open('result_python.csv', 'w')

# create the csv writer
writer = csv.writer(f)



file_name = 'result_python.xlsx'
  
df9.to_excel(file_name) 




