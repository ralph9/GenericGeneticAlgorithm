# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:55:40 2020

@author: Raúl
"""
from read import read
from init_population import Population
from init_population import init_population
from tournament import tournament
from crossover import crossover
from mutate import mutate
from init_population import Individual
import time


def genetic():
    ITERATIONS = 30
    POP_SIZE = 40
    CROSSOVER_RATE = 0.5
    MUTATION_RATE = 0.01
    TOURNAMENT_SIZE = 6
    task = read('generatedTaskFile.csv')
    print("Here it goes...")
    population = init_population(task.numberOfObjects,POP_SIZE,task)
    i = 0
    while i < ITERATIONS:
        print("New iteration")
        j = 0
        new_population = Population(task)
        new_population.listOfIndividuals = []
        while j < POP_SIZE:
            parent1 = tournament(population,TOURNAMENT_SIZE,task)
            parent2 = tournament(population,TOURNAMENT_SIZE,task)
            child =  Individual()
            child.itemsTaken = crossover(parent1,parent2,CROSSOVER_RATE)
            mutate(child,MUTATION_RATE)
            new_population.addIndividualToPopulation(child)
            j+=1
        population = new_population
        i+=1
    return population.best()


start_time = time.time()
genetic()
print("--- %s seconds ---" % (time.time() - start_time))
