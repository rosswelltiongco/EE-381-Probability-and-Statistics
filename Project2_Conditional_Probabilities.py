"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Rosswell Tiongco
" Project 2 - Conditional Probabilities
" EE 381    - Probability and Statistics
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 1 - Probability of erroneous transmission
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import numpy as np

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
    p0 = [.60,.40]
    e0 = [.95,.05]
    e1 = [.03,.97]

    S_list = []
    R_list = []
    for count in range(100000):
        S = nSideDie(p0)-1
        R = nSideDie(e1)-1 if (S == 1) else nSideDie(e0)-1
        S_list.append(S)
        R_list.append(R)

    #print(S_list)
    errors = sum(1 for bit in range(100000) if S_list[bit] != R_list[bit])/100000
    print("Problem 1: {}".format(errors))

problem1()
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 2 - Conditional probability: P(R=1|S=1)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def problem2():
    p0 = [.60,.40]
    e0 = [.95,.05]
    e1 = [.03,.97]

    S_list = []
    R_list = []
    for count in range(100000):
        S = nSideDie(p0)-1
        R = nSideDie(e1)-1 if (S == 1) else nSideDie(e0)-1
        S_list.append(S)
        R_list.append(R)

    success = 0
    total = 0
    for bit in range(100000):
        if S_list[bit] == 1:
            total+=1
            if R_list[bit] == 1:
                success+=1
    probability = success/total
    print("Problem 2: {}".format(probability))

problem2()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 3 - Conditional probability: P(S=1|R=1)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def problem3():
    p0 = [.60,.40]
    e0 = [.95,.05]
    e1 = [.03,.97]

    S_list = []
    R_list = []
    for count in range(100000):
        S = nSideDie(p0)-1
        R = nSideDie(e1)-1 if (S == 1) else nSideDie(e0)-1
        S_list.append(S)
        R_list.append(R)

    success = 0
    total = 0
    for bit in range(100000):
        if R_list[bit] == 1:
            total+=1
            if S_list[bit] == 1:
                success+=1
    probability = success/total
    print("Problem 3: {}".format(probability))
problem3()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Problem 4 - Enhanced transmission method
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def problem4():
    p0 = [.60,.40]
    e0 = [.95,.05]
    e1 = [.03,.97]

    S_list = []
    R_list = []
    for count in range(100000):
        S = nSideDie(p0)-1
        R = [nSideDie(e1)-1 if (S == 1) else nSideDie(e0)-1 for _ in range(3)]
        S_list.append(S)
        R_list.append(R)

    decoded = [1 if bits.count(1) > bits.count(0) else 0 for bits in R_list]
    probability = sum(1 for bit in range(100000) if S_list[bit] != decoded[bit])/100000
    print("Problem 4: {}".format(probability))

problem4()
