import random
import copy
import matplotlib.pyplot as plt
from decimal import Decimal, DivisionUndefined
N = 20
P = 50
MIN = -5
MAX = 5
GENERATION = 50


# creates the 'individual' object (gene and fitness)
class individual(object):
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0
#creates the mutation object, used to track the final fitness with the rate and step
class mutations(object):
    def __init__(self):
        self.mutation_rate = 0
        self.mutation_step = 0
        self.average_fitness = 0

#initalises the individual as "ind"
ind = individual()

# takes an 'individual' and returns the fitness of the object using the fitness funciton
def test_function(ind):
    utility = 0
    for gene in (ind):
        utility += (gene ** 4) - 16*(gene**2) + (5*gene)
    utility = utility/2
    return utility


averagefitnesss = 0
averages = []
MUTRATE = 0.0
MUTSTEP = 0.5
#using an inbeded while loop the step and rate are iterated through every posibility up to a set decimal place 
while MUTSTEP < 0.80:
    MUTSTEP = round(MUTSTEP + 0.01,3)
    MUTRATE = 0.0
    while MUTRATE < 0.3:
        MUTRATE = round(MUTRATE + 0.1,3)
        print(MUTRATE,MUTSTEP)
        lowestscore = 0

#loops through 10 times and gets the average to remove any outliers
        for i in range (0,5):
            offspring = []
            population = []
            to_plt = []
            notfitpeople = []
            # fill the population array with 50 'individuals' with 10 different genes using the MIN and MAX varables as the range
            for x in range(0, P):
                tempgene = []
                for x in range(0, N):
                    tempgene.append(random.uniform(MIN, MAX))
                newind = individual()
                newind.gene = tempgene.copy()
                population.append(newind)

            score = 0
            # loops through the population and gives each individual a fitness value by passing its genes through the test function
            for i in population:
                i.fitness = test_function(i.gene)
                score += i.fitness


            lowestscores = []
            lowestscore = 0
            # takes two random 'individuals' from the popualtion array and appends the better one to the offspring array
            for i in range(GENERATION):
                offspring = []
                new_Solutions = []
                score = 0
                for i in population:
                    i.fitness = test_function(i.gene)
                    score += i.fitness

                to_plt.append(score/P)

                # parent selection selects the better of two individuals and appends the better to a new array
                for i in range(0, P):
                    parent1 = random.randint(0, P-1)
                    off1 = copy.deepcopy(population[parent1])
                    parent2 = random.randint(0, P-1)
                    off2 = copy.deepcopy(population[parent2])
                    if off1.fitness < off2.fitness:
                        offspring.append(off1)
                    else:
                        offspring.append(off2)

                temp = individual()
                # making new individuals
                toff1 = individual()
                toff2 = individual()
                temp = individual()
                # uses a cross point to swap the genes of the two parent individuals to create and new individual
                for i in range(0, P, 2):
                    toff1 = copy.deepcopy(offspring[i])
                    toff2 = copy.deepcopy(offspring[i+1])
                    temp = copy.deepcopy(offspring[i])
                    crosspoint = random.randint(1, N)
                    for j in range(crosspoint, N):
                        toff1.gene[j] = toff2.gene[j]
                        toff2.gene[j] = temp.gene[j]
                    offspring[i] = copy.deepcopy(toff1)
                    offspring[i+1] = copy.deepcopy(toff2)

                #uses the MUT step and rate to alter the genes and create the new population 
                for i in range(0, P):
                    newind = individual()
                    newind.gene = []
                    for j in range(0, N):
                        gene = offspring[i].gene[j]
                        mutprob = random.random()
                        if mutprob < (MUTRATE):
                            alter = random.uniform(-MUTSTEP,MUTSTEP)
                            gene = gene + alter
                            if gene < MAX:
                                gene = MAX
                            if gene > MIN:
                                gene = MIN
                            if(random.randint(0, 1) == 1):
                                offspring[i].gene[j] = offspring[i].gene[j] + alter
                                if offspring[i].gene[j] > MAX:
                                    offspring[i].gene[j] = MAX
                            else:
                                offspring[i].gene[j] = offspring[i].gene[j] - alter
                                if offspring[i].gene[j] < MIN:
                                    offspring[i].gene[j] = MIN

                # takes the highest fitness of the previous population and the lowest of the current and swaps them so the population never 
                #goes up and always slopes down
                tmpobject = individual()
                lowestposition = 0
                LowestFitness = population[0].fitness
                HighestFitness = 0
                for i in range(0, P):
                    tmpobject = population[i]
                    if tmpobject.fitness < LowestFitness:
                        LowestFitness = tmpobject.fitness
                        fitperson = tmpobject

                tmpobject = individual()

                for i in range(0, P):
                    tmpobject = population[i]
                    if tmpobject.fitness > HighestFitness:
                        HighestFitness = tmpobject.fitness
                        lowestposition = i


                offspring[lowestposition] = fitperson

                notfitpeople.append(fitperson.fitness)
                newind.gene.append(gene)
                new_Solutions.append(newind)
                population = copy.deepcopy(offspring)
            #print(to_plt)
            #print(notfitpeople)
            #plt.plot(to_plt)
            #plt.plot(x, drawstyle="steps")
            #plt.plot(notfitpeople)
            #plt.show()
            lowestscore += notfitpeople[49]
            lowestscores.append(lowestscore)
            averagefitnesss += lowestscore
            #print(lowestscores)
        #creates a mutation object with the average fitness and MUT step and rate and then adds it to an array
        mutation = mutations()
        divide = averagefitnesss/5
        averagefitnesss = 0
        mutation.average_fitness = divide
        mutation.mutation_rate = MUTRATE
        mutation.mutation_step = MUTSTEP
        averages.append(mutation)
    x = len(averages)     
    lowestaverage = 0
#iterates through the average array and outputs the best MUT step, rate and fitness
for i in range(0,x):
    tmpobject = averages[i]
    if tmpobject.average_fitness < lowestaverage:
        lowestaverage = tmpobject.average_fitness
        bestplot = tmpobject
print("Fitness = ", bestplot.average_fitness, "Rate = ", bestplot.mutation_rate, "Step = ", bestplot.mutation_step)
