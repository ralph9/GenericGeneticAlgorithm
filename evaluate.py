# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:55:35 2020

@author: Raúl
"""

def evaluate(item,task):
        totalWeightForIndividual = 0
        totalSizeForIndividual = 0
        totalPriceForIndividual = 0
        counter = 0
 
        #we loop over the items that the individual has
        for i in range(len(item.itemsTaken)):
            if item.itemsTaken[i] == 1:
                #if the item has been chosen then we have to add its weight and size 
                #to the total of the individual, as well as the price retrieved
                objectForThisIteration = task.objectsOfTask[counter]
                totalWeightForIndividual += objectForThisIteration.weight
                totalSizeForIndividual += objectForThisIteration.size
                totalPriceForIndividual += objectForThisIteration.price
                counter +=1 
        #if the individual is within the requlired constrains, we assign it the value of the total price
        if totalWeightForIndividual <= int(task.limitOfWeight) and totalSizeForIndividual <= int(task.limitOfSize):
                return totalPriceForIndividual
        #if it doesn't comply with the requirements then we assign 0 in order to discard the individual
        else:
                return 0