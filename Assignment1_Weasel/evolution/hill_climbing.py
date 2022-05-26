from soton.complexity.evolution import evolve


def start_hill_climbing():
    survivor, existing_population = evolve.start_evolving()
    solution_found = False
    total_mutation = 0
    generation = 0

    while not solution_found:
        max_fitness = 0
        for i in range(len(survivor)):
            mutated_str, number_of_mutations = evolve.mutate(survivor[i])
            survivor[i] = mutated_str
            total_mutation += number_of_mutations

            if survivor[i] in existing_population:
                survivor_fitness = existing_population[survivor[i]]
            else:
                survivor_fitness = evolve.check_fitness(survivor[i])

            if survivor_fitness > max_fitness:
                max_fitness = survivor_fitness
                fit_survivor = ''.join((survivor[i]))

            if survivor[i] == evolve.target:
                solution_found = True
                best_fit_survivor = ''.join(survivor[i])
                break

        if not solution_found:
            generation += 1
        print("Best fit survivor found at generation {}: {} with "
              "fitness {}".format(generation, fit_survivor, max_fitness))

    print("Survivor '{} 'has been found".format(best_fit_survivor))
    print("Number of Mutations it took is {}".format(total_mutation))
    print("Generation was {}".format(generation))


if __name__ == '__main__':
    start_hill_climbing()
