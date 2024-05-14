import requests
from bs4 import BeautifulSoup
import mysql.connector

cnx = mysql.connector.connect(user = 'wsa', 
                              host = '34.68.250.121',
                              database = 'Tutorials-Winter2024',
                             password = 'LeBron>MJ!')
cursor = cnx.cursor(buffered = True)

years = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
for year in years:
    url = requests.get(f"https://www.sports-reference.com/cfb/schools/michigan/{year}/gamelog/")
    soup = BeautifulSoup(url.text, 'html.parser')
    #print(soup.prettify())
    
    table = soup.find("div", attrs = {'id': 'div_offense'}).find("table")
    #print(rosterTable)
    
    tableRows = table.find('tbody').find_all("tr")
    #print(tableRows)

    for row in tableRows:
        #print(row)
        #print("----------------")
        
        columns = row.find_all("td")
        
        date = columns[0].find('a').text
        year = int(date.split('-')[0])
        
        home_away_section = columns[1].text
        if home_away_section == '':
            home_away = 'Home'
        elif home_away_section == '@':
            home_away = 'Away'
        else:
            home_away = 'Nuetral'
        
        opponent = columns[2].find('a').text
        
        result_list = columns[3].text.split(' ')
        result = result_list[0]
        points_scored = int(result_list[1].split('-')[0][1:])
        points_against = int(result_list[1].split('-')[1][:-1])
        
        pass_cmp = int(columns[4].text)
        pass_att = int(columns[5].text)
        pass_pct = float(columns[6].text)
        pass_yrds = int(columns[7].text)
        pass_td = int(columns[8].text)
        pass_1st_down = int(columns[16].text)
        
        rush_att = int(columns[9].text)
        rush_yrds = int(columns[10].text)
        rush_td = int(columns[12].text)
        rush_1st_down = int(columns[17].text)
        
        total_offense = int(columns[14].text)
        fumbles = int(columns[22].text)
        ints = int(columns[23].text)
        
        values = [date, year, opponent, home_away, result, points_scored, points_against]
        #print(values)
        
        statement = "INSERT INTO Michigan_GameLogs_Smayan (date, year, opponent, home_away, result, points_scored, points_against) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        
        # last 2 lines are commented out so we don't inadvertenly add all our data to SQL twice and create duplicate rows
        
        #cursor.execute(statement, values)
        #cnx.commit()

