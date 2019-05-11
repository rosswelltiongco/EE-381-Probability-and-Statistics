"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Rosswell Tiongco
" Project 6 - Markov Chains
" EE 381    - Probability and Statistics
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import numpy as np
import matplotlib.pyplot as plt
import random

#             A      B      C
pA       = [1/2,   1/4,   1/4]
pB       = [1/4,   1/8,   5/8]
pC       = [1/3,   2/3,     0]
pInitial = [1/4,    0,    3/4]

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 1. A three state markov chain
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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

def nSideDie0(p):
    return nSideDie(p) - 1

def makeMarkov(chainLength):
    S = [nSideDie0(pInitial)]
    for i in range(chainLength-1):
        if S[-1] == 0:
            S.append(nSideDie0(pA))
        elif S[-1] == 1:
            S.append(nSideDie0(pB))
        elif S[-1] == 2:
            S.append(nSideDie0(pC))
    return S


def problem1():
    # # Generate and plot 1 markov chain
    plt.figure("1A")
    plt.title("3 State Markov Chain")
    plt.xlabel("Time Step")
    plt.ylabel("State")
    x = range(15)
    plt.plot(x,makeMarkov(15),"ro",LINESTYLE='--')
    plt.show()


    # Make 10,000 markove chains
    massChain  = [(makeMarkov(15)) for x in range(10_000)]
    transposed = np.transpose(massChain)

    stateA = []
    stateB = []
    stateC = []

    for row in transposed:
        stateA.append((list(row).count(0)/10_000))
        stateB.append((list(row).count(1)/10_000))
        stateC.append((list(row).count(2)/10_000))

    # Plot the results of 10,000 markov chains
    plt.figure("1B")
    plt.title("10,000 3-State Markov Chains")
    plt.xlabel("Time step")
    plt.ylabel("State Probability")
    x = range(15)
    plt.plot(x,stateA,'ro',LINESTYLE='--', label='State 0')
    plt.plot(x,stateB,'bo',LINESTYLE='--', label='State 1')
    plt.plot(x,stateC,'go',LINESTYLE='--', label='State 2')
    plt.legend(loc='upper right')
    plt.show()

problem1()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 2. Google Page Rank Algorithm
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def problem2():
    # Define state transition matrix
                    #  A    B    C    D    E
    P = np.matrix([ [  0,   1,   0,   0,   0],  # A
                    [1/2,   0, 1/2,   0,   0],  # B
                    [1/3, 1/3,   0,   0, 1/3],  # C
                    [  1,   0,   0,   0,   0],  # D
                    [  0, 1/3, 1/3, 1/3,   0]]) # E

    # Define initial probability state (step 0)
    V = [[1/5, 1/5, 1/5, 1/5, 1/5],    [  0,   0,   0,   0,   1]]

    for i in range(2):
        transposed = np.transpose(V[i])
        newP = V[i]
        bigList = [V[i]]

        for num in range(20): #20
            newP = np.matmul(newP,P)
            stepData = newP.tolist()[0]
            bigList.append(stepData)

        data = np.transpose(bigList).tolist()
        plt.figure("2")
        plt.title("Google Page Rank with initial vector: '{}'".format(V[i]))
        plt.xlabel("Chain Position")
        plt.ylabel("State")
        x = range(21)
        plt.plot(x,data[0],'ro',LINESTYLE='--',label='A')
        plt.plot(x,data[1],'bo',LINESTYLE='--',label='B')
        plt.plot(x,data[2],'go',LINESTYLE='--',label='C')
        plt.plot(x,data[3],'ko',LINESTYLE='--',label='D')
        plt.plot(x,data[4],'co',LINESTYLE='--',label='E')
        plt.legend(loc='upper right')
        plt.show()

        print("Probabilities for intial vector {}".format(V[i]))
        results = [(str(x[-1])[:6],data.index(x)) for x in data]
        # print(sorted(results,reverse=True))
        getPrinted = [print("State: {} Probability: {}".format(x[1],x[0])) for x in sorted(results,reverse=True)]

problem2()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"3. Simulate a five state absorbing Markov Chain
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Define state transition matrix
#        0    1    2    3    4
P = [ [  1,   0,   0,   0,   0],  # 0
      [0.3,   0, 0.7,   0,   0],  # 1
      [  0, 0.5,   0, 0.5,   0],  # 2
      [  0,   0, 0.6,   0, 0.4],  # 3
      [  0,   0,   0,   0,   1]]  # 4


def makeMarkov(chainLength):
    S = [2]
    for i in range(chainLength-1):
        if S[-1] == 0:
            S.append(nSideDie0(P[0]))
        elif S[-1] == 1:
            S.append(nSideDie0(P[1]))
        elif S[-1] == 2:
            S.append(nSideDie0(P[2]))
        elif S[-1] == 3:
            S.append(nSideDie0(P[3]))
        elif S[-1] == 4:
            S.append(nSideDie0(P[4]))
    return S


def problem3():
    # Generate and plot 1 markov chain
    plt.figure("1A")
    plt.title("3 State Markov Chain")
    plt.xlabel("Chain Position")
    plt.ylabel("State")
    x = range(15)
    plt.plot(x,makeMarkov(15),"ro",LINESTYLE='--')
    plt.show()

problem3()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"4. Computer the probability of absorbsion using the simulatd chain
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def problem4():
    absorbingState = [makeMarkov(15)[-1] for x in range(10_000)]
    end2 = absorbingState.count(0)/10_000
    end4 = absorbingState.count(4)/10_000
    print("B20: {}\nB24: {}".format(end2,end4))

problem4()
