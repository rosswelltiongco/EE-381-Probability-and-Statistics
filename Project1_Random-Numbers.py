"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Rosswell Tiongco
" Project 1 - Random Numbers and Stochastic Experiments
" EE 381    - Probability and Statistics
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 1 - Function for a n-sided die
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import numpy as np
import matplotlib.pyplot as plt
import random

# Input: probability vector summing to 1
# Output: side of die based on input probability
def nSideDie(p):
    sides = len(p)
    roll = np.random.random()
    prob_sum = 0
    for i in range(0,sides):
        prob_sum = prob_sum + p[i]
        if i == 0:
            if roll <= prob_sum:
                value = i + 1
            else:
                value = 0
        else:
            if roll > prob_sum - p[i] and roll <= prob_sum:
                value = i + 1
    return value

def problem1():
    # Function test: Plot 10,000 rolls
    # Probability vector given by professor
    #   1      2       3      4     5     6     7
    p=[0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10]

    # Generate 1000 rolls
    rolls = [nSideDie(p) for x in range(10000)]
    side = range(1,len(p)+1)
    sideCounts = [rolls.count(x)/10000 for x in side]

    # Stem plot graphing
    plt.stem(side,sideCounts)
    plt.title('PMF of 7 sided die')
    plt.xlabel('Face')
    plt.ylabel('Occurences of face')
    plt.show()

problem1()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 2 - Number of rolls needed to get a '7' with two dice
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import random

# Input: None
# Output: How many rolls it takes to get a 7 with two dice
def getRolls():
    total = 0
    iteration = 1
    while (total != 7):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        total = r1+r2
        iteration+=1
    return iteration-1

def problem2():
    rolls = [getRolls() for x in range(100000)]

    timesItTakes = sorted(set(rolls))
    occurences = [rolls.count(num)/100000 for num in timesItTakes]

    plt.stem(timesItTakes,occurences)
    plt.xlim(right=30)
    plt.title('PMF - Rolling a 7 with two dice')
    plt.xlabel('Times it takes')
    plt.ylabel('Occurences')
    plt.show()

problem2()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 3 - Getting 50 heads when tossing 100 coins
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import numpy as np

# Input: None
# Output: True if there are 50 heads in 100 tosses
def toss100Coins():
    return 1 if sum(np.random.randint(0, 2, 100)) == 50 else 0

def problem3():
    print("Probability:",sum(toss100Coins() for _ in range(100000))/100000)

problem3()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 4 - The Password Hacking Problem
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import numpy as np

# Input: None
# Output: True if hacker matches a password Probability: (1/26^4)
def matchedPassword(size):
    # Hacker makes 80,000 four letter passwords
    hackerPasswords = np.random.randint(0, 26**4, size+1)
    # Hacker matched a password if some number was found
    return 1 if (99 in hackerPasswords) else 0

# Repeat 1000 times
def problem4():
    # Variables provided by professor
    k = 7
    m = 80000
    test = 300480

    probability = lambda size: sum(matchedPassword(size) for _ in range(1000))/1000

    print("Probability when hacker has 80,000 passwords:",probability(m))
    print("Probability when hacker has 560,000 passwords:",probability(k*m))
    print("To get probability of {}, hacker needs {} passwords".format(probability(test), test))

problem4()
