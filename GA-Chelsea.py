from typing import List
from random import choices

Genome = List[int]
Population = List[Genome]


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
