# Omar Jiminez 
"""
Summary: Program will evolve to generate a best-fitting (covers the most amount of area) picobot program
1) Program evalutes fitness of each randomly generated program from 0-1
2) Program choses most fit programs 
3) Programs will randomly mate to produce new population of programs. 
4) Software will introduce mutations so that the next generation will be the same size as the previous one
5) Repeat for x number of generations  """

import random 
POSSIBLE_SURROUNDINGS = ['xxxx','Nxxx','NExx','NxWx','xxxS','xExS','xxWS','xExx','xxWx']
#Global Variables 
# Wall dimensions of picobot world 
HEIGHT = 25
WIDTH = 25
#Number of states for Picobot program, 
NUMSTATES = 5

# Program class with working construction and _repr_
class Program:
    """ Class program represents a single picobot program"""
    def __init__(self):
        """JUST sets self.rules to be an empty dictionary THATS IT"""
        self.rules = { } #dictionary that stores state patterns and new states! # eg: 0 xExx -> N 1
        #(0, "xExx") : ("N", 1)
    def __repr__(self):
        """Objective: Sort rules
        RULES MUST BE IN PICOBOT FORM: state Xxxx -> X state
        1) Create string with all of rules in self.rules
        2) Sort by dictionary key  (so they are easier to compare to eachother 
        3) Print rules (as string) in sorted order
        4) Return of full Picobotprogram (in picobot form)"""
        unsortedKeys = list(self.rules.keys())  # prints rules in sorted order, where unsortedKeys is a list. 
        sortedKeys = sorted(unsortedKeys) # produces list of keys
        rules = ""
        for key in sortedKeys:
            value = self.rules[key]
            rules+= str(key[0]) + " " + key[1] + " -> " + value[0]+ " "+ str(value[1]) + "\n"
        return rules #string of rules

# Randomize method 
    def randomize(self):
        """Produces 45 randomly-generated rules.
        Makes random rules for each combination of the 5 states and 9 surroundings
        1) Loop through each possible state and each possible surroundings pattern 
        2) Generate a random next state and a random next LEGAL move in move_dir
        """
    
        possible_steps = [] # empty array we want to use and fill up
        for i in range(NUMSTATES): # factor of 5
            for j in range(len(POSSIBLE_SURROUNDINGS)): # factor of 9
                # so together, the total number of states is 45
                #t = (i,POSSIBLE_SURROUNDINGS[j] )      # doesnt do anything rn
                possible_steps.append((i,POSSIBLE_SURROUNDINGS[j] )) # adding a tuple i, a number of state (5 of a number of a state)
                # for every possible state, we are putting all the possible surroundings, then we repeat and fill up the array
        values = [] # empty array that is values of keys, and the keys are the possible steps and come from the dictionary of self.rules
        #we want the above bc it is tuple in our possible values 
        #posmove= ["x", "N", "E", "W", "S"] # arrary of direction

        for n in range(len(possible_steps)): # adds a random possible move and a random state for every key
            currentI, currentS = possible_steps[n]
            posS =  ["x", "N", "E", "W", "S"] 
            for step in 'NEWS':
                if step in currentS:
                    posS.remove(str(step))
            move=(random.choice(posS))
            values.append((move,random.choice(range(NUMSTATES)))) #

        for p in range(len(possible_steps)): # adds what we have gained to the dictionary self.rules
            self.rules[possible_steps[p]] = values[p]
        
    def getMove(self, state, surroundings):
        """ Accept: Integer state and surrounding (e.g., "xExx")
        Return: Tuple with new move and new state
        Method: Use self.rules  """
        x = self.rules[(state,surroundings)]
        return x

    # in program class  # i moved to program class from world class - michi
    def mutate(self): 
        """
       1) Chose a rule from self.rules
       2) Change the value of the rule to a new state and VALID move (no walls)
       3) Check that new rule is NOT the same as the original. if old==new then regenerate. 
        """
        #(0, "xExx") : ("N", 1)
        keys = [i for i in self.rules] # set keys into array 
        values = [self.rules[i] for i in self.rules]
        element=random.choice(range(len(keys))) # sets variable key to a random value
        oldS, oldD = keys[element] # get values of key 
        moveD, moveS = values[element]
        

        newS= random.choice(range(NUMSTATES))
        while oldS == newS:
            newS= random.choice(range(NUMSTATES))

        # newD= random.choice(posmove) 
        posS =  ["x", "N", "E", "W", "S"] 
        # print(posS)
        for step in 'NEWS':
            if step in moveD or step in oldD:
                posS.remove(str(step))
                
        # print(posS)
        newD= random.choice(posS) 
        # print (newD)
        # print (oldD)
        while oldD==newD:
                newD= random.choice(range(posS))

        self.rules[keys[element]]= (newD,newS)

     


    def crossover(self, other): # i moved to program class from world class - michi
        """Objective: Mate. (Generates new program with some of the rules from self and the rest from other.)
    Accept: other object of type Program
    Return: child program
    1) Chose random state from [0-3 INCLUSIVE]
    2) Child program gets corresponding rules
    Note: DO NOT modify the program of one of the parents rather than returning a brand-new offspring Program. 

        """
        childP = Program() #empty list
        
        x = random.choice(range(4)) #gets a random valye from 0, 1, 2, 3
        
        for e in self.rules: #(0, "xExx") : ("N", 1)
            if e[0] <= x:1
            childP.rules[e] = self.rules[e] 
                #dictionarys are funny
                #d = {}
                #d{'west'} = 'onfire'
                #{'west':'onfire'}

        for k in other.rules:
            if k[0] > x:
                childP.rules[k] = other.rules[k]

        return childP

    def __gt__(self, other):
            """Greater-than operator -- works randomly, but works!"""
            return random.choice([True, False])

    def __lt__(self, other):
            """Less-than operator -- works randomly, but works!"""
            return random.choice([True, False])
"""
0 NExx -> W 2
0 NxWx -> E 0
0 Nxxx -> E 2
0 xExS -> W 4
0 xExx -> W 4
0 xxWS -> N 3
0 xxWx -> N 4
0 xxxS -> E 3
0 xxxx -> N 0

1 NExx -> S 0
1 NxWx -> E 2
1 Nxxx -> S 2
1 xExS -> N 4
1 xExx -> S 0
1 xxWS -> E 2
1 xxWx -> S 2
1 xxxS -> N 4
1 xxxx -> S 3

2 NExx -> W 2
2 NxWx -> E 4
2 Nxxx -> W 3
2 xExS -> N 0
2 xExx -> N 2
2 xxWS -> E 0
2 xxWx -> S 1
2 xxxS -> N 3
2 xxxx -> E 0

3 NExx -> S 0
3 NxWx -> E 1
3 Nxxx -> E 4
3 xExS -> W 0
3 xExx -> N 4
3 xxWS -> N 3
3 xxWx -> E 1
3 xxxS -> N 2
3 xxxx -> W 1

4 NExx -> S 1
4 NxWx -> E 2
4 Nxxx -> E 0
4 xExS -> N 4
4 xExx -> W 2
4 xxWS -> N 1
4 xxWx -> N 2
4 xxxS -> E 3
4 xxxx -> S 0

"""

# possible_steps holds only the "possible" steps!
#four choices --> (0, "xExx") : ("N", 1)
POSSIBLE_SURROUNDINGS = ['xxxx','Nxxx','NExx','NxWx','xxxS','xExS','xxWS','xExx','xxWx']

#world class
class World:
    def __init__(self, initial_row, initial_col, program):
        self.row = initial_row  #row picobot it located
        self.col = initial_col # column picobot is located in 
        self.state = 0
        self.program = program
        self.room = [[' ']*WIDTH for row in range(HEIGHT)]

    def __repr__(self):
        s = ''                          # The string to return
        for row in range(0, HEIGHT):
            s += '|'
            for col in range(0, WIDTH):
                if row == self.row and col== self.col:
                    s+= "P|"
                else:
                    s += self.room[row][col] + '|'
                
            s += '\n'
        return s

    def step(self):
        """
    - Moves picobot one step
    - Updates self.room
    - Updates state,row, column of picobot (new move)
    - USING self.prog
    - Determine surroindings:Usuing getCurrentSurroundings to find row and column 
    use surrdings and self.state to ask self.prog to find  nextMove and nextState usuing get.move
        """
        CurrentS= self.getCurrentSurroundings()
        newMove = self.program.getMove(self.state,CurrentS)
        newD , newS = newMove

        self.room[self.row][self.col] = "o"

        if newD == "N":
            self.row-=1
        if newD == "E":
            self.col+=1
        if newD == "W":            
            self.col-=1
        if newD== "S":
            self.row+=1

        self.state = newS

    def getCurrentSurroundings(self):
        s= ""

        if self.row-1<0:
            s+= "N"
        else:
            s+="x"

        if self.col+1>24:
            s+= "E"
        else:
            s+="x"

        if self.col-1<0:
            s+= "W"
        else:
            s+="x"

        if self.row+1>24:
            s+= "S"
        else:
            s+="x"

        return s

    def run(self,steps):
        for i in range(steps):
            self.step()

    def fractionVisitedCells(self): # this is basic fitness score of picobot program 
        """returns the floating-point fraction of cells in self.room that have been marked as visited 
        (including Picobot's current location)
        THIS IS NOT THE NUMBER OF STEPS. 
       It is the number of distinct grid squares in Picobot's environment that it touched during its run"""
        F= 0
        for row in range(HEIGHT):
            
            for col in range(WIDTH):
                if self.room[row][col] =="o":
                    F+=1
        
        return float(F/(HEIGHT*WIDTH))

# Functions outside of outside of both the Program and World classes

# Function 1: Accepts: poplation size, returns population (a Python list) of that many random Picobot programs.
def popSize(size):
    c = []
    for i in range(size):
        b=Program()
        b.randomize()
        c+=[b] #dict' object is not callable --> means you are trying to call something that isnt a function (for ex/ 3() or 13213())
    return c


# Function 2: (should be short)
def evaluateFitness(program, trials, steps): 
    """
    Arguments: Picobot program, trials, steps
    Return: fitness (a floating point number between 0.0 and 1.0) that is the fraction of the cells visited by this Picobot program,
     averaged over the given number of trials. (use fractionVisitedCells)
    """
    avgfit= 0
    for i in range(trials):

        C=World(random.choice(range(25)),random.choice(range(25)), program)
        C.run(steps)
        fit = C.fractionVisitedCells()
        avgfit+= fit
    avgfit= avgfit/trials
    return avgfit



# Function 3: Main function. 
def GA(popsize, numgens): 
    """create popsize random Picobot programs as the initial population (200 has worked well in the past).
     Then, Evaluate the fitness of all of those programs
     Sort a list of [fitness, program] pairs
     Extract the most-fit programs (get parent generation) ( keep top 10% of the population)
     FOR THE REST 90%, create offspring from randomly-chosen parents within the top-10% set.
     Mutate 1/3 of the population 
     CREATE CHILD PROGRAMS: (this is the experimental part)
     - keep every generation the same size (popsize)
     - keep those most-fit programs as part of the next generation (AT FIRST, DELETE LATER)
     - ELSE:select two parents at random from the most-fit pool.
     - Use crossover to create a child program from those two parents.
     - Use mutate once in a while ONCE IN A WHILE 
     REPEAT. 
     THEN return or print best program from last generation. 
     print both the average and maximum fitness among the programs in that generation of the simulation."""
    
    #create popsize random picobot programs as the inital population 
    initialpop = popSize(popsize)
    fitpro = []

    for e in range(len(initialpop)):
            score = evaluateFitness(initialpop[e], 42, 1000)
            fitpro += [ (score,initialpop[e]) ] #  temp list to score program
        #sort a list of [fitness, program] pairs
        
    first = sorted(fitpro, reverse=True)
    bestPro = first[0]

    fitpro = []

    #evaluate the fitness of all of those programs
    for gen in range(numgens):
        for e in range(len(initialpop)):
            score = evaluateFitness(initialpop[e], 42, 1000)
            fitpro += [ (score,initialpop[e]) ] #  temp list to score program
        #sort a list of [fitness, program] pairs
        
        SL = sorted(fitpro) #sorted fitness programs 
        SLs = [  x[1] for x in SL    ] # getting only the programs of the tuple
        #extract the most fit programs (recommended 10%)
        extractfit = []
        for i in range(1,(int(popsize*.05))+1):    
            extractfit+= [SLs[-i]]

        #create childrej programs!!
        newGen = []
        for i in range(popsize):
            mom= random.choice(extractfit)
            dad =random.choice(extractfit)
            child = mom.crossover(dad)      #things are getting spicy
            flip = random.choice(range(3))
            if flip == 0:
                child.mutate()
            newGen+=[child]
        #keep each gen the same size popsize
        #keep the most fit programs as part of the next gen (FOR NOW)
        #select 2 parents at random from most fit pool 
        #use crossover to create a child program from the 2 parents
        #use mutate once in a while (NOT TOO MUCH)
        #REPEAT
        initialpop= newGen

        print ("GENERATION: " + str(gen))
        genAvg = 0
        for k in range(len(newGen)):
            genAvg += evaluateFitness(newGen[k],42,1000)
        print(" AVERAGE FITNESS: "+ str((genAvg/len(newGen))))

        for e in range(len(initialpop)):
            score = evaluateFitness(initialpop[e], 42, 1000)
            fitpro += [ (score,initialpop[e]) ] #  temp list to score program
        #sort a list of [fitness, program] pairs
        
        SL = sorted(fitpro, reverse=True)
        tempBest = evaluateFitness(SL[0][1] , 42, 1000)
        print(" BEST FITNESS: " + str(evaluateFitness(SL[0][1] , 42, 1000)))
        if tempBest >  bestPro[0]:
            bestPro = SL[0]

        fitpro= []

    ##best generation
    # for e in range(len(initialpop)):
    #         score = evaluateFitness(initialpop[e], 42, 1000)
    #         fitpro += [ (score,initialpop[e]) ] #  temp list to score program
    #     #sort a list of [fitness, program] pairs
        
    # SL = sorted(fitpro)
    # return SL[-1]
    print ("Best Program: ")
    print(bestPro)
    return SL[0]



    