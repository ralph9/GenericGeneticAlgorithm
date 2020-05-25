# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 18:00:05 2020

@author: Raúl
"""

#class representing a task, its objects and its constraints
class Task:
    objectsOfTask = []
    limitOfWeight = None
    limitOfSize = None
    numberOfObjects = 0
    def __init__(self, limitWeight, limitSize):
        self.limitOfWeight = limitWeight
        self.limitOfSize = limitSize
        
    def appendObjectToTask(self,objectToAdd):
        self.objectsOfTask.append(objectToAdd)
        #print("done")

#class representing an object that can be taken for the knapsack
class ObjectOfTask:
    weight = 0
    size = 0
    price = 0
    
def createObjectForTask(weight,size,price):
    objectForTask = ObjectOfTask()
    objectForTask.weight = weight
    objectForTask.size = size
    objectForTask.price = price

    return objectForTask