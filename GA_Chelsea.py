import copy
import random
from data import player_chelsea
from random import randrange, sample


value_cap = 550  # limit for sum value 11-squad
pop_size = 1000  # population size


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
        for i in index:
            team[1][i] = 1
    if (position == "CM"):
        flag = 0
        index = sample(range(int(len(team[2]))), num_player)
        for i in index:
            team[2][i] = 1
    if (position == "AT"):
        flag = 0
        index = sample(range(int(len(team[3]))), num_player)
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
    return team_information


intial_seed(team=bit_string_player)


team_information = intial_seed(team=bit_string_player)
team_information = sorted_dict = dict(
    sorted(team_information.items(), key=lambda x: x[1]['rating'], reverse=True))
# print(team_information)
# for squad in team_information.values():
#     print(squad)


"""selection function"""


def selection(population):
    fitness_scores = [individual['rating']
                      for individual in population.values()]
    total_fitness = sum(fitness_scores)
    selection_probabilities = [
        score / total_fitness for score in fitness_scores]

    selected = []
    for i in range(len(population)):
        cumulative_probability = 0
        r = random.uniform(0, 1)
        for j in range(len(population)):
            cumulative_probability += selection_probabilities[j]
            if cumulative_probability > r:
                selected.append(population[j])
                break
    return selected


selection_choices = sorted(selection(team_information),
                           key=lambda x: x['rating'], reverse=False)


new_selection = []

for selection in selection_choices:
    if selection not in new_selection:
        new_selection.append(selection)
        print(selection)

# crossover function


def crossover(parent1, parent2):
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)
    crossover_point = random.randint(1, len(child1['squad']) - 1)
    for i in range(crossover_point, len(child1['squad'])):
        child1['squad'][i], child2['squad'][i] = child2['squad'][i], child1['squad'][i]
    return child1, child2


parent1, parent2 = random.sample(selection_choices, 2)
child1, child2 = crossover(parent1, parent2)

print(child1, '\n', child2)


# mutation function:
