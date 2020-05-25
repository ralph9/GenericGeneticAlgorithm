import random
import csv
import os
def generate(n,w,s,output_file):
    #requirements established by the task
    weightThreshold = 10 * w / n
    sizeThreshold = 10 * s / n
    priceThreshold = n
    minTotalWeight = 2 * w
    totalWeightForSet = 0
    minTotalSize = 2 * s
    totalSizeForSet = 0

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        #writing the first three values
        writer.writerow([str(n) + "," + str(w) + "," + str(s)])
        
        #for each line we create random values within the constraints
        #and write them onto the file
        for x in range(n):
            randomWeight =  random.randrange(1,int(weightThreshold))
            randomSize = random.randrange(1,int(sizeThreshold))
            randomPrice = random.randrange(1,int(priceThreshold))
            
            totalWeightForSet += randomWeight
            totalSizeForSet += randomSize
            
            writer.writerow([str(randomWeight) + "," + str(randomSize) + "," + str(randomPrice)])
    #in the case the two constraints regarding total size and weight are not met
    #we scrap the file and generate a new one, until it is whithin the correct values
    if totalWeightForSet < minTotalWeight or totalSizeForSet < minTotalSize:
        os.remove(output_file)
        generate(n,w,s,output_file)

generate(1200,18001,18901,'testFile.csv')


