###########################################################
#Importation et traitement de la base transparence sante
#qui est un bon candidat pour le Big data
###########################################################

#remarque: les accents et apostrophe,... dans les commentaires sont volontairement retire 
#autant que possible a cause du systeme d encodage (j utilise UTF-8)
#ces derniers pouvant provoquer des modifications dans les commentaires

#lien 1:
#https://github.com/DorianNaaji/Transparence-Sante
#lien download: 
#https://www.data.gouv.fr/fr/datasets/transparence-sante-1/

setwd("C:\\Users\\Francis\\R_new\\transparence santé")

##################################################
#temps de calcul:
T1<-Sys.time()

rm (list=ls())
library(data.table)
data<-fread("C:\\Users\\Francis\\R_new\\transparence santé\\data\\declaration_avantage_2021_10_26_04_00.csv",stringsAsFactors=TRUE)
nrow(data)
#[1] 12 827 163
#ce code s'effectue en 1 dizaine de minutes (parfois plus) pour un ordinateur portable moyennement puissant
#Processeur: AMD A8-7410 APU with AMD Radeon R5 Graphics       2.20 GHz
#Memoire RAM installé: 8,00Go (6,93Go utilisable)

T2<-Sys.time()
Tdiff= difftime(time2, time1)
Tdiff
#######################################################

data[0]
#data frame with 0 columns and 12 827 163 rows

colnames(data)
#[1] "entreprise_identifiant"         "denomination_sociale"          
#[3] "ligne_identifiant"              "ligne_rectification"           
#[5] "benef_categorie_code"           "categorie"                     
#[7] "benef_nom"                      "benef_prenom"                  
#[9] "benef_qualite_code"             "qualite"                       
#[11] "benef_adresse1"                 "benef_adresse2"                
#[13] "benef_adresse3"                 "benef_adresse4"                
#[15] "benef_codepostal"               "benef_ville"                   
#[17] "benef_pays_code"                "pays"                          
#[19] "benef_titre_code"               "benef_titre_libelle"           
#[21] "benef_specialite_code"          "benef_speicalite_libelle"      
#[23] "benef_identifiant_type_code"    "identifiant_type"              
#[25] "benef_identifiant_valeur"       "benef_etablissement"           
#[27] "benef_etablissement_codepostal" "benef_etablissement_ville"     
#[29] "benef_denomination_sociale"     "benef_objet_social"            
#[31] "ligne_type"                     "avant_date_signature"          
#[33] "avant_montant_ttc"              "avant_nature"                  
#[35] "avant_convention_lie"           "semestre"  

rm(data)

#Visualisation de petites bases sous Excel
#write.csv(data[1:100,],file=".\\Data\\data_temp\\avantage-100.csv")
#write.csv(data[1:10000,],file=".\\Data\\data_temp\\avantage-10000.csv")

#10 1eres lignes
data10<-data[1:10,]
View(data10)

library(dplyr)     # pour mutate_at et %>%
#library(tidyverse)
library(tidyr)      # pour unnest et separate
library(caret)
#dplyr contient les operateurs %>% qui permettent le data wrangling (operation sur la BDD)

data_small <- data %>%
select(entreprise_identifiant,denomination_sociale,ligne_rectification,benef_categorie_code,benef_nom,
benef_prenom,benef_qualite_code,qualite,benef_codepostal,benef_ville,benef_titre_libelle,benef_speicalite_libelle,benef_identifiant_valeur,avant_date_signature,avant_montant_ttc,avant_nature,semestre)
#ce code s effectue en quelques secondes

#write.csv(data_small,file=".\\Data\\avantage_small_new.csv")

#decouplage de la base par année
#test
#annee<-data_small$avant_date_signature[1]
#library(tidyverse)
#annee2<-str_split(annee, "/", simplify = TRUE)
#annee2[1,3]
#fin test


annee2<-data_small$avant_date_signature
library(tidyverse)
annee2<-str_split(annee2, "/", simplify = TRUE)
annee<-as.integer(annee2[,3])
data_small<-cbind(data_small,annee)

#test pour verifier la construction de la colonne annee
#table(annee)

#2018          2019          2020       2021 
#1634241       1537320     466504    117659
#2019 semble etre un bon candidat pour notre etude (1 537 320 enregistrements ce qui est large)
#et pas trop eloigne dans le temps

rm(annee2,annee)

#data_small$annee<-NULL  suppression de la colonne mal construite (ancien)


###########################################################################
#calcul des avantages par bénéficiaires en 2019 (fonction groupby de dplyr)
library(dplyr)

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
#on trouve ici les 91 enregistrement de personnes ayant recu plus de 30 000 euros en avantage en 2019

#resultats sous Excel
write.csv(resum4,file=".\\Data\\result_30000.csv")

