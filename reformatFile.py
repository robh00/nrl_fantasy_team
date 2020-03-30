import numpy as np
import pandas as pd
import csv

print ("======== Process Start ========")   
#Here we read the data into a pandas dataframe.
df=pd.read_csv("C:\\Users\\rob_h\\Documents\\workspace\\nrlFantasy\\csv files\\nrlFantasyRd2.csv")

df=df.drop(["ID"],axis = 1) #drop the id column
df["Position"]=df['Position'].str[:3]
df["Price"]=df["Price"].str.replace("k","000")
#df["Price"]=df["Price"].str.replace("m","000")
df["Price"]=df["Price"].str.replace("$","")
#add following columns
df["HOK"] = (df["Position"] == 'HOK').astype(float)
df["FRF"] = (df["Position"] == 'FRF').astype(float)
df["2RF"] = (df["Position"] == '2RF').astype(float)
df["HLF"] = (df["Position"] == 'HLF').astype(float)
df["CTR"] = (df["Position"] == 'CTR').astype(float)
df["WFB"] = (df["Position"] == 'WFB').astype(float)
df["Price"] = df["Price"].astype(float)
df["Available"]= (df["Status"] != 'playing').astype(float)
df.to_csv("C:\\Users\\rob_h\\Documents\\workspace\\nrlFantasy\\csv files\\nrlFantasyRd2Reformat.csv")

print(df)
print ("======== Process Complete ========")