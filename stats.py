import requests
from bs4 import BeautifulSoup
import time


years = ['1998-03-08', '1999-03-07', '2000-03-12', '2001-03-11', '2002-03-10', '2003-03-16','2004-03-14','2005-03-13',
         '2006-03-12','2007-03-11','2008-03-16','2009-03-15','2010-03-14', '2011-03-13', '2012-03-11', '2013-03-17', 
         '2014-03-16', '2015-03-15', '2016-03-13', '2017-03-12', '2018-03-11', '2019-03-17', '2021-03-14', '2022-03-13', 
        '2023-03-12', '2024-03-17']
for year in years:
    url = requests.get("https://www.teamrankings.com/ncaa-basketball/stat/assist--per--turnover-ratio?date=" + year)
    soup = BeautifulSoup(url.text, 'html.parser')

    table = soup.find('table').find('tbody')
    tableRows = table.find_all('tr')
    date_list = year.split('-')
    currentYear = date_list[0]

    for row in tableRows:
        
        columns = row.find_all("td")
        if len(columns) > 0 and columns[2].text.split('%')[0] != '--':
        
            rank = int(columns[0].text)
            team = columns[1].text
            data = float(columns[2].text.split('%')[0])
            # we are getting multiple data points of interest from this single column so we must split it
            values = [year, rank, team, data]
            print(values)