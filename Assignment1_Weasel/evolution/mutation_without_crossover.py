import random

from soton.complexity.evolution import evolve


def start_evolution_without_crossover():
    survivor, existing_population = evolve.start_evolving()
    solution_found = False
    total_mutation = 0
    generation = 0

    while True:
        max_fitness = 0
        best_fit_survivor = ''

        rand_survivor_1, rand_survivor_fitness_1, _, rand_survivor_2, rand_survivor_fitness_2, _ \
            = evolve.get_random_survivors_from_population(survivor)

        if rand_survivor_fitness_1 > rand_survivor_fitness_2:
            parent = rand_survivor_1
        else:
            parent = rand_survivor_2

        child, number_of_mutations = evolve.mutate(parent)
        str_child = ''.join(child)

        if str_child == evolve.target:
            survivor = ''.join(child)
            break
        else:
            if existing_population[str_child] >= max_fitness:
                max_fitness = existing_population[str_child]
                best_fit_survivor = str_child

        rand_survivor_1, rand_survivor_fitness_1, index_1, rand_survivor_2, rand_survivor_fitness_2, index_2 \
            = evolve.get_random_survivors_from_population(survivor)

        if rand_survivor_fitness_1 > rand_survivor_fitness_2:
            survivor[index_2] = child
        else:
            survivor[index_1] = child

        total_mutation += number_of_mutations

        if not solution_found:
            generation += 1

        print("Best fit survivor found at generation {}: {} with "
              "fitness {}".format(generation, best_fit_survivor, max_fitness))

    print("Survivor '{} 'has been found".format(survivor))
    print("Number of Mutations it took is {}".format(total_mutation))
    print("Generation was {}".format(generation))


if __name__ == '__main__':
    start_evolution_without_crossover()
