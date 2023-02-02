# -*- coding: UTF-8 -*-

#A small team simulator that will base a 24-team season that ends in a tournament at the end. Injuries, team names, previous defeats, and more is required.

import names

import random

from random_word import RandomWords

import time

import cursor

import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import mixer

cursor.hide()

mixer.init()

mixer.music.load("crit.mp3")

 

rands = RandomWords()

week = 0

title = """

░██╗░░░░░░░██╗██████╗░███████╗░██████╗████████╗██╗░░░░░██╗███╗░░██╗░██████╗░

░██║░░██╗░░██║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██║░░░░░██║████╗░██║██╔════╝░

░╚██╗████╗██╔╝██████╔╝█████╗░░╚█████╗░░░░██║░░░██║░░░░░██║██╔██╗██║██║░░██╗░

░░████╔═████║░██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██║░░░░░██║██║╚████║██║░░╚██╗

░░╚██╔╝░╚██╔╝░██║░░██║███████╗██████╔╝░░░██║░░░███████╗██║██║░╚███║╚██████╔╝

░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░

 

░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░

██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗

╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝

░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗

██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║

╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

"""

#These are ASCII escape characters that will color the text when used properly.





#needed for mosts funcitons

 

#Wrestling is held in a meet style, one team versus the other. In a meet, it is two teams versus each other. ONLY ONE WRESTLER CAN BE IN EACH WEIGHT CLASS IN A MEET.

 

class bcolors:

    HEADER = '\033[95m' #purple

    OKBLUE = '\033[94m' #blue

    OKCYAN = '\033[96m' #cyan

    OKGREEN = '\033[92m' #green

    WARNING = '\033[93m' #WARNING

    FAIL = '\033[91m' #RED?

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'

 

class Team:

    def __init__(self, name, players):

        self.name = name

        self.players = players

        self.rank = 0

        self.teamRank = 0

        self.teamPercentage = 0

        self.teamHistory = []

        self.wins = 0

        self.losses = 0

        self.gamesPlayed = 0

        self.gamesScheduled = 0

       

    def dropPlayer(self, player):

        del self.players[player]

        print("Removed player")

 

class Player:

    def __init__(self, name, history, isInjured, ranking, seed, team):

        self.name = name

        self.history = history

        self.isInjured = isInjured

        self.ranking = ranking

        self.seed = seed

        self.weight = random.randint(106, 240)

        self.WeightClass = 106

        self.team = team

        self.matchesPlayed = 0

        self.playedRecently = False

        self.stats = {

            "Speed" : (random.randint(random.randint(50,90), 100)/100),

            "Strength" : (random.randint(random.randint(50,90), 100)/100),

            "Stamina" : (random.randint(random.randint(50,90), 100)/100)

        }

    def getRanking(self):

        return round(self.stats["Speed"] + self.stats["Strength"] + self.stats["Stamina"],2)

 

class Match:

    def __init__(self, team1, team2):

        self.team1name = team1

        self.team1obj = findTeamByName(team1)

        self.team2obj = findTeamByName(team2)

        self.team2name = team2

        self.team1s = {

         '106' : [],

         '113' : [],

         '120' : [],

         '126' : [],

         '132' : [],

         '145' : [],

         '152' : [],

         '160' : [],

         '170' : [],

         '182' : [],

         '195' : [],

         '220' : [],

         '285' : [],

        }

        self.team2s = {

        '106' : [],

         '113' : [],

         '120' : [],

         '126' : [],

         '132' : [],

         '145' : [],

         '152' : [],

         '160' : [],

         '170' : [],

         '182' : [],

         '195' : [],

         '220' : [],

         '285' : [],

        }

        self.outcome = "neutral"

        self.pointValue = 2

        self.playingClasses = []

 

#Script

#begins

#HERE!

injuredPlayers = {

 

}

 

def getrandomName():

   

    return names.get_full_name()

 

speedMode = False

 

Season = [

 

]

 

Classes = {

    '106' : [],

    '113' : [],

    '120' : [],

    '126' : [],

    '132' : [],

    '145' : [],

    '152' : [],

    '160' : [],

    '170' : [],

    '182' : [],

    '195' : [],

    '220' : [],

    '285' : [],

 

}

 

leaderboard =  {

 

}

 

leaderboardStyles = {

    "5":{

        "1": bcolors.OKGREEN,

        "2": bcolors.OKGREEN,

        "3": bcolors.WARNING,

        "4": bcolors.FAIL,

        "5": bcolors.FAIL

    },

    "6":{

        "1": bcolors.OKGREEN,

        "2": bcolors.OKGREEN,

        "3": bcolors.WARNING,

        "4": bcolors.WARNING,

        "5": bcolors.FAIL,

        "6": bcolors.FAIL

 

    },

    "7":{

        "1": bcolors.OKGREEN,

        "2": bcolors.OKGREEN,

        "3": bcolors.OKGREEN,

        "4": bcolors.WARNING,

        "5": bcolors.WARNING,

        "6": bcolors.FAIL,

        "7": bcolors.FAIL

 

    },

    "8":{

        "1": bcolors.OKGREEN,

        "2": bcolors.OKGREEN,

        "3": bcolors.OKGREEN,

        "4": bcolors.WARNING,

        "5": bcolors.WARNING,

        "6": bcolors.FAIL,

        "7": bcolors.FAIL,

        "8": bcolors.FAIL

 

    },

    "9":{

        "1": bcolors.OKGREEN,

        "2": bcolors.OKGREEN,

        "3": bcolors.OKGREEN,

        "4": bcolors.WARNING,

        "5": bcolors.WARNING,

        "6": bcolors.WARNING,

        "7": bcolors.FAIL,

        "8": bcolors.FAIL,

        "9": bcolors.FAIL

 

    },

    "10":{

        "1": bcolors.OKGREEN,

        "2": bcolors.OKGREEN,

        "3": bcolors.OKGREEN,

        "4": bcolors.WARNING,

        "5": bcolors.WARNING,

        "6": bcolors.WARNING,

        "7": bcolors.WARNING,

        "8": bcolors.FAIL,

        "9": bcolors.FAIL,

        "10": bcolors.FAIL

 

    }

}

nameLeaderboard = [

 

]

#used in the choosePlayers function to find teams by the names put in matches.

def findTeamByName(name):

 

    for team in Season:

        if team.name == name:

            return team

 

#Weight classes 106, 113, 120, 126, 132, 138, 145, 152, 160, 170, 182, 195, 220 and 285 pounds

 

def setWeightClass(player):

    global Classes

    pastClass = 0

    for weight in Classes:

       

        if player.weight <= int(weight) and player.weight > int(pastClass):

            player.WeightClass = int(weight)

            pastClass = weight

        else:

            pass

       

#prints the classes in a human-readable way

def printClasses():

    global Classes

    global speedMode

    for weightClass in Classes:

        print(bcolors.FAIL + "Those in the weight class of: " + weightClass + " are:" + bcolors.ENDC)

        if speedMode == False:

            time.sleep(2)

       

        if len(Classes[weightClass]) == 0:

            print(bcolors.HEADER + "No one!" + bcolors.ENDC)

        else:

            print("[" + bcolors.OKBLUE + "Name" + bcolors.ENDC + "-" + bcolors.OKGREEN + "Weight" + bcolors.ENDC + "-" + bcolors.OKCYAN + "Team" + bcolors.ENDC + "]")

            for player in Classes[weightClass]:

                if speedMode == False:

                    time.sleep(0.05)

                print(bcolors.OKBLUE + player.name + bcolors.ENDC + "-" + bcolors.OKGREEN + str(player.weight) + bcolors.ENDC + "-" + bcolors.OKCYAN + player.team + bcolors.ENDC)

       

 

#classes




MatchesObjects = {

 

}

MatchesNames = []

 

#checks weight classses for too low amounts of people.   

def checkWeightClasses():

    global Classes

    for weightClass in Classes:

        if len(Classes[weightClass]) < 3 and len(Classes[weightClass]) != 0:

            print(bcolors.HEADER + "The weight class of " + str(weightClass) + " has less than three people left. They will be reshuffled and the classes will be rechecked.")

            for player in Classes[weightClass]:

                print(player.name + " is being reset.")

                del Classes[str(player.WeightClass)][Classes[str(player.WeightClass)].index(player)]

                player.weight = random.randint(106, 285)

                setWeightClass(player)

                Classes[str(player.WeightClass)].append(player)

                print(bcolors.OKBLUE + player.name + " has been moved to weight class " + str(player.WeightClass) + ", with the weight of " + str(player.weight) + "." + bcolors.OKBLUE)

            checkWeightClasses()

 

#find a team by a percentage ranking. Used for sortTeams function

def findTeamByPercent(rank):

    for Team in Season:

        if Team.teamPercentage == rank:

            return Team

        else:

            pass

#sorts teams based on their percentage chance of winning.

def sortTeams():

    percentageList = [

 

    ]

    for Team in Season:

        percentageList.append(Team.teamPercentage)

       

    percentageList.sort()

    percentageList.reverse()

 

    for ind in range(len(percentageList)):

        leaderboard[ind] = findTeamByPercent(percentageList[ind])

    for team in leaderboard.values():

        nameLeaderboard.append(team.name)

 

#prints the final leaderboard along with who is in the game and who's in danger of being eliminated in the tournament.

def printLeaderboard():

    print(bcolors.OKCYAN + "LEADERBOARD" + bcolors.ENDC + "\n")

    style = leaderboardStyles[str(len(leaderboard))]

    for i in range(len(leaderboard)):

        time.sleep(1 + ((i + 1) / 10))

        print(bcolors.OKCYAN + "#" + str(i + 1) + bcolors.ENDC +  "-" + style[str(i + 1)] + leaderboard[i].name + bcolors.ENDC + "-" + bcolors.HEADER + str(leaderboard[i].teamPercentage) + "%" + bcolors.ENDC)

 

#creates a new team with a lot of players.

def generateNewTeam():

    global Classes

    players = [

 

    ]

    teamName = rands.get_random_word().capitalize()

    for i in range(random.randint(5, 13)):

        name = getrandomName()

        player = Player(name, [], False, 0, 0, teamName)

        players.append(player)

        setWeightClass(player)

        Classes[str(player.WeightClass)].append(player)

 

    team = Team(teamName, players)

    Season.append(team)

    print("\n" + bcolors.FAIL + "The roster for team " + team.name + " is..." + bcolors.ENDC + "\n")

    teamRank = 0.0

    for player1 in team.players:

        print(player1.name + "... " + bcolors.OKCYAN + "WITH A RANKING OF " + str(player1.getRanking()) + bcolors.ENDC)

        teamRank = teamRank + player1.getRanking()

        #time.sleep(1)

    print(bcolors.OKGREEN + "TOTAL TEAM RANKING: " + str(teamRank) + " out of: " + str(3 * len(team.players)) + " (" + str(len(team.players)) + " players), percentage rating is " + str(round((teamRank/(int(len(team.players)) * 3)) * 100, 1)) + "%" + bcolors.ENDC + "\n \n")

    team.teamPercentage =  str(round((teamRank/(int(len(team.players)) * 3)) * 100, 1))


 

def random_print(text, color, speed=False):

    global speedMode

    global week

    string = text

    lst = []

    lst.extend(string)

    printedstring = []

    printedstring.extend("*" * len(lst))

    print("\n")

    for i in range(len(printedstring)):

        if speed == False:

            time.sleep(0.01)

        print("".join(printedstring[:i]), end="\r")

    if speed == False:

        time.sleep(0.01/week)

    for i in range(len(lst)):

        if speed == False:

            time.sleep((random.randint(1, 2)/100))

        ind = random.randint(0, (len(lst) - 1))

        while printedstring[ind] != "*":

            ind = random.randint(0, (len(lst) -1))

       

        printedstring[ind] = lst[ind]

        print(color + "".join(printedstring) + bcolors.ENDC, end="\r")

    if speedMode == False:

        time.sleep(0.5)

   

 

def progress(percent=0, width=40):

    left = width * percent // 100

    right = width - left

   

    tags = "#" * left

    spaces = " " * right

    percents = f"{percent:.0f}%"

    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)





#chooses players for a set of matches that are generated.

def choosePlayers(matches):

    global week

    for i in range(len(matches)):

       

        

        split = matches[i].split(" vs. ")

        team1 = split[0]

        team2 = split[1]

        match = Match(team1, team2)

        playingClasses = [

 

        ]

        for wclass in Classes:

            team1has = False

            team2has = False

           

            for player in Classes[wclass]:

                if not wclass in playingClasses:

                    if player.team == team1 and team1has == False:

                        team1has = True

                    elif player.team == team2 and team2has == False:

                        team2has = True

                    if team1has == True and team2has == True:

                        playingClasses.append(wclass)

       

        print("Classes being played: ")

 

        print(",".join(playingClasses))

        match.playingClasses = playingClasses

        #time.sleep(2)

        for curclass in playingClasses:

            print(bcolors.FAIL + team1.upper() + " is choosing their players for the class: " + curclass + bcolors.ENDC + ", against team " + team2 + "\n")

 

            #finds most active player that isn't injured or has played the last match.

            bestChoice = ""

            highestStats = {

                "Speed" : 0,

                "Strength" : 0,

                "Stamina" : 0,

            }

            for player in findTeamByName(team1).players:

                if str(player.WeightClass) == str(curclass) and player.matchesPlayed < week + 1 and player.isInjured != True:

                    if player.stats["Strength"] > highestStats["Strength"] and player.stats["Speed"] > highestStats["Speed"]:

                        highestStats = player.stats

                        bestChoice = player

                    elif player.stats["Strength"] < highestStats["Strength"] and player.stats["Speed"] > highestStats["Speed"]:

                        highestStats = player.stats

                        bestChoice = player

                    elif player.stats["Strength"] < highestStats["Strength"] and player.stats["Speed"] < highestStats["Speed"] and player.stats["Stamina"] > highestStats["Stamina"]:

                        continue

                    elif player.stats["Strength"] < highestStats["Strength"] and player.stats["Speed"] > highestStats["Speed"] and player.stats["Stamina"] > highestStats["Stamina"]:

                        highestStats = player.stats

                        bestChoice = player

                else:

                    pass

            print(bcolors.WARNING + team1.upper() + "'s choice for weight class: " + curclass + " is...." + bcolors.ENDC + "\n")

            #time.sleep(0.2)

            try:

                random_print(bestChoice.name.upper() + "!!!!", bcolors.OKGREEN, True)

                bestChoice.isChosen = True

                match.team1s[curclass] = bestChoice

                print("\n")

            except AttributeError:

                print("No player in this class.")

        #team2Selections

        for curclass in playingClasses:

            print(bcolors.FAIL + team2.upper() + " is choosing their players for the class: " + curclass + bcolors.ENDC + ", against team " + team1 + "\n")

 

            #finds most active player that isn't injured or has played the last match.

            bestChoice = ""

            highestStats = {

                "Speed" : 0,

                "Strength" : 0,

                "Stamina" : 0,

            }

            for player in findTeamByName(team2).players:

                if str(player.WeightClass) == str(curclass) and player.matchesPlayed < week + 1:

                   

                    if player.stats["Strength"] > highestStats["Strength"] and player.stats["Speed"] > highestStats["Speed"]:

                        highestStats = player.stats

                        bestChoice = player

                    elif player.stats["Strength"] < highestStats["Strength"] and player.stats["Speed"] > highestStats["Speed"]:

                        highestStats = player.stats

                        bestChoice = player

                    elif player.stats["Strength"] < highestStats["Strength"] and player.stats["Speed"] < highestStats["Speed"] and player.stats["Stamina"] > highestStats["Stamina"]:

                        continue

                    elif player.stats["Strength"] < highestStats["Strength"] and player.stats["Speed"] > highestStats["Speed"] and player.stats["Stamina"] > highestStats["Stamina"]:

                        highestStats = player.stats

                        bestChoice = player

                   

                else:

                    pass

           

            print(bcolors.WARNING + team2.upper() + "'s choice for weight class: " + curclass + " is...." + bcolors.ENDC + "\n")

            #time.sleep(0.2)

            try:

                random_print(bestChoice.name.upper() + "!!!!", bcolors.OKGREEN, True)

                player.matchesPlayed += 1

                match.team2s[curclass] = bestChoice

               

 

                print("\n")

            except AttributeError:

                print("No player in this class, forfeit will be assigned.")

        MatchesObjects[matches[i]] = match

        MatchesNames.append(matches[i])

 

def findTeamByRecord(wins, losses):

    for Team in Season:

        if Team.wins == wins and Team.losses == losses:

            return Team

def displayResults():

    global Season

   

    teamRatings = {

 

    }

    for Team in Season:

        print(Team.wins)

        print(Team.losses)

        print("Games Played Below")

        print(Team.gamesPlayed)

        print(Team.name)

        rating = int(Team.wins) / int(Team.gamesPlayed)

      

        teamRatings[Team.name] = rating

 

    values = list(teamRatings.values())

 

    leaderBoard = [

 

    ]

    leaderboard_Sorted = sorted(teamRatings.items(), key=lambda x:x[1], reverse=True)

 

    print(dict(leaderboard_Sorted))

    leaderboard_Sorted = dict(leaderboard_Sorted)

    x = 0

    for key in leaderboard_Sorted.keys():

        x+=1

        random_print("#" + str(x) + " " +key+"-"+str(findTeamByName(key).wins)+"/"+str(findTeamByName(key).losses), bcolors.OKCYAN, False)

        for history in findTeamByName(key).teamHistory:

            if history.split(":")[1] == "W":

                random_print(history, bcolors.OKGREEN, False)

            elif history.split(":")[1] == "L":

                random_print(history, bcolors.FAIL, False)

            elif history.split(":")[1] == "T":

                random_print(history, bcolors.WARNING, False)

   

    print("\n")

 

       

 

       

   

 

    for team in leaderBoard:

        print(bcolors.FAIL + "#" + str(leaderBoard.index(team) + 1) + bcolors.ENDC + " " +  bcolors.WARNING + team + bcolors.ENDC + " " + str(findTeamByName(team).wins) + " / " + str(findTeamByName(team).losses))

 

def playMatches():

    global MatchesNames

    global Season

    for match in MatchesNames:

        curMatch = MatchesObjects[match]

        totalScore = {

            str(curMatch.team1name) : 0,

            str(curMatch.team2name) : 0

        }

        random_print("The match " + match + " is PLAYING NOW!", bcolors.FAIL, True)

        print("\n")

        t1w = 0

        t2w = 0

       

        for wclass in curMatch.playingClasses:

            try:

                player1 = curMatch.team1s[wclass]

            except AttributeError:

                print("Team one did not arrive with a proper player. Ending class match... FORFEIT")

                totalScore[curMatch.team1name] = 0

                totalScore[curMatch.team2name] = 3

                t2w += 1

                continue

            try:

                player2 = curMatch.team2s[wclass]

            except AttributeError:

                print("Team two did not arrive with a proper player. Ending class match. FORFIET")

                t1w += 1

                totalScore[curMatch.team1name] = 0

                totalScore[curMatch.team2name] = 3

                continue

            try:

                print(player1.name)

            except AttributeError:

                print("Player1 not found. Ending Class Match, FORFEIT.")

                totalScore[curMatch.team1name] = 0

                totalScore[curMatch.team2name] = 3

                t2w += 1

               continue

            try:

                print(player2.name)

            except AttributeError:

                print("Player2 not found. Ending Class Match, FORFEIT.")

                totalScore[curMatch.team1name] = 0

                totalScore[curMatch.team2name] = 3

                t1w += 1

                continue

            random_print("Contestants: " + player1.name + " vs. " + player2.name, bcolors.OKCYAN, True)

            print("\n")

            p1stats = player1.stats

            p2stats = player2.stats

            hstats={

            "Strength" : 0,

            "Stamina" : 0,

            "Speed" : 0

            }

            winners={

            "Strength" : "",

            "Stamina" : "",

            "Speed" : ""

            }

            p1w = 0

            p2w = 0

 

            #determine better stats

            players = [

                player1,

                player2

            ]

            for player in players:

                for stat in hstats:

                    if player.stats[stat] > hstats[stat]:

                        winners[stat] = player.name

                        hstats[stat] = player.stats[stat]

            print(hstats)

            print(winners)

            for winner in winners:

                if winners[winner] == player1.name:

                    p1w += 1

                elif winners[winner] == player2.name:

                    p2w += 1

            if p2w > p1w:

                random_print(player2.name + " WINS THE MATCH!!! (" + str(p1w) + "-" + str(p2w) + ")", bcolors.OKGREEN, True)

                print("\n")

                player1.history.append(player2.name)

                player2.history.append(player1.name)

                t2w += 1

            elif p1w > p2w:

                print(player1.name + " WINS THE MATCH!!! (" + str(p1w) + "-" + str(p2w) + ")", bcolors.OKGREEN, True)

                print("\n")

                player1.history.append(player2.name)

                player2.history.append(player1.name)

                t1w += 1

        if t2w > t1w:

            print(curMatch.team2name + " WON THE MATCH!!! (" + str(t1w) + "-" + str(t2w) + ")", bcolors.OKGREEN, True)

            print("\n")

            curMatch.team1obj.gamesPlayed += 1

            curMatch.team2obj.gamesPlayed += 1

            curMatch.team1obj.teamHistory.append(curMatch.team2name + ":L")

            curMatch.team1obj.losses += 1

            curMatch.team2obj.teamHistory.append(curMatch.team1name + ":W")

            curMatch.team2obj.wins += 1

        elif t1w > t2w:

            print(curMatch.team1name + " WON THE MATCH!!! (" + str(t1w) + "-" + str(t2w) + ")", bcolors.OKGREEN, True)

            print("\n")

            curMatch.team1obj.gamesPlayed += 1

            curMatch.team2obj.gamesPlayed += 1

            curMatch.team1obj.teamHistory.append(curMatch.team2name + ":W")

            curMatch.team1obj.wins += 1

            curMatch.team2obj.teamHistory.append(curMatch.team1name + ":L")

            curMatch.team2obj.losses += 1

        elif t1w == t2w:

            print(curMatch.team1name + " and " + curMatch.team2name + " TIED THE MATCH!!! (" + str(t1w) + "-" + str(t2w) + ")", bcolors.OKGREEN, True)

            print("\n")

            curMatch.team1obj.gamesPlayed += 1

            curMatch.team2obj.gamesPlayed += 1

            curMatch.team1obj.teamHistory.append(curMatch.team2name + ":T")

            curMatch.team1obj.losses += 1

            curMatch.team2obj.teamHistory.append(curMatch.team1name + ":T")

            curMatch.team2obj.losses += 1

        randomInjure = random.randint(1, 5)

 

        if randomInjure == 1:

            if isinstance(player1, Player):

                player1.isInjured = True

                injuredPlayers[player1] = random.randint(1, 3)

            else:

                print("Not a player")

        elif randomInjure == 2:

            if isinstance(player2, Player):

                player2.isInjured = True

                injuredPlayers[player2] = random.randint(1, 3)

            else:

                print("Not a player")

 

                

 

           

            

def checkForHistory(team, enemy):

    total = 0

    for history in team.teamHistory:

        print(history)

        print("History above")

        print(history.split(":")[0])

        print("Split Above")

       

        print(enemy)

        print("Enemy Above")

     

        if history.split(":")[0] == enemy:

            total+=1

    return total

           




    

#generates a few matches for a week

def generateMatches():

    global nameLeaderboard

    global Season

    global week

    print(nameLeaderboard)

    print(bcolors.WARNING + "MATCHES ARE BEING GENERATED")

    matches = [

 

    ]

    print("\n")

    teamsLeft = [

 

    ]

    for Team in Season:

        Team.gamesScheduled = 0

   

    for i in range(int(len(nameLeaderboard)/2)):

        progress(i, int(len(nameLeaderboard)/2))

        offset = random.randint(-(len(nameLeaderboard)), (len(nameLeaderboard)))

        m = ""

        isDone = False

        teamsLeft = []

        for Team in Season:

            print(Team.name)

            print(Team.gamesScheduled)

            if Team.gamesScheduled < 1:

                teamsLeft.append(Team)

           

        isSorting = False

        team1 = ""

        team2 = ""

        while team1 == team2:

            try:

                team1 = teamsLeft[random.randint(-len(teamsLeft), len(teamsLeft))].name

                team2 = teamsLeft[random.randint(-len(teamsLeft), len(teamsLeft))].name

            except IndexError:

                team1 = ""

                team2 =  ""

        print(team1)

        print("team1")

        print(team2)

        print("team2")

        team1obj = findTeamByName(team1)

        team2obj = findTeamByName(team2)

        print(team1obj, team2obj)

        while team1 == team2 and team1obj.gamesScheduled == 1 or team2obj.gamesScheduled == 1:

            try:

                team1 = teamsLeft[random.randint(-len(teamsLeft), len(teamsLeft))].name

                team2 = teamsLeft[random.randint(-len(teamsLeft), len(teamsLeft))].name

                team1obj = findTeamByName(team1)

                team2obj = findTeamByName(team2)

                print(team1obj.gamesScheduled)

                print("Found")

                continue

            except IndexError:

                team1 = ""

                team2 = ""

        print("Done")

        print(team1, team2)

        total = checkForHistory(findTeamByName(team1), team2)

        if int(total) > int(week - 1):

            while team1 == team2 and total > week - 1 and team1obj.gamesScheduled == 1 or team2obj.gamesScheduled == 1 and matches.find(team1 + " vs. " + team2) and team1obj.name != team2obj.name:

                try:

                    team1 = teamsLeft[random.randint(-len(teamsLeft), len(teamsLeft))].name

                    team2 = teamsLeft[random.randint(-len(teamsLeft), len(teamsLeft))].name

                    team1obj = findTeamByName(team1)

                    team2obj = findTeamByName(team2)

                    total = checkForHistory(findTeamByName(team1), team2)

                except IndexError:

                    team1 = ""

                    team2 = ""

        findTeamByName(team1).gamesScheduled += 1

        findTeamByName(team2).gamesScheduled += 1

        print(findTeamByName(team1).gamesScheduled)

        print(findTeamByName(team2).gamesScheduled)

        m = team1 + " vs. " + team2

       

        matches.append(m)

    print(matches)

   

    for match in matches:

        split = match.split(" vs. ")

 

        print(bcolors.OKCYAN + split[0] + bcolors.ENDC + " vs. " + bcolors.OKGREEN + split[1] + bcolors.ENDC + "\n")

    removePlayers = [

 

    ]

    for player in injuredPlayers:

        if injuredPlayers[player] > 0:

            injuredPlayers[player] = injuredPlayers[player] - 1

        else:

            player.isInjured = False

            removePlayers.append(injuredPlayers[player])

    for player in list(injuredPlayers,):

        if injuredPlayers[player] == 0:

            del injuredPlayers[player]

 

    return matches

 

def tournamentBrackets():

    teams = [

        "Hi",

        "Nosidfksfjh",

        "sdafjkgsahjfjasdgfkjashgf",

        "skjdhafjashdfkjdash",

        "team5",

        "team6",

        "team7",

        "team8",

        "team9",

        "team10"

 

    ]

    longest = 0


    for team in teams:

        if len(team) > longest:

            longest = len(team)

    longest += 5

    borderStrings = "-"

    print(f"""

 

    [{teams[0]}]{borderStrings * (longest - len(teams[0]))}|

    {" " * (longest + 2)}|-[{teams[0]}]{borderStrings * (longest - len(teams[0]))}|

    [{teams[1]}]{borderStrings * (longest - len(teams[1]))}|

        {" " * (2*(longest + 2))}|-[{teams[2]}]{borderStrings * (longest - len(teams[2]))}|

    [{teams[2]}]{borderStrings * (longest - len(teams[2]))}|

    {" " * (longest + 2)}|-[{teams[2]}]{borderStrings * (longest - len(teams[2]))}|

    [{teams[3]}]{borderStrings * (longest - len(teams[3]))}|

 

    [{teams[4]}]{borderStrings * (longest - len(teams[4]))}|

    {" " * (longest + 2)}|-[{teams[4]}]{borderStrings * (longest - len(teams[4]))}|

    [{teams[5]}]{borderStrings * (longest - len(teams[5]))}|

        {" " * (2*(longest + 2))}|-[{teams[5]}]{borderStrings * (longest - len(teams[5]))}|

    [{teams[6]}]{borderStrings * (longest - len(teams[6]))}|

    {" " * (longest + 2)}|-[{teams[7]}]{borderStrings * (longest - len(teams[7]))}|

    [{teams[7]}]{borderStrings * (longest - len(teams[7]))}|

        {" " * (2*(longest + 2))}|-[{teams[7]}]{borderStrings * (longest - len(teams[7]))}|

    [{teams[8]}]{borderStrings * (longest - len(teams[8]))}|

    {" " * (longest + 2)}|-[{teams[8]}]{borderStrings * (longest - len(teams[8]))}|

    [{teams[9]}]{borderStrings * (longest - len(teams[9]))}|

 

 

 

   

    

    """)







###THIS IS THE START OF THE PROGRAM.###

 

#tournamentBrackets()

 

print(title)

resp = input("Speed mode? y/n")

print(resp)

if resp.lower() == "y":

 

   speedMode = True

    print("Activated Speed Mode")

else:

 

    speedMode = False

print("\n The simulator will begin in two seconds.")

 

time.sleep(2)

num = random.randint(6, 10)

isEven = False

while isEven == False:

    print(num % 2 == 0)

 

    isEven = num % 2 == 0

    if isEven == False:

        num = random.randint(6, 10)

   

       

 

print(num)

for i in range(num):

    generateNewTeam()

   

 

print(bcolors.HEADER + "ALL THE TEAMS REGISTERED ARE: " + bcolors.ENDC)

 

for team in Season:

    print(bcolors.BOLD + team.name + bcolors.ENDC)

for weightClass in Classes:

    print(bcolors.FAIL + "Those in the weight class of: " + weightClass + " are:" + bcolors.ENDC)

    for player in Classes[weightClass]:

        print(bcolors.OKBLUE + player.name + bcolors.ENDC + "-" + bcolors.OKGREEN + str(player.weight) + bcolors.ENDC)

 

checkWeightClasses()

print("\n \n \n " + bcolors.WARNING + "THE NEW, OPTIMIZED CLASSES ARE: " + bcolors.ENDC + "\n\n")

printClasses()

print("\n\n\n" + bcolors.WARNING + "THE NEW, OPTIMIZED CLASSES ARE ABOVE ^^^" + bcolors.ENDC + "\n")

 

sortTeams()

printLeaderboard()

 

print(bcolors.HEADER + "ALL THE TEAMS REGISTERED ARE: " + bcolors.ENDC + "\n")

 

for team in Season:

    print(bcolors.BOLD + team.name + bcolors.ENDC)

 

for i in range(len(leaderboard)):

   

    week += 1

    sound2 = mixer.Sound('fallen.mp3')

   

 

    random_print("Week " + str(week) + " begins now! (Out of " + str(len(leaderboard)) + ")", bcolors.HEADER, True)

    random_print("The Injured:", bcolors.FAIL, False)

    sound2.play()

    if len(injuredPlayers) > 0:

        time.sleep(6)

    else:

        sound2.stop()

    for player in injuredPlayers:

       

        

 

        #mixer.music.play()

        random_print(player.name + "-" + player.team + "-Weeks Left:" + str(injuredPlayers[player]), bcolors.OKCYAN, False)

        time.sleep(25/len(injuredPlayers))

   

    total = 0

    for team in Season:

        for player in team.players:

            total += 1

    print("\n")

    print(bcolors.FAIL + str(total) + " REMAIN.")

 

   

    random_print("Would you like to skeep the week? (y/n)", bcolors.FAIL, False)

    resp = input("")

    print(resp)

    if resp.lower() == "y":

 

        speedMode = True

        print("Activated Speed Mode")

        time.sleep(2)

    else:

 

        speedMode = False

        print("Running normal time")

        time.sleep(2)

    print("\n")

    m   = generateMatches()

    choosePlayers(m)

    playMatches()

    displayResults()

    MatchesObjects = {}

 

    MatchesNames = []

 

tournamentBrackets()
