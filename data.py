
# player position
# GK-GoalKeeper
# DF-Defender
# CM-Central Midfielder
# AT-Attacker

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

# avg rating for each position


def sum_rating():
    rating = {}
    sum_rate = 0
    index = 0
    for position in player_chelsea.values():
        position_rating = []
        position_rate = 0
        for player in position.values():
            print(player['rating'])
            position_rating.append(player['rating'])
            sum_rate += player['rating']
            position_rate += player['rating']
        if index == 0:
            rating['GK'] = {'avg': float(
                position_rate/len(position.values())), 'rating': position_rating}
        if index == 1:
            rating['DF'] = {'avg': float(
                position_rate/len(position.values())), 'rating': position_rating}
        if index == 2:
            rating['CM'] = {'avg': float(
                position_rate/len(position.values())), 'rating': position_rating}
        if index == 3:
            rating['AT'] = {'avg': float(
                position_rate/len(position.values())), 'rating': position_rating}
        index += 1

    print(rating, '\n', sum_rate)
    return rating


sum_rating()
