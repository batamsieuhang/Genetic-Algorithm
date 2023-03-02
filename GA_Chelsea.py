import copy
import random
import time
from data import player_chelsea, sum_rate_avg
from random import randrange, sample


value_cap = 550  # limit for sum value 11-squad
num_gen = 1000  # number of generation
pop_size = 300  # population size

bit_string_player = []


for pos in player_chelsea.values():
    # create bit string for squad
    bit_string_player.append([index['flag'] for index in pos.values()])


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

# print 11-squad


def print_squad(team):
    value = {}
    for i in range(int(len(team))):
        if i == 0:
            index = 0
            for players in player_chelsea["GK"].values():
                if (team[i][index]) == 1:
                    print(f"GK: {players['name']},")
                index += 1
        if i == 1:
            index = 0
            for players in player_chelsea["DF"].values():
                if (team[i][index]) == 1:
                    print(f"DF: {players['name']},")
                index += 1
        if i == 2:
            index = 0
            for players in player_chelsea["CM"].values():
                if (team[i][index]) == 1:
                    print(f"CM: {players['name']},")
                index += 1
        if i == 3:
            index = 0
            for players in player_chelsea["AT"].values():
                if (team[i][index]) == 1:
                    print(f"AT: {players['name']},")
                index += 1
    return 0


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


# Create random bits string in teamsquad for each postion with number player
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


# create population
def population(team):
    teams = []
    team_information = {}
    for i in range(num_gen):
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
    return team_information


population(team=bit_string_player)


team_information = population(team=bit_string_player)
team_information = sorted_dict = dict(
    sorted(team_information.items(), key=lambda x: x[1]['rating'], reverse=True))


# selection function
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


# crossover function
def crossover(parent1, parent2):
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)
    crossover_point = random.randint(1, len(child1['squad']) - 1)
    for i in range(crossover_point, len(child1['squad'])):
        child1['squad'][i], child2['squad'][i] = child2['squad'][i], child1['squad'][i]
    return child1, child2


# mutation function:
def mutation(individual):
    for i in range(len(individual['squad'])):
        index = randrange(0, len(individual['squad'][i]))
        if (sum_rate_avg()[i]['avg'] > sum_rate_avg()[i]['rating'][index]) and (individual['squad'][i][index] == 1):
            individual['squad'][i][index] = 1 - individual['squad'][i][index]
            while True:
                index_random = randrange(0, len(individual['squad'][i]))
                if individual['squad'][i][index_random] == 0:
                    individual['squad'][i][index_random] = 1
                    break
                else:
                    continue
        elif (individual['squad'][i][index] == 0) and (sum_rate_avg()[i]['avg'] <= sum_rate_avg()[i]['rating'][index]):
            individual['squad'][i][index] = 1 - individual['squad'][i][index]
            while True:
                index_random = randrange(0, len(individual['squad'][i]))
                if individual['squad'][i][index_random] == 1:
                    individual['squad'][i][index_random] = 0
                    break
                else:
                    continue
    individual['value'] = sum_value(individual['squad'])
    individual['rating'] = sum_rating(individual['squad'])
    return individual

# run_evolution


def run_evolution(SelectionFunc, CrossoverFunc, MutationFunc):
    start = time.time()
    team_information = population(team=bit_string_player)  # create population
    team_information = sorted(SelectionFunc(team_information),
                              key=lambda x: x['rating'], reverse=False)
    new_selection = []  # new population after selection
    for selection in team_information:  # delete duplicate element in list
        print(selection)
        if selection not in new_selection:
            new_selection.append(selection)
    for i in range(pop_size):
        parent1, parent2 = random.sample(new_selection, 2)
        child1, child2 = CrossoverFunc(parent1, parent2)
        child1 = MutationFunc(child1)
        child2 = MutationFunc(child2)
        new_selection.append(child1)
        new_selection.append(child2)
    new_selection = sorted(new_selection,
                           key=lambda x: x['rating'], reverse=True)
    print("best squad 4-4-3 for chelsea team is: ", '')
    print_squad(new_selection[0]['squad'])
    end = time.time()
    print(f"the value of club is: ", str(sum_value(new_selection[0]['squad'])))
    print(f"the rating of club is: ", str(
        sum_rating(new_selection[0]['squad'])))
    print(f"time excute: {end-start}s")


# main program
run_evolution(SelectionFunc=selection,
              CrossoverFunc=crossover, MutationFunc=mutation)
