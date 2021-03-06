#Citizen Requests
# Dataset link - http://donnees.ville.montreal.qc.ca/dataset/5866f832-676d-4b07-be6a-e99c21eb17e4/resource/2cfa0e06-9be4-49a6-b7f1-ee9f2363a872/download/requetes311.csv
#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df = pd.DataFrame()

################ Reading data #################################################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('requetes311.csv')
#prints first 5 row of the dataframe
print(df.head(5))

#number of records in dataset
print("Number of records: "+str(len(df)))

############### Filtering data #################################################################################
print("###################### Filtering columns ###############################################################")
#filters all records for columns ID_UNIQUE, ACTI_NOM  and ARRONDISSEMENT
print(df[["ID_UNIQUE","ACTI_NOM","ARRONDISSEMENT"]])

print("####################### Filtering on values of column ##################################################")
#filters the records in which TYPE_LIEU_INTERV has value - Adresse
print(df[df["TYPE_LIEU_INTERV"] == "Adresse"])

print("######################## Filtering on multiple values on column #########################################")
#filters the records in which ARRONDISSEMENT has value - Dorval or Mont-Royal
print(df[(df["ARRONDISSEMENT"] == "Dorval") | (df["ARRONDISSEMENT"] == "Mont-Royal")])

print("######################### Slice on rows (by index) #######################################################")
#filter by index (taking rows from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[20:30])

print("########################## Slice on columns(by index)######################################################")
#filter by index (taking columns from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[:,2:7])

print("########################## Slice on row and column (by index) ############################################")
#filter by index (taking rows from 0 to 10, and columns 2 to 5)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[0:10,2:5])


print("########################## Multiple filters on column and get value of other column #######################")
#Gives the value of ARRONDISSEMENT column where NATURE is "Requete" and ACTI_NOM is "Communications corporatives"
print(df.loc[(df["NATURE"]=="Requete")&(df["ACTI_NOM"]== "Communications corporatives"),"ARRONDISSEMENT"])
