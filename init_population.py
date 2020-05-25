# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:15:45 2020

@author: Raúl
"""
import random
from evaluate import evaluate

class Population:
    listOfIndividuals = []
    sizeLimit = 10000
    task = None

    #self-explanatory, it adds a new individual to the list that makes up
    #the population
    def addIndividualToPopulation(self,newIndividualToAdd):
            self.listOfIndividuals.append(newIndividualToAdd)

    #"constructor" for a population, assigning a task to it
    def __init__(self,task):
        #print("New population created")
        self.task = task
        
    #method to extract the best individual from a population
    #(called at the end of the genetic algorithm)
    def best(self):
        bestScore = 0
        print("Individuals in population:")
        print(len(self.listOfIndividuals))
        #we loop over all of them and choose the one with the best score
        for item in self.listOfIndividuals:
            if evaluate(item,self.task) > bestScore:
                bestScore = evaluate(item,self.task)
        print("Best score for this run:")
        print(bestScore)
        return bestScore


#class representing an individual, with the genes represented as a list
#with values 0 or 1
class Individual:
    itemsTaken = []
        
    #adds the genes to the individual
    def appendItemListToIndividual(self,listOfItemsToBeAdded):
        self.itemsTaken = listOfItemsToBeAdded
 
    def __len__(self):
        return len(self.itemsTaken)
    
    #getter for the genes, used for debugging purposes
    def getItems(self):
        return self.itemsTaken
      
#initial population creator
def init_population(n_items, size, task):
    newPopulation = Population(task)
    for n in range(size):
        newIndividual = Individual()
        listOfItemsForIndividual = []
        #gene creator, with a 0.85 chance of being a 0 for any given position
        #(tuned to avoid a high number of fitness value of zeroes)
        for i in range(n_items):
            chancesOfZero = 0.85
            checkProbability = random.uniform(0, 1)
            valueForItem = 0
            if checkProbability < chancesOfZero:
                valueForItem = 0
            else:
                valueForItem = 1
            listOfItemsForIndividual.append(valueForItem)
        newIndividual.appendItemListToIndividual(listOfItemsForIndividual)
        newPopulation.addIndividualToPopulation(newIndividual)
    return newPopulation
