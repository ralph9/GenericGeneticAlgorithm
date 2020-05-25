# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:46:58 2020

@author: Raúl
"""
import random

def mutate(individual,mutation_rate):
    #first we see how many genes will mutate 
    #given the total number of them in an individual
    #-1 is given to avoid a wrong index position (last position of the list +1)
    totalGenes = len(individual.itemsTaken) -1
    totalMutations = int(mutation_rate * totalGenes)
    
    #then we choose the random positions where the mutations will happen
    #(no repetitions)
    positionsForMutations = []
    for i in range(totalMutations):
        positionChosen = random.randint(0,totalGenes)
        while positionChosen in positionsForMutations:
            positionChosen = random.randint(0,totalGenes)
        positionsForMutations.append(positionChosen)
    
    #we check those positions in the gene chain and swap their values
    for position in positionsForMutations:
        geneToMutate = individual.itemsTaken[position]
        if geneToMutate == 0:
            geneToMutate = 1
        else:
            geneToMutate = 0
            