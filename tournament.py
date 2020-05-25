# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:08:49 2020

@author: Raúl
"""
import random 
from evaluate import evaluate

def tournament(population, tournament_size, task):
    listOfChosenIndices = []
    listOfChosenIndividuals = []
    #first we loop and choose random indices
    #no repeating
    for i in range(tournament_size):
        indexChosenForIteration = random.randrange(len(population.listOfIndividuals))
        while indexChosenForIteration in listOfChosenIndices:
            indexChosenForIteration = random.randrange(len(population.listOfIndividuals))
        listOfChosenIndices.append(indexChosenForIteration)
        listOfChosenIndividuals.append(population.listOfIndividuals[indexChosenForIteration])
    #now we have our list of randomly chosen individuals
    #we evaluate them and record the best
    bestResultSoFar = 0
    bestIndividualSoFar = listOfChosenIndividuals[0]
    for i in range(len(listOfChosenIndividuals)):
        if(listOfChosenIndividuals[i].itemsTaken == None):
            print("null item list")
        resultForIteration = evaluate(listOfChosenIndividuals[i],task)
        #if we got a valid evaluation value and it is better than the best
        #it automatically becomes the new best
        if resultForIteration > bestResultSoFar:
            bestResultSoFar = resultForIteration
            bestIndividualSoFar = listOfChosenIndividuals[i]
    #finally, we return the best individual
    return bestIndividualSoFar