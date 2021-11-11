# Big-data
## Programmes sous R et Python présentant des traitements sur la base transparence santé (12.8M enregistrements).


### 1-Transparence santé 
Contient la méthode utilisée pour l'importation sous R d'un fichier volumineux et certains traitements sur cette base. 

Le fichier transparence santé se trouve à l'adresse suivante: 
https://www.data.gouv.fr/fr/datasets/transparence-sante-1/

Mon fichier concernant les avantages perçus par les professionnels de santé possèdent près de 13 millions de lignes (12 827 163) et pèse plus de 3,5Go au format CSV.  
Les résultats du programme R trans_sante_avantage.r font ressortir les 91 bénéficiaires ayant perçu plus de 30 000€ d'avantages sur l'année 2019 dont 6 qui n'ont pas de prénom et sont en fait des entreprises.

Les résultats du programme Python trans_sante_avantage.py font ressortir les 85 bénéficiaires (avec un nom et prénom) ayant perçu plus de 30 000€ d'avantages sur l'année 2019.

Les résultats comportent néanmoins 2 entreprises dont les champs nom et prénom sont renseignés.

Remarque sur R : Des fichiers .rdata (images de l'espace de travail) créés régulièrement constituent un bon moyen de ne pas refaire des importations de fichiers lourds pouvant prendre un temps important.
