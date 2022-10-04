#!/usr/bin/env python3

import numpy as np
import math
from copy import copy

def get_violations_count(sol):

    violations_count = 0

    for i in range(len(sol)):

        for j in range(len(sol)):

            # columns
            if (i != j) and (sol [i] == sol [j]):

                violations_count += 1

            # diagonals

            deltay = abs(sol[i] - sol[j])
            deltax = abs(i - j)
            same_diagonal = deltax == deltay

            if same_diagonal:

                violations_count += 1

    return violations_count

def obj(sol):

    return get_violations_count(sol)

def rand_in_rand_position(sol):

    neighbor = copy(sol)

    idx = np.random.randint(0,len(sol))
    value = np.random.randint(0,len(sol))

    neighbor[idx] = value

    return neighbor

def swap(sol):

    neighbor = copy(sol)

    idx1 = np.random.randint(0,len(sol))
    idx2 = np.random.randint(0,len(sol))

    neighbor[idx1], neighbor[idx2] =  neighbor[idx2], neighbor[idx1] 

    return neighbor

def local_search_simulated_annealing(sol, objective, get_neighbor, maxit = 50, verbose=False):

    current_values = []

    temperature = 100

    best_solution = copy(sol)
    best_value    = objective(sol)

    current_value = objective(sol)

    it = 0

    while it <= maxit:

        n = get_neighbor(sol)

        n_val = objective(n)

        if n_val <= best_value:

            best_value = n_val

            best_solution = copy(n)

        neighbor_is_better = n_val <= current_value

        can_change = np.random.rand() < math.exp(-( n_val - current_value ) / temperature)

        if neighbor_is_better or can_change:

            sol = copy(n)

            current_value = n_val

        current_values.append(current_value)

        if verbose:
            print(f'{it} : {best_value}')

        it += 1

        temperature *= 0.99

    return best_solution, best_value, current_values


if __name__ == '__main__':

    initial_sol = list(range(8))

    sol, val, c = local_search_simulated_annealing(initial_sol, obj, swap, maxit = 100, verbose=False)

    print(f'sol: {sol}')
    print(f'val: {val}')
    print(f'c_vals: {c}')
    #print(f'{len(c) == 100 + 1}')