# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:45:54 2020

@author: Raúl
"""
import random

def crossover(parent1, parent2, crossover_rate):
    #first we simulate the crossover happening or not
    #we get a random probability between 0 and 1
    #and we compare it with the crossover rate_
    simulatedProbability = random.uniform(0,1)
    if simulatedProbability < crossover_rate:
        #now we have to choose a random cutting point
        lengthOfGenes = len(parent1.itemsTaken)
        cuttingPoint = random.randint(0,lengthOfGenes)
        
        #we take the genes from p1 from the beginning to the cutting point
        parent1Chromosomes = [parent1.itemsTaken[:cuttingPoint]]
        
        #and for p2 from the cutting point to the end
        parent2Chromosomes = [parent2.itemsTaken[cuttingPoint:]]
      
        #and we fuse them and assign them as the genes of the child
        newChild = parent1Chromosomes[0] + parent2Chromosomes[0]

        return newChild
    else:
        return parent1.itemsTaken

#crossover(0,1,1)