import random
from random import Random

population_size = 50
target = "methinks it is like a weasel"
mutation_rate = 1 / len(target)
possible_characters = "abcdefghijklmnopqrstuvwxyz "
survivor = []
generation_fitness = {}


def check_fitness(new_generation):
    fitness_score = 0
    for i in range(len(new_generation)):
        if new_generation[i] == target[i]:
            fitness_score += 1
    return fitness_score


def start_evolving(population_size=population_size):
    for i in range(population_size):
        new_generation = ''
        for j in range(len(target)):
            possible_generation = random.choice(possible_characters)
            new_generation += possible_generation
        generation_fitness[new_generation] = check_fitness(new_generation)
        survivor.append(new_generation)
    return survivor, generation_fitness


def mutate(possible_generation):
    mutation_number = 0
    chr_string = list(possible_generation)
    for i in range(len(chr_string)):
        random_num = random.uniform(0, mutation_rate)
        if random_num < mutation_rate:
            mutation_number += 1
            chr_string_copy = chr_string.copy()
            chr_string_copy[i] = random.choice(possible_characters)
            temp_str = ''.join(chr_string_copy)

            if temp_str not in generation_fitness:
                generation_fitness[temp_str] = check_fitness(chr_string_copy)

            if generation_fitness[temp_str] > generation_fitness[''.join(chr_string)]:
                chr_string = chr_string_copy

    return ''.join(chr_string), mutation_number


def get_random_survivors_from_population(population):
    index_1 = index_2 = -1
    while index_1 == index_2:
        index_1 = random.randint(0, len(population) - 1)
        index_2 = random.randint(0, len(population) - 1)

    rand_survivor_1 = population[index_1]
    rand_survivor_2 = population[index_2]
    rand_survivor_fitness_1 = generation_fitness[''.join(rand_survivor_1)]
    rand_survivor_fitness_2 = generation_fitness[''.join(rand_survivor_2)]

    return rand_survivor_1, rand_survivor_fitness_1, index_1, rand_survivor_2, rand_survivor_fitness_2, index_2
