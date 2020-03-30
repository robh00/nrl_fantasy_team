"""
Scrape data for specified period.
Data saved to `..
<Player>
<Team>
<Position>
<Price>
<Overall Season Price Change>
<Price Change Last Rd>
<Rounds played>
<Selected By %>
<Average Per RND >
<Form (L3 Avg) >
<$/points>
<Points RND >
< Total points>
 """
 

from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Firefox(executable_path=r'C:\\Python37\\geckodriver-v0.26.0-win64\\geckodriver.exe')



def playerScraper(url):
   
    
    driver.get(url)
    # Give the javascript time to render
    time.sleep(1)
    # Now we have the page, let BeautifulSoup do the rest!
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # The text containing players names  are in the div with class caption.
    driver.quit()
    playerList=[]
  
    numRecords=0
    playerDetails=soup.find_all(class_='player-pool-item trade-pool-list-player type-base')
    #for details in soup.find_all(class_='player-pool-item trade-pool-list-player type-base'):
    for details in playerDetails:
        playerList.append([])
        
        indexNum=str(numRecords)
        playerList[numRecords].append(indexNum)
        playerName=details.find(class_='player-name').text.strip()
        playerList[numRecords].append(playerName)
        playerTeam=details.find(class_='player-opponent').find('b').text.strip()
        playerList[numRecords].append(playerTeam)
        playerPosition=details.find(class_='player-positions').text.strip()
        playerList[numRecords].append(playerPosition)
        
        #get playing status of each player
        for statusFlag in details.find_all('i',class_='player-status'):
            playerStatus=statusFlag['class'][1]
            playerList[numRecords].append(playerStatus)
             
        cols=details.find_all('div',class_='column')
        for x in range(1,len(cols)):
            playerList[numRecords].append(cols[x].text.strip())
        numRecords +=1
    print ("Number of records ",numRecords)
    return playerList