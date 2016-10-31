# Word Genetic Algorithm [init, points, selection, crossover, mutation]

# Point Granting
# correct letter 1 points
# correct letter in posistion 2 points
# correct length 4 points

# word properties
# - length
# - letters

import string
import random

# Properties
target_word = "more"
showEvery = 1
PopulationSize = 10
minLength = len(target_word)
maxLength = len(target_word)
mutationRate = 10 # / 100 %

last_generation = []
current_generation = []
nGeneration = 0

def initPop():
    global last_generation
    pop = PopulationSize
    while pop > 0:
        last_generation.append( generateWord(random.randint(minLength, maxLength)) )
        pop -= 1

def generateWord(length):
    l = string.ascii_letters.lower()
    cLength = 0
    rWord = ""
    
    while cLength < length:
        rWord += random.choice(l)
        cLength += 1
    
    return rWord

def pointGranting(word):
    points = 0
    #if len(word) == len(target_word):
    #    points += 3
        
    for tl in target_word:
        for wl in word:
            if tl == wl:
                points += 1

    cl = 0
    for tl in target_word:
        if cl < len(word):
            if tl == word[cl]:
                points += 2
            cl += 1
    
    return points


def selection(): #selection of the best (half the population)
    global last_generation
    halfbest = []
    bestscore = pointGranting(target_word)+1
    while len(halfbest) < PopulationSize/2:
        ch = False
        for i in last_generation:
            if bestscore < pointGranting(i):
                halfbest.append(i)
                last_generation.remove(i)
                bestscore = pointGranting(i)
                ch = True
                print("choose " + i + " with p " + str(pointGranting(i)))
        if(ch == False):
            bestscore -= 1
    #print(last_)
    last_generation = halfbest #purge
    #print(halfbest)

def crossover(p1, p2):
    if len(p1) > len(p2): # finding out the shorter word
        pl = p2
    else:
        pl = p1

    if len(p1) > 2:
        crossover_point = random.randint(1, len(pl)-1)
    else:
        crossover_point = 1
    crossover = p1[:crossover_point]+p2[crossover_point:]
    print("("+str(crossover_point)+"): "+p1+"+"+p2+" = "+crossover)
    return crossover

def repopulation(): # doubling popualtion
    global last_generation
    for i in last_generation:
        nK = 0
        while nK < 2:
            partner = last_generation[ random.randint(0, len(last_generation)-1) ]
            current_generation.append( crossover(i, partner) )
            nK += 1

def mutation():
    global current_generation
    ci = 0
    for i in current_generation:
        #rnd = random.randint(0, 100)
        #if rnd < mutationRate:
        #    if random.choice([True, False]):
        #        current_generation[ci] = i + random.choice( string.ascii_letters.lower() )
        #    else:
        #        if (len(i)-1 > minLength):
        #            current_generation[ci] = i[:-1]
        rnd = random.randint(0, 100)
        if rnd < mutationRate:
            ri = list(i)
            ri[ random.randint(0, len(i)-1 ) ] = random.choice( string.ascii_letters.lower() )
            current_generation[ci] = ''.join(ri)
            print("mutated")
        ci += 1
            

print("\n - Word Genetic Algorithm -\n  by Vox"+"\n"*2)
initPop()
target_word = target_word.lower()
while 1:
    bestWord = ""
    for w in last_generation:
        if pointGranting(bestWord) < pointGranting(w):
            bestWord = w
    #for l in last_generation:
    #    print(l)
    #    print(pointGranting(l))
    #    print("\n")
    if (nGeneration % showEvery) == 0:
        print("Generation: "+str(nGeneration))
        print("Current Generations best: '" + bestWord + "' with a score of "+str(pointGranting(bestWord))+" / "+str(pointGranting(target_word)) )
        input(": next generations ?\n")

    selection()
    repopulation()
    mutation()

    last_generation = current_generation
    current_generation = []
    
    nGeneration += 1
