# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:30:53 2019

@author: cslab051
"""
import random
import math

class Chromosome:
    def __init__(self,length):

        self.chromosome=self.createChromosome(length)
        self.calculateFitness()


    def getGene(self):
        str="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return random.choice(str)
    
    def createChromosome(self,length):
        chormosome=[]
        for i in range(length):
            chormosome.append(self.getGene())
        
        return chormosome
            
    def calculateFitness(self):
       self.fitness=0
       global target
       for i in range(len(target)):
            if self.chromosome[i]== target[i]:
                self.fitness+=1

    def crossover_mutation(self):
        child = []
        par1 = "ABCDEFGHIJKLM"
        par2 = "NOPQRSTUVWXYZ"
        for p1, p2 in zip(par1, par2):

            probilitiy = random.random()

            if (probilitiy > 0 and probilitiy < 0.5):
                child.append(p1)
            elif (probilitiy > 0.5 and probilitiy < 0.9):
                child.append(p2)
            else:
                child.append(chrsm.getGene())

        print(child)



    
    
target="ABC"
population=[]


for i in range(50):
    population.append(Chromosome(len(target)))
print(population,"\n")
for i in range(50):
    print("Fitness of ",i+1,"Chromosome: ",population[i].fitness)
else:
    print("Finally Finished!!")

#Chromosome.crossover_mutation()

"""
Selection
"""
population=sorted(population,key=lambda int:int.fitness)
while True:

    if population[len(population)-1].fitness==len(target):
        break

    ten_per = abs(len(population)*10/100) # check
    ten_per=int(ten_per)
    print (ten_per)
    new_gen = population[0:ten_per]

    print("New gen")
    print(new_gen)
    #90
        # main population ka 50%
        # calclate 50%
        # top 50 fittest indvuals
        #select 2random parents
        #par1=population[0:50] top50 fittest indiividuals

        #new_gen.apeend(croseeover())



"""
crossover and mutation
child=[]
par1="ABCDEFGHIJKLM"
par2="NOPQRSTUVWXYZ"
for p1,p2 in zip(par1,par2):

    probilitiy=random.random()

    if(probilitiy>0 and probilitiy<0.5):
        child.append(p1)
    elif(probilitiy>0.5 and probilitiy<0.9):
        child.append(p2)
    else:
        child.append(chrsm.getGene())

print(child)
"""