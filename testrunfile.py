import random
import copy
import matplotlib.pyplot as plt
from decimal import Decimal, DivisionUndefined
N = 20
P = 50
MIN = -10
MAX = 10
GENERATION = 50
MUTRATE = 0.22
MUTSTEP = 0.28

# creates the 'individual' object (gene and fitness)


class individual(object):
    def __init__(self):
        self.gene = []
        self.fitness = 0

ind = individual()

# takes an 'individual' and returns the fitness of the object

def test_function(ind):
    utility = 0.0
    runningsum = 0.0

    utility = copy.deepcopy(ind.gene[0]) - 1
    utility = utility ** 2

    for i in range(1,N):
        total = 0.0

        gene1 = copy.deepcopy(ind.gene[i])
        gene2 = copy.deepcopy(ind.gene[i-1])

        total = (gene1 ** 2) *2
        total = (total - gene2) ** 2
        runningsum += total

    utility = utility + runningsum

    return utility

averagefitnesss = 0
averages = []


offspring = []
population = []
to_plt = []
notfitpeople = []
# fill the population array with 50 'individuals' with 10 different genes
for x in range(0, P):
    tempgene = []
    for x in range(0, N):
        tempgene.append(random.uniform(MIN, MAX))
    newind = individual()
    newind.gene = tempgene.copy()
    population.append(newind)



lowestscores = []
lowestscore = 0
# takes two random 'individuals' from the popualtion array and appends the better one to the offspring array
for i in range(GENERATION):
    offspring = []
    new_Solutions = []
    score = 0
    for i in population:
        i.fitness = test_function(i)
        score += i.fitness
        
    score = score/P
    to_plt.append(score)

    # parent selection
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
if notfitpeople[49] < 100000:
    print("Lowest Fitness = ", notfitpeople[49])
    print(to_plt)
    
    plt.plot(to_plt)
    plt.plot(x, drawstyle="steps")
    plt.plot(notfitpeople)
    plt.show()
    
    # lowestscore += notfitpeople[49]
    #lowestscores.append(lowestscore)
    #averagefitnesss += lowestscore
    #print(lowestscores)    
    averagefitnesss = averagefitnesss/5
    print(averagefitnesss)
    print("The Lowest Fitness = ", notfitpeople[49])
