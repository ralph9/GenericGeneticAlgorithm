# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:49:48 2020

@author: Raúl
"""
import csv
from taskClass import createObjectForTask
from taskClass import Task

def read(input_file):
    print("Starting read...")
    with open(input_file) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        #we extract the values of the first row for special treatment
        firstRow = next(csvReader)
        print(firstRow[0].split(","))
        limitWeight = firstRow[0].split(",")[1]
        limitSize = firstRow[0].split(",")[2]
        newTask = Task(limitWeight,limitSize)
        for row in csvReader:
            #we split the subsequent rows
            rowSplitted = row[0].split(",")
            #we create a new object with the values given from the split
            newObjectForTask = createObjectForTask(int(rowSplitted[0]),int(rowSplitted[1]),int(rowSplitted[2]))
            newTask.appendObjectToTask(newObjectForTask)
            lineCount+=1
        newTask.numberOfObjects = lineCount 
        print("Lines read:")
        print(len(newTask.objectsOfTask))
            
    print("Reading finished")           
    return newTask
