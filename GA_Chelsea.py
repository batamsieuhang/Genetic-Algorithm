import copy
from random import randrange, sample

# player position
# GK-GoalKeeper
# DF-Defender
# CM-Central Midfielder
# AT-Attacker

value_cap = 500  # limit for sum value 11-squad
pop_size = 20  # population size


player_chelsea = {
    "GK": {
        "Edouard Mendy": {
            "name": "Edouard Mendy",
            "position": "GK",
            "rating": 6.5,
            "value": 25,
            "flag": 0
        },
        "Kepa Arrizabalaga": {
            "name": "Kepa Arrizabalaga",
            "position": "GK",
            "rating": 7.02,
            "value": 15,
            "flag": 0
        },
        "Marcus Bettinelli": {
            "name": "Marcus Bettinelli",
            "position": "GK",
            "rating": 5.0,
            "value": 2,
            "flag": 0
        },
    },
    "DF": {
        "Wesley Fofana": {
            "name": "Wesley Fofana",
            "position": "DF",
            "rating": 7.48,
            "value": 65,
            "flag": 0
        },
        "Kalidou Koulibaly": {
            "name": "Kalidou Koulibaly",
            "position": "DF",
            "rating": 6.82,
            "value": 35,
            "flag": 0
        },
        "Trevoh Chalobah": {
            "name": "Trevoh Chalobah",
            "position": "DF",
            "rating": 6.94,
            "value": 22,
            "flag": 0
        },
        "Thiago Silva": {
            "name": "Thiago Silva",
            "position": "DF",
            "rating": 6.93,
            "value": 2,
            "flag": 0
        },
        "Marc Cucurella": {
            "name": "Marc Cucurella",
            "position": "DF",
            "rating": 6.54,
            "value": 55,
            "flag": 0
        },
        "Ben Chilwell": {
            "name": "Ben Chilwell",
            "position": "DF",
            "rating": 6.97,
            "value": 38,
            "flag": 0
        },
        "Reece James": {
            "name": "Reece James",
            "position": "DF",
            "rating": 7.19,
            "value": 70,
            "flag": 0
        },
        "César Azpilicueta": {
            "name": "César Azpilicueta",
            "position": "DF",
            "rating": 6.29,
            "value": 8,
            "flag": 0
        },
    },
    "CM": {
        "Denis Zakaria": {
            "name": "Denis Zakaria",
            "position": "CM",
            "rating": 7.51,
            "value": 20,
            "flag": 0
        },
        "N\'Golo Kanté": {
            "name": "N\'Golo Kanté",
            "position": "CM",
            "rating": 7.2,
            "value": 30,
            "flag": 0
        },
        "Enzo Fernández": {
            "name": "Enzo Fernández",
            "position": "CM",
            "rating": 6.81,
            "value": 55,
            "flag": 0
        },
        "Mateo Kovacic": {
            "name": "Mateo Kovacic",
            "position": "CM",
            "rating": 6.85,
            "value": 40,
            "flag": 0
        },
        "Conor Gallagher": {
            "name": "Conor Gallagher",
            "position": "CM",
            "rating": 6.57,
            "value": 32,
            "flag": 0
        },
        "Ruben Loftus-Cheek": {
            "name": "Ruben Loftus-Cheek",
            "position": "CM",
            "rating": 6.6,
            "value": 25,
            "flag": 0
        },
        "Mason Mount": {
            "name": "Mason Mount",
            "position": "CM",
            "rating":  6.89,
            "value": 75,
            "flag": 0
        },
        "Kai Havertz": {
            "name": "Kai Havertz",
            "position": "CM",
            "rating": 6.75,
            "value": 70,
            "flag": 0
        },
    },
    "AT": {
        "Raheem Sterling": {
            "name": "Raheem Sterling",
            "position": "AT",
            "rating": 6.66,
            "value": 70,
            "flag": 0
        },
        "Mykhaylo Mudryk": {
            "name": "Mykhaylo Mudryk",
            "position": "AT",
            "rating": 6.15,
            "value": 40,
            "flag": 0
        },
        "Christian Pulisic": {
            "name": "Christian Pulisic",
            "position": "AT",
            "rating": 6.31,
            "value": 24,
            "flag": 0
        },
        "Hakim Ziyech": {
            "name": "Hakim Ziyech",
            "position": "AT",
            "rating": 6.47,
            "value": 20,
            "flag": 0
        },
        "Noni Madueke": {
            "name": "Noni Madueke",
            "position": "AT",
            "rating": 6.77,
            "value": 15,
            "flag": 0
        },
        "João Félix": {
            "name": "João Félix",
            "position": "AT",
            "rating": 6.55,
            "value": 50,
            "flag": 0
        },
        "Armando Broja": {
            "name": "Armando Broja",
            "position": "AT",
            "rating": 6.29,
            "value": 30,
            "flag": 0
        },
        "Pierre-Emerick Aubameyang": {
            "name": "Pierre-Emerick Aubameyang",
            "position": "AT",
            "rating": 6.15,
            "value": 12,
            "flag": 0
        },
        "David Datro Fofana": {
            "name": "David Datro Fofana",
            "position": "AT",
            "rating": 6.61,
            "value": 7,
            "flag": 0
        },
    },


}

bit_string_player = []


for pos in player_chelsea.values():
    # create bit string for squad
    bit_string_player.append([index['flag'] for index in pos.values()])


"""
Create random bits string in teamsquad for each postion with number player
"""


def Ran_pos(team, position, num_player):
    if (position == "GK"):
        for i in range(num_player):
            team[0][randrange(int(len(team[0])))] = 1
    if (position == "DF"):
        flag = 0
        index = sample(range(int(len(team[1]))), num_player)
        print(index)
        for i in index:
            team[1][i] = 1
    if (position == "CM"):
        flag = 0
        index = sample(range(int(len(team[2]))), num_player)
        print(index)
        for i in index:
            team[2][i] = 1
    if (position == "AT"):
        flag = 0
        index = sample(range(int(len(team[3]))), num_player)
        print(index)
        for i in index:
            team[3][i] = 1
    return team


def sum_value(team):  # sum of value 11-squad
    value = 0
    for i in range(int(len(team))):
        if i == 0:
            index = 0
            for players in player_chelsea["GK"].values():
                if (team[i][index]) == 1:
                    value += players['value']
                index += 1
        if i == 1:
            index = 0
            for players in player_chelsea["DF"].values():
                if (team[i][index]) == 1:
                    value += players['value']
                index += 1
        if i == 2:
            index = 0
            for players in player_chelsea["CM"].values():
                if (team[i][index]) == 1:
                    value += players['value']
                index += 1
        if i == 3:
            index = 0
            for players in player_chelsea["AT"].values():
                if (team[i][index]) == 1:
                    value += players['value']
                index += 1
    return value

# create population


def intial_seed(team):
    teams = []
    for i in range(pop_size):
        while True:
            team = copy.deepcopy(bit_string_player)
            Ran_pos(team,
                    position="GK", num_player=1)
            Ran_pos(team,
                    position="DF", num_player=4)
            Ran_pos(team,
                    position="CM", num_player=4)
            Ran_pos(team,
                    position="AT", num_player=3)
            if (sum_value(team) <= value_cap):
                teams.append(team)
                break
    for team in teams:
        print(team)
        print(sum_value(team))
        print("\n")
    print(len(teams))
    return teams


intial_seed(team=bit_string_player)
