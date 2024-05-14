import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import json

url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-06/2017-ncaa-tournament-bracket-scores-stats-records')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
# print(gameswithupsets)
# for game in gameswithupsets:
#     print(game)
games = []
for game in gameswithupsets:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    print(parts)
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2017 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    print(inserts)


url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-07/2016-ncaa-tournament-bracket-scores-stats-records')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
# print(gameswithupsets)
# for game in gameswithupsets:
#     print(game)
games = []
for game in gameswithupsets:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2016 '
team_frequency['Notre Dame'] = 3
del team_frequency['Notre']
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    print(inserts)


url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-08/2015-ncaa-tournament-bracket-scores-stats-records')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
# print(gameswithupsets)
# for game in gameswithupsets:
#     print(game)
games = []
for game in gameswithupsets:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2015 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    print(inserts)

url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-10/2014-ncaa-tournament-bracket-scores-stats-records')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
# print(gameswithupsets)
# for game in gameswithupsets:
#     print(game)
games = []
for game in gameswithupsets:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2014 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    print(inserts)

url = requests.get('https://www.ncaa.com/news/basketball-men/article/2020-05-11/2013-ncaa-tournament-bracket-scores-stats-records')
soup = BeautifulSoup(url.text, 'html.parser')
soup.prettify()
table = soup.find('article')
# Define a function to filter <ul> tags where the text in <li> elements starts with "No"
def starts_with_no(text):
    if text is None:
        return False
    return text.startswith("No.")

# Find all <ul> tags containing the text starting with "No" in the <li> elements
li_tags = soup.find_all("li")
# Filter <ul> tags where the text in <li> elements starts with "No"
litags = [li_tag for li_tag in li_tags if starts_with_no(li_tag.get_text(separator="|", strip=True))]
gameswithupsets = []
for li_tag in litags:
    gameswithupsets.append(li_tag.get_text(separator="|", strip=True))
# print(gameswithupsets)
# for game in gameswithupsets:
#     print(game)
games = []
for game in gameswithupsets:
    games.append(game.split("||")[0].strip())
team_names = []
for game in games:
    # Splitting the row by commas
    parts = game.split(',')
    # Extracting the team name after "No." in the first part
    first_team_with_score = parts[0].split('No. ')[1].split(',')[0].strip()
    # Removing the score from the team name
    first_team = ' '.join(first_team_with_score.split()[:-1])
    team_names.append(first_team)
names = [team.split(' ', 1)[1] for team in team_names]
team_frequency = {}

# Loop through the list of team names and count occurrences
for team in names:
    if team in team_frequency:
        team_frequency[team] += 1
    else:
        team_frequency[team] = 1
year = '2013 '
for team, frequency in team_frequency.items():
    yearteam = year + str(team)
    inserts = [yearteam, frequency]
    print(inserts)

Schools24 = ["Connecticut", "Houston", "Purdue", "North Carolina", "Tennessee", "Arizona", "Marquette",
    "Iowa State", "Baylor", "Creighton", "Kentucky", "Illinois", "Duke", "Kansas", "Auburn",
    "Alabama", "BYU", "San Diego State", "Wisconsin", "Saint Mary's (CA)", "Gonzaga", "Clemson",
    "Texas Tech", "South Carolina", "Florida", "Washington State", "Texas", "Dayton", "Nebraska",
    "Utah State", "Florida Atlantic", "Mississippi State", "Michigan State", "Texas A&M", "TCU",
    "Northwestern", "Nevada", "Boise State", "Colorado", "Drake", "Virginia", "New Mexico",
    "Oregon", "Colorado State", "N.C. State", "Duquesne", "Grand Canyon", "James Madison",
    "McNeese State", "UAB", "Vermont", "Yale", "Samford", "Charleston", "Oakland", "Akron",
    "Morehead State", "Colgate", "Long Beach State", "Western Kentucky", "South Dakota State",
    "Saint Peter's", "Longwood", "Stetson", "Montana State", "Grambling State", "Howard", "Wagner"] 
team_dict24 = {team: 0 for team in Schools24}

Schools07 = [
    "North Carolina", "Eastern Kentucky", "Michigan State", "Marquette", "USC", "Arkansas",
    "Texas", "New Mexico State", "Vanderbilt", "George Washington", "Washington State", "Oral Roberts",
    "Boston College", "Texas Tech", "Georgetown", "Belmont", "Florida", "Jackson State",
    "Purdue", "Arizona", "Butler", "Old Dominion", "Maryland", "Davidson",
    "Winthrop", "Notre Dame", "Oregon", "Miami (Ohio)", "UNLV", "Georgia Tech",
    "Wisconsin", "Texas A&M-Corpus Christi", "Ohio State", "Central Connecticut State", "Xavier", "BYU",
    "Tennessee", "Long Beach State", "Virginia", "Albany", "Louisville", "Stanford",
    "Texas A&M", "Penn", "Nevada", "Creighton", "Memphis", "North Texas", "Kansas", "Niagara",
    "Kentucky", "Villanova", "Virginia Tech", "Illinois", "Southern Illinois", "Holy Cross",
    "VCU", "Duke", "Pittsburgh", "Wright State", "Indiana", "Gonzaga", "UCLA", "Weber State"
]
team_dict07 = {team:0 for team in Schools07}

Schools08 = [
    "North Carolina", "Mount St. Mary's", "Arkansas", "Indiana", "Notre Dame", "George Mason",
    "Washington State", "Winthrop", "Oklahoma", "St. Joseph's", "Louisville", "Boise State",
    "Butler", "South Alabama", "Tennessee", "American", "Kansas", "Portland State", "UNLV", "Kent State",
    "Villanova", "Clemson", "Siena", "Vanderbilt", "Kansas State", "USC", "Wisconsin", "Cal State Fullerton",
    "Davidson", "Gonzaga", "Georgetown", "UMBC", "Memphis", "Texas-Arlington", "Mississippi State", "Oregon",
    "Michigan State", "Temple", "Pittsburgh", "Oral Roberts", "Marquette", "Kentucky", "Stanford", "Cornell",
    "Miami (FL)", "Saint Mary's", "Texas", "Austin Peay", "UCLA", "Mississippi Valley State", "Texas A&M", "BYU",
    "Western Kentucky", "Drake", "San Diego", "UConn", "Purdue", "Baylor", "Xavier", "Georgia",
    "West Virginia", "Arizona", "Duke", "Belmont"
]

team_dict08 = {team: 0 for team in Schools08}

Schools09 = [
    "Pittsburgh", "East Tennessee State", "Oklahoma State", "Tennessee",
    "Wisconsin", "Florida State", "Xavier", "Portland State", "UCLA", "VCU",
    "Villanova", "American", "Texas", "Minnesota", "Duke", "Binghamton",
    "Louisville", "Morehead State", "Siena", "Ohio State", "Arizona", "Utah",
    "Cleveland State", "Wake Forest", "Dayton", "West Virginia", "Kansas",
    "North Dakota State", "USC", "Boston College", "Michigan State", "Robert Morris",
    "North Carolina", "Radford", "LSU", "Butler", "Western Kentucky", "Illinois",
    "Gonzaga", "Akron", "Arizona State", "Temple", "Syracuse", "Stephen F. Austin",
    "Michigan", "Clemson", "Oklahoma", "Morgan State", "UConn", "Chattanooga",
    "Texas A&M", "BYU", "Purdue", "Northern Iowa", "Washington", "Mississippi State",
    "Marquette", "Utah State", "Missouri", "Cornell", "Maryland", "California",
    "Memphis", "Cal State Northridge"
]

team_dict09 = {team:0 for team in Schools09}

Schools10 = [
    "Kentucky", "East Tennessee State", "West Virginia", "Morgan State", "New Mexico", "Montana",
    "Wisconsin", "Wofford", "Cornell", "Temple", "Washington", "Marquette",
    "Missouri", "Clemson", "Wake Forest", "Texas (OT)", "Syracuse", "Vermont",
    "Kansas State", "North Texas", "Pittsburgh", "Oakland", "Murray State", "Vanderbilt",
    "Butler", "UTEP", "Xavier", "Minnesota", "BYU", "Florida (2OT)",
    "Gonzaga", "Florida State", "Duke", "Arkansas-Pine Bluff", "Villanova", "Robert Morris (OT)",
    "Baylor", "Sam Houston State", "Purdue", "Siena", "Texas A&M", "Utah State",
    "Old Dominion", "Notre Dame", "Saint Mary's", "Richmond", "California", "Louisville",
    "Kansas", "Lehigh", "Ohio State", "UC Santa Barbara", "Ohio", "Georgetown",
    "Maryland", "Houston", "Michigan State", "New Mexico State", "Tennessee", "San Diego State",
    "Georgia Tech", "Oklahoma State", "Northern Iowa", "UNLV"
]

team_dict10 = {team: 0 for team in Schools10}

Schools11 = [
    "Ohio State", "UTSA", "North Carolina", "Long Island", "Syracuse", "Indiana State",
    "Kentucky", "Princeton", "West Virginia", "Clemson", "Marquette", "Xavier",
    "Washington", "Georgia", "George Mason", "Villanova", "Duke", "Hampton",
    "San Diego State", "Northern Colorado", "UConn", "Bucknell", "Texas", "Oakland",
    "Arizona", "Memphis", "Cincinnati", "Missouri", "Temple", "Penn State",
    "Michigan", "Tennessee", "Kansas", "Boston University", "Notre Dame", "Akron",
    "Purdue", "Saint Peter's", "Morehead State", "Louisville", "Richmond", "Vanderbilt",
    "VCU", "Georgetown", "Florida State", "Texas A&M", "Illinois", "UNLV",
    "Pitt", "UNC Asheville", "Florida", "UC Santa Barbara", "BYU", "Wofford",
    "Wisconsin", "Belmont", "Kansas State", "Utah State", "Gonzaga", "St. John's",
    "UCLA", "Michigan State", "Butler", "Old Dominion"
]

team_dict11 = {team: 0 for team in Schools11}


Schools12 = [
    "Syracuse", "UNC Asheville", "Ohio State", "Loyola (Md.)", "Florida State", "St. Bonaventure",
    "Wisconsin", "Montana", "Vanderbilt", "Harvard", "Cincinnati", "Texas", "Gonzaga", "West Virginia",
    "Kansas State", "Southern Miss", "Michigan State", "Long Island", "Norfolk State", "Missouri",
    "Marquette", "BYU", "Louisville", "Davidson", "New Mexico", "Long Beach State", "Murray State",
    "Colorado State", "Florida", "Virginia", "Saint Louis", "Memphis", "Kentucky", "Western Kentucky",
    "Lehigh", "Duke", "Baylor", "South Dakota State", "Indiana", "New Mexico State", "VCU", "Wichita State",
    "Colorado", "UNLV", "Xavier", "Notre Dame", "Iowa State", "UConn", "North Carolina", "Vermont",
    "Kansas", "Detroit", "Georgetown", "Belmont", "Ohio", "Michigan", "South Florida", "Temple", "NC State",
    "San Diego State", "Purdue", "Saint Mary's", "Creighton", "Alabama"
]

team_dict12 = {team: 0 for team in Schools12}

Schools13 = [
    "Louisville", "North Carolina A&T", "Duke", "Albany", "Michigan State", "Valparaiso",
    "Saint Louis", "New Mexico State", "Oregon", "Oklahoma State", "Memphis", "Saint Mary's",
    "Creighton", "Cincinnati", "Colorado State", "Missouri", "Gonzaga", "Southern", "Ohio State",
    "Iona", "Harvard", "New Mexico", "La Salle", "Kansas State", "Ole Miss", "Wisconsin", "Arizona",
    "Belmont", "Iowa State", "Notre Dame", "Wichita State", "Pittsburgh", "Indiana", "James Madison",
    "Miami (Fla.)", "Pacific", "Marquette", "Davidson", "Syracuse", "Montana", "California", "UNLV",
    "Butler", "Bucknell", "Illinois", "Colorado", "Temple", "NC State", "Kansas", "Western Kentucky",
    "Florida Gulf Coast", "Georgetown", "Florida", "Northwestern State", "Michigan", "South Dakota State",
    "VCU", "Akron", "Minnesota", "UCLA", "San Diego State", "Oklahoma", "North Carolina", "Villanova"
]

team_dict13 = {team: 0 for team in Schools13}

Schools14 = [
    "Wichita State", "Cal Poly", "Michigan", "Wofford", "Mercer", "Duke", "Louisville", "Manhattan",
    "Saint Louis", "NC State", "Tennessee", "UMass", "Texas", "Arizona State", "Kentucky", "Kansas State",
    "Arizona", "Weber State", "Wisconsin", "American", "Creighton", "Louisiana", "San Diego State",
    "New Mexico State", "North Dakota State", "Oklahoma", "Baylor", "Nebraska", "Oregon", "BYU",
    "Gonzaga", "Oklahoma State", "Virginia", "Coastal Carolina", "Villanova", "Milwaukee", "Iowa State",
    "North Carolina Central", "Michigan State", "Delaware", "Harvard", "Cincinnati", "North Carolina",
    "Providence", "UConn", "Saint Joseph's", "Memphis", "George Washington", "Florida", "Albany",
    "Kansas", "Eastern Kentucky", "Syracuse", "Western Michigan", "UCLA", "Tulsa", "Stephen F. Austin",
    "VCU", "Dayton", "Ohio State", "Stanford", "New Mexico", "Pittsburgh", "Colorado"
]

team_dict14 = {team: 0 for team in Schools14}

Schools15 = [
    "Kentucky", "Hampton", "Kansas", "New Mexico State", "Notre Dame", "Northeastern", "Maryland", "Valparaiso", 
    "West Virginia", "Buffalo", "Butler", "Texas", "Wichita State", "Indiana", "Cincinnati", "Purdue", "Wisconsin", 
    "Coastal Carolina", "Arizona", "Texas Southern", "Georgia State", "Baylor", "North Carolina", "Harvard", "Arkansas", 
    "Wofford", "Xavier", "Ole Miss", "Ohio State", "VCU", "Oregon", "Oklahoma State", "Villanova", "Lafayette", "Virginia", 
    "Belmont", "Oklahoma", "Albany", "Louisville", "UC Irvine", "Northern Iowa", "Wyoming", "Dayton", "Providence", 
    "Michigan State", "Georgia", "NC State", "LSU", "Duke", "Robert Morris", "Gonzaga", "North Dakota State", "UAB", 
    "Iowa State", "Georgetown", "Eastern Washington", "Utah", "Stephen F. Austin", "UCLA", "SMU", "Iowa", "Davidson", 
    "San Diego State", "St. John's"
]

team_dict15 = {team: 0 for team in Schools15}

Schools16 = [
    "North Carolina", "Florida Gulf Coast", "Xavier", "Weber State", "Stephen F. Austin", "West Virginia",
    "Kentucky", "Stony Brook", "Indiana", "Chattanooga", "Notre Dame", "Michigan",
    "Wisconsin", "Pittsburgh", "Providence", "Southern California", "Oregon", "Holy Cross",
    "Oklahoma", "Cal State Bakersfield", "Texas A&M", "Green Bay", "Duke", "UNC Wilmington",
    "Yale", "Baylor", "Northern Iowa", "Texas", "VCU", "Oregon State",
    "Saint Joseph's", "Cincinnati", "Kansas", "Austin Peay", "Villanova", "UNC Asheville",
    "Miami (Fla.)", "Buffalo", "Hawai'i", "California", "Maryland", "South Dakota State",
    "Wichita State", "Arizona", "Iowa", "Temple", "UConn", "Colorado",
    "Virginia", "Hampton", "Middle Tennessee", "Michigan State", "Utah", "Fresno State",
    "Iowa State", "Iona", "Little Rock", "Purdue", "Gonzaga", "Seton Hall",
    "Syracuse", "Dayton", "Butler", "Texas Tech"
]

team_dict16 = {team: 0 for team in Schools16}

Schools17 = [
    "Villanova", "Mount St. Mary's", "Duke", "Troy", "Baylor", "New Mexico State", "Florida", "East Tennessee State",
    "Virginia", "UNC Wilmington", "Southern California", "SMU", "South Carolina", "Marquette", "Wisconsin", "Virginia Tech",
    "Gonzaga", "South Dakota State", "Arizona", "North Dakota", "Florida State", "Florida Gulf Coast", "West Virginia", "Bucknell",
    "Notre Dame", "Princeton", "Xavier", "Maryland", "Saint Mary's", "VCU", "Northwestern", "Vanderbilt",
    "North Carolina", "Texas Southern", "Kentucky", "Northern Kentucky", "UCLA", "Kent State", "Butler", "Winthrop",
    "Middle Tennessee", "Minnesota", "Cincinnati", "Kansas State", "Wichita State", "Dayton", "Arkansas", "Seton Hall",
    "Kansas", "UC Davis", "Louisville", "Jacksonville State", "Oregon", "Iona", "Purdue", "Vermont",
    "Iowa State", "Nevada", "Rhode Island", "Creighton", "Michigan", "Oklahoma State", "Michigan State", "Miami (Fla.)"
]

team_dict17 = {team: 0 for team in Schools17}


Schools18 = [
    "Villanova", "Radford", "Purdue", "Cal State Fullerton", "Texas Tech", "Stephen F. Austin", 
    "Marshall", "Wichita State", "West Virginia", "Murray State", "Florida", "St. Bonaventure", 
    "Butler", "Arkansas", "Alabama", "Virginia Tech",
    "Xavier", "Texas Southern", "North Carolina", "Lipscomb", "Michigan", "Montana", "Gonzaga", 
    "UNC Greensboro", "Ohio State", "South Dakota State", "Houston", "San Diego State", 
    "Texas A&M", "Providence", "Florida State", "Missouri", "UMBC", "Virginia", "Cincinnati", 
    "Georgia State", "Tennessee", "Wright State", "Buffalo", "Arizona", "Kentucky", "Davidson", 
    "Loyola Chicago", "Miami (Fla.)", "Nevada", "Texas", "Kansas State", "Creighton", "Kansas", 
    "Pennsylvania", "Duke", "Iona", "Michigan State", "Bucknell", "Auburn", "College of Charleston", 
    "Clemson", "New Mexico State", "Syracuse", "TCU", "Rhode Island", "Oklahoma", "Seton Hall", 
    "NC State"
]

team_dict18 = {team: 0 for team in Schools18}

Schools19 = [
    "Duke", "North Dakota State", "Michigan State", "Bradley", "LSU", "Yale", 
    "Virginia Tech", "Saint Louis", "Liberty", "Mississippi State", "Maryland", "Belmont", 
    "Minnesota", "Louisville", "UCF", "VCU",
    "Gonzaga", "Fairleigh Dickinson", "Michigan", "Montana", "Texas Tech", "Northern Kentucky", 
    "Florida State", "Vermont", "Murray State", "Marquette", "Buffalo", "Arizona State", 
    "Florida", "Nevada", "Baylor", "Syracuse",
    "Virginia", "Gardner-Webb", "Tennessee", "Colgate", "Purdue", "Old Dominion", "UC Irvine", 
    "Kansas State", "Oregon", "Wisconsin", "Villanova", "Saint Mary's", "Iowa", "Temple", 
    "Oklahoma", "Ole Miss",
    "North Carolina", "Iona", "Kentucky", "Abilene Christian", "Houston", "Georgia State", 
    "Kansas", "Northeastern", "Auburn", "New Mexico State", "Ohio State", "Iowa State", 
    "Wofford", "Seton Hall", "Washington", "Utah State"
]

team_dict19 = {team: 0 for team in Schools19}


Schools21 = [
    "Illinois", "Drexel", "Loyola Chicago", "Georgia Tech", "Oregon St.", "Tennessee", 
    "Oklahoma St.", "Liberty", "Syracuse", "San Diego St.", "West Virginia", "Morehead St.", 
    "Rutgers", "Clemson", "Houston", "Cleveland St.", "Gonzaga", "Norfolk St.", "Oklahoma", 
    "Missouri", "Creighton", "UCSB", "Ohio", "Virginia", "USC", "Drake", "Kansas", 
    "Eastern Wash.", "Oregon", "VCU", "Iowa", "Grand Canyon", "Michigan", "Texas Southern", 
    "LSU", "St. Bonaventure", "Colorado", "Georgetown", "Florida St.", "UNC Greensboro", 
    "UCLA", "BYU", "Abilene Christian", "Texas", "Maryland", "UConn", "Alabama", "Iona", 
    "Baylor", "Hartford", "Wisconsin", "North Carolina", "Villanova", "Winthrop", "North Texas", 
    "Purdue", "Texas Tech", "Utah St.", "Arkansas", "Colgate", "Florida", "Virginia Tech", 
    "Oral Roberts", "Ohio State"
]

team_dict21 = {team: 0 for team in Schools21}

Schools22 = [
    "Kansas", "Texas Southern", "Creighton", "San Diego St.", "Richmond", "Iowa", "Providence", 
    "S. Dakota St.", "Iowa St.", "LSU", "Wisconsin", "Colgate", "Miami (FL)", "USC", "Auburn", 
    "Jacksonville St.", "Gonzaga", "Georgia St.", "Memphis", "Boise St.", "New Mexico St.", 
    "UConn", "Arkansas", "Vermont", "Notre Dame", "Alabama", "Texas Tech", "Montana St.", 
    "Michigan St.", "Davidson", "Duke", "Cal St. Fullerton", "Baylor", "Norfolk St.", 
    "North Carolina", "Marquette", "Saint Mary’s", "Indiana", "UCLA", "Akron", "Texas", 
    "Virginia Tech", "Purdue", "Yale", "Murray St.", "San Francisco", "St. Peter’s", "Kentucky",
     "Arizona", "Wright St.", "TCU", "Seton Hall", "Houston", "UAB", "Illinois", "Chattanooga", 
    "Michigan", "Colorado St.", "Tennessee", "Longwood", "Ohio St.", "Loyola Chicago", 
    "Villanova", "Delaware"
]

team_dict22 = {team: 0 for team in Schools22}

Schools23 = [
    "Houston", "North Kentucky", "Auburn", "Iowa", "Miami (FL)", "Drake", "Indiana", "Kent St.", 
    "Pitt", "Iowa St.", "Xavier", "Kennesaw St.", "Penn St.", "Texas A&M", "Texas", "Colgate", 
    "Kansas", "Howard", "Arkansas", "Illinois", "St. Mary’s", "VCU", "UConn", "Iona", 
    "TCU", "Arizona St.", "Gonzaga", "Grand Canyon", "Northwestern", "Boise St.", "UCLA", 
    "UNC Asheville", "FDU", "Purdue", "FAU", "Memphis", "Duke", "Oral Roberts", "Tennessee", 
    "Louisiana", "Kentucky", "Providence", "Kansas St.", "Montana St.", "Michigan St.", 
    "USC", "Marquette", "Vermont", "Alabama", "Texas A&M-CC", "Maryland", "West Virginia", 
    "San Diego St.", "Col of Charleston", "Furman", "Virginia", "Creighton", "NC State", 
    "Baylor", "UCSB", "Missouri", "Utah St.", "Princeton", "Arizona"
]

team_dict23 = {team: 0 for team in Schools23}