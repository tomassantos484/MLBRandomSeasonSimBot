import random
import tweepy
from credentials import *
from PlayerNameAL import *
from PlayerNameNL import *
from MLBTeams import *
from BaseballPositions import *

#Variables/Stats 
QualifiedPA = 600

AvgAB = 530

SacFlies = int(round(QualifiedPA * (random.uniform(0.00,0.0138))))

SacBunts = int(round(QualifiedPA * (random.uniform(0.00,0.0134))))

Strikeouts = int(round(AvgAB * (random.uniform(0.0710,0.3430))))

Groundouts = int(round(AvgAB * (random.uniform(0.1620,0.3260))))

Popouts = int(round(AvgAB * (random.uniform(0.0113,0.1230))))

Flyouts = int(round(AvgAB * (random.uniform(0.1008,0.2230))))

Lineouts = int(round(AvgAB * (random.uniform(0.0354,0.1101))))

HBP = int(round(QualifiedPA* (random.uniform(0.00,0.0516))))

ROE = int(round(AvgAB*random.uniform(0.00,0.0182)))

Outs = int(Strikeouts + Groundouts + Popouts + Flyouts + Lineouts)

Singles = int(round(AvgAB * (random.uniform(0.0824,0.2206))))

Doubles = int(round(AvgAB * (random.uniform(0.0437,0.0663))))

Triples = int(round(AvgAB * (random.uniform(0.00,0.0134))))

HomeRuns = int(round(AvgAB* (random.uniform(0.00,0.09))))

Walks = int(round(QualifiedPA*(random.uniform(0.0330,0.2030))))

Hits = int(Singles + Doubles + Triples + HomeRuns)

TB = int((Singles) + (Doubles * 2) + (Triples * 3) + (HomeRuns * 4))

AB = int(Hits + ROE + Outs)

PA = int(Hits + ROE + Outs + Walks + HBP + SacFlies + SacBunts)

Runs = int(round(HomeRuns + (PA * random.uniform(0.07,0.18))))

BA = round(Hits/AB, 4)

OBP =  round((Hits + Walks + HBP)/(AB + Walks + HBP + SacFlies), 3)

Slugging = round(TB/AB,3)

lgOBP = .312

lgSLG = .395

lgOPS = lgOBP + lgSLG

ops_plus = int(round(100*((OBP/lgOBP)+(Slugging/lgSLG) -1)))

RBI = int(round(HomeRuns + (AB * random.uniform(0.07,0.24))))

SBAttempts = 37 #Top 10 Base Stealers by Total Stolen Bases attempted an avg of 37 SB Attempts in 2022.

SB = int(round(SBAttempts * (random.uniform(0,0.90))))

CS = int(round(SBAttempts * (random.uniform(0,0.30))))

OPS = round(OBP + Slugging, 3)

PlayerAge = random.randrange(17,49) #Mel Ott (youngest HOF to play at 17 in 1926) and Julio Franco (oldest player to receive regular playing time at age 49 in 2007) are the extremes in this age range.

##################################################################                                                                                                                                                  

# List of player names
first_name = (MLB_FirstNames)
last_name = (MLB_LastNames)

#List of MLB Teams
MLBTeam = (Teams)

# Function to generate a random player
def random_player():
    return {
        "firstname": random.choice(first_name),
        "lastname": random.choice(last_name),
        "age": PlayerAge,
        "team": random.choice(MLBTeam),
        "position": random.choice(Positions)
    }

# Function to generate random statistics (batters)
def random_stats():
    return {
        "batting_average": BA,
        "home_runs": HomeRuns,
        "rbi": RBI,
        "strikeouts": Strikeouts,
        "walks": Walks,
        "hitbypitch": HBP,
        "runs": Runs,
        "hits": Hits,
        "doubles": Doubles,
        "triples": Triples,
        "homeruns": HomeRuns,
        "totalbases": TB,
        "ops+": ops_plus,
        "pa": PA,
        "ab": AB,
        'obp': OBP,
        'slg': Slugging,
        "ops": OPS,
        "stolenbases": SB,
        "caughtstealing": CS

    }
# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Generate random player and statistics
player = random_player()
stats = random_stats()

# Compose tweet
tweet = f"\n {player['firstname']} {player['lastname']} \nAge: {player['age']} \nPosition: {player['position']} \nTeam: {player['team']} \nPA: {stats['pa']} \nAB: {stats['ab']} \nRuns: {stats['runs']} \nHits: {stats['hits']} \nDoubles: {stats['doubles']} \nTriples: {stats['triples']} \nHome Runs: {stats['homeruns']} \nRBI: {stats['rbi']}\nSB: {stats['stolenbases']}\nCS: {stats['caughtstealing']} \nBB: {stats['walks']} \nSO {stats['strikeouts']} \nBA: {stats['batting_average']} \nOBP: {stats['obp']} \nSLG: {stats['slg']} \nOPS: {stats['ops']} \nOPS+: {stats['ops+']}"

# Post tweet
api.update_status(tweet)

print("New Player Generated!")