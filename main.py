'''
Created on 29 Feb 2020

@author: rob_h
'''
import csv
import pandas as pd
from scrape_players import playerScraper

def main():
    
    print ("======== Process Start ========")
    url='https://fantasy.nrl.com/stats-centre'   
    playerData=playerScraper(url)
    writeToFile(playerData)
    print ("======== Process Complete ========") 

    
def writeToFile(data):
    headers=["ID","Player","Team","Position","Status","Price","SeasonPriceChange","PriceChangeLastRD","RdsPlayed","SelectBy","Projection","FormLast3Rds","$/Points","PointsCurrRd","TotalPoints"]
    with open("C:\\Users\\rob_h\\Documents\\workspace\\nrlFantasy\\csv files\\nrlFantasyRd2.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
                

if __name__ == '__main__':
    main()
