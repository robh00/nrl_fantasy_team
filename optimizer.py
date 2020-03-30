from pulp import *
import numpy as np
import pandas as pd
import csv

print ("======== Process Start ========")   
#Here we read the data into a pandas dataframe.
players=(pd.read_csv("C:\\temp\\nrlFantasyRd2Reformat.csv"))
print(players)
#itialize the optimization model
model = LpProblem("NRL", LpMaximize)
#we need to create dictionaries for each one of our parameters:
total_points = {}
cost = {}
playing={}
HOK = {}
FRF = {}
SRF = {}
HLF = {}
CTR = {}
WFB = {}
number_of_players = {}
   
# i = row index, player = player attributes
for i, player in players.iterrows():
    var_name = 'x' + str(i) # Create variable name
    decision_var = LpVariable(var_name, cat='Binary') # Initialize Variables
    total_points[decision_var] = player["Projection"] # Create Points Dictionary
    cost[decision_var] = player["Price"] # Create Cost Dictionary
    playing[decision_var]=player["Available"]
      
    # Create Dictionary for Player Types
    HOK[decision_var] = player["HOK"]
    FRF[decision_var] = player["FRF"]
    SRF[decision_var] = player["2RF"]
    HLF[decision_var] = player["HLF"]
    CTR[decision_var] = player["CTR"]
    WFB[decision_var] = player["WFB"]
    number_of_players[decision_var] = 1.0
     
# Define ojective function and add it to the model
objective_function = LpAffineExpression(total_points)
model += objective_function
   
#Define cost constraint and add it to the model
total_cost = LpAffineExpression(cost)
model += (total_cost <= 9800000)
#Define playing constraint and add it to the model
playing = LpAffineExpression(playing)
model +=(playing<=0)
model +=(playing>=-1)
  
# Add player type constraints
HOK_constraint = LpAffineExpression(HOK)
FRF_constraint = LpAffineExpression(FRF)
SRF_constraint = LpAffineExpression(SRF)
HLF_constraint = LpAffineExpression(HLF)
CTR_constraint = LpAffineExpression(CTR)
WFB_constraint = LpAffineExpression(WFB)
total_players = LpAffineExpression(number_of_players)
playing_constraint= LpAffineExpression(playing)
   
model += (HOK_constraint == 2)
model += (FRF_constraint == 4)
model += (SRF_constraint == 5)
model += (HLF_constraint == 3)
model += (CTR_constraint == 3)
model += (WFB_constraint == 4)
model += (total_players == 21)
  
# All of the possible PuLP solvers
#pulp.pulpTestAll()
model.status
   
try:
    model.solve()
except Exception:
    print('Problem infeasible')
        
print(model.status)
players["is_drafted"] = 0.0
 
for var in model.variables():
    # Set is drafted to the value determined by the LP
    players.iloc[int(var.name[1:]),21] = var.varValue # column 21 = is_drafted
   
my_team = players[players["is_drafted"] == 1.0]
my_team = my_team[["Player","Team","Position","Price","SeasonPriceChange","PriceChangeLastRD","RdsPlayed","SelectBy","Projection","FormLast3Rds","$/Points","PointsCurrRd","TotalPoints","Available","is_drafted"]]
    
print(my_team)
my_team.to_csv("C:\\temp\\is_draftedRd1.csv")
   
           
   
print ("Total used amount of salary cap: {}".format(my_team["Price"].sum()))
print ("Projected points: {}".format(my_team["Projection"].sum().round(1)))
print ("======== Process Complete ========")
