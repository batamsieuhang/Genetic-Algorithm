import copy
from data import player_chelsea
from random import randrange, sample

# player position
# GK-GoalKeeper
# DF-Defender
# CM-Central Midfielder
# AT-Attacker

value_cap = 500  # limit for sum value 11-squad
pop_size = 20  # population size


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


def sum_rating(team):  # sum of value 11-squad
    rating = 0
    for i in range(int(len(team))):
        if i == 0:
            index = 0
            for players in player_chelsea["GK"].values():
                if (team[i][index]) == 1:
                    rating += players['rating']
                index += 1
        if i == 1:
            index = 0
            for players in player_chelsea["DF"].values():
                if (team[i][index]) == 1:
                    rating += players['rating']
                index += 1
        if i == 2:
            index = 0
            for players in player_chelsea["CM"].values():
                if (team[i][index]) == 1:
                    rating += players['rating']
                index += 1
        if i == 3:
            index = 0
            for players in player_chelsea["AT"].values():
                if (team[i][index]) == 1:
                    rating += players['rating']
                index += 1
    return rating


# create population
def intial_seed(team):
    teams = []
    team_information = {}
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
                teams.append(team)  # include Fitness evaluation
                break
    index = 0
    for team in teams:
        team_information[index] = {"squad": team, "value": sum_value(
            team), "rating": sum_rating(team)}
        index += 1

    print(len(teams))
    print(team_information)
    return team_information


intial_seed(team=bit_string_player)
