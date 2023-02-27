from typing import List
from random import choices
from collections import namedtuple

Genome = List[int]
Population = List[Genome]
Thing = namedtuple('Thing', ['name', 'position', 'rating', 'salary'])

things = [
    Thing('Edouard Mendy', 'GK', 6.5, 25),
    Thing('Kepa Arrizabalaga', 'GK', 7.02, 15),
    Thing('Marcus Bettinelli', 'GK', 5.0, 2),
    Thing('Wesley Fofana', 'GK', 7.48, 65),
    Thing('Kalidou Koulibaly', 'DF', 6.82, 35),
    Thing('Trevoh Chalobah', 'DF', 6.94, 22),
    Thing('Thiago Silva', 'DF', 6.93, 2),
    Thing('Marc Cucurella', 'DF', 6.54, 55),
    Thing('Ben Chilwell', 'DF', 6.97, 38),
    Thing('Reece James', 'DF', 7.19, 70),
    Thing('César Azpilicueta', 'DF', 6.29, 8),
    Thing('Denis Zakaria', 'CM', 7.51, 20),
    Thing('N\'Golo Kanté', 'CM', 7.2, 30),
    Thing('Enzo Fernández', 'CM', 6.81, 55),
    Thing('Mateo Kovacic', 'CM', 6.85, 40),
    Thing('Conor Gallagher', 'CM', 66.57, 32),
    Thing('Ruben Loftus-Cheek', 'CM', 6.6, 25),
    Thing('Mason Mount', 'CM', 6.89, 75),
    Thing('Kai Havertz', 'CM', 6.75, 70),
    Thing('Raheem Sterling', 'AT', 6.66, 70),
    Thing('Mykhaylo Mudryk', 'AT', 6.15, 40),
    Thing('Christian Pulisic', 'AT', 6.31, 24),
    Thing('Hakim Ziyech', 'AT', 6.47, 20),
    Thing('Noni Madueke', 'AT', 6.77, 15),
    Thing('João Félix', 'AT', 6.55, 50),
    Thing('Armando Broja', 'AT', 6.29, 30),
    Thing('Pierre-Emerick Aubameyang', 'AT', 6.15, 12),
    Thing('David Datro Fofana', 'AT', 6.61, 7),
]


def generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length)


def generate_population(size: int, genome_length: int) -> Population:
    return [generate_genome(genome_length) for _ in range(size)]


def fitness(genome: Genome, things: List[Thing], salary_limit: int) -> float:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of the same length")

    salary = 0
    value = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            salary += thing.salary
            value += thing.value

            if salary > salary_limit:
                return 0
    return value/11
