# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:30:53 2019

@author: cslab051
"""
import random
import math


class Chromosome:
    def __init__(self):
        self.fitness = 0

    def getGene(self):
        str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return random.choice(str)

    def createChromosome(self, length):
        chormosome = []
        for i in range(length):
            chormosome.append(self.getGene())

        return chormosome

    def calculateFitness(self, chrsm, target):
        self.fitness = 0
        for i in range(len(target)):
            if chrsm[i] == target[i]:
                self.fitness += 1
        return self.fitness

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


target = "ABC"
population = []
chrsm = Chromosome()
for i in range(50):
    population.append(chrsm.createChromosome(len(target)))
print(population, "\n")
for i in range(50):
    print("Fitness of ", i + 1, "Chromosome: ", chrsm.calculateFitness(population[i], target))
else:
    print("Finally Finished!!")

chrsm.crossover_mutation()

"""
Selection
"""
new_gen = ""
for in1 in population:

    population1=sorted(population, key=lambda int:int.fitness)
    population2=[]

    if(population1[len(population1)-1].fitness == len(target)):
        print(population2)
        break

ten_per = abs(len(population) * 10 / 100)
print("10 per value : ",ten_per)
new_gen = population[0:ten_per]
print("New gen")
print(new_gen)

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