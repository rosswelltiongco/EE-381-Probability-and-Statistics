"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Rosswell Tiongco
" Project 5 - Confidence Intervals
" EE 381    - Probability and Statistics
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 1. Effect of sample size on confience intervals
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
N = 1500000 # Bearings
m = 55 # Mean
sd = 5 # Standard deviation
n = range(1,201) # Sample size 1,2,...200

B = np.random.normal(m,sd,N) # Generate population

averages = []

for num in n:
    x = B[random.sample(range(N),num)]
    mean = x.mean()
    # sd = np.std(x,ddof=1)
    averages.append(mean)


plt.figure("1A")
plt.title("Sample means and 95% confidence intervals")
plt.xlabel("Sample Size")
plt.ylabel("average weight (X bar)")
plt.plot(n,averages,"ob",marker='x',linestyle='none')
plt.plot(n,[mean for x in n]) # Plot average line
x = np.linspace(1,200)
plt.plot(x,m+1.96*sd/(x**(1/2)),color="red",linestyle='--')
plt.plot(x,m-1.96*sd/(x**(1/2)),color="red",linestyle='--')
plt.ylim(top=55+10)
plt.ylim(bottom=55-10)

plt.figure("1B")
plt.title("Sample means and 99% confidence intervals")
plt.xlabel("Sample Size")
plt.ylabel("average weight (X bar)")
plt.plot(n,averages,"ob",marker='x',linestyle='none')
plt.plot(n,[mean for x in n]) # Plot average line
x = np.linspace(1,200)
plt.plot(x,m+2.58*sd/(x**(1/2)),color="green",linestyle='--')
plt.plot(x,m-2.58*sd/(x**(1/2)),color="green",linestyle='--')
plt.ylim(top=55+10)
plt.ylim(bottom=55-10)
plt.show()
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 2. Using the sample mean to estimate the population mean
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

population = np.random.normal(m,sd,N) # Generate population
n95Counter = 0
n99Counter = 0
t95_5Counter = 0
t95_40Counter = 0
t95_120Counter = 0
t99_5Counter = 0
t99_40Counter = 0
t99_120Counter = 0

def experiment(sampleSize):
    global n95Counter
    global n99Counter
    global t95_5Counter
    global t95_40Counter
    global t95_120Counter
    global t99_5Counter
    global t99_40Counter
    global t99_120Counter

    sample = B[random.sample(range(N),sampleSize)] # Generate sample of 5 from population
    sampleMean = np.mean(sample) # Mean of sample
    sampleSD = np.std(sample,ddof=1) #standard deviation of sample
    # [xmean - 1.96(sd/root(n), xmean + 1.96(sd/root(n)))]
    n95 = [sampleMean - 1.96*sampleSD/(sampleSize**.5), sampleMean + 1.96*sampleSD/(sampleSize**.5)]
    n99 = [sampleMean - 2.58*sampleSD/(sampleSize**.5), sampleMean + 2.58*sampleSD/(sampleSize**.5)]
    t95_5 = [sampleMean - 2.78*sampleSD/(sampleSize**.5), sampleMean + 2.78*sampleSD/(sampleSize**.5)]
    t95_40 = [sampleMean - 2.02*sampleSD/(sampleSize**.5), sampleMean + 2.02*sampleSD/(sampleSize**.5)]
    t95_120 = [sampleMean - 1.98*sampleSD/(sampleSize**.5), sampleMean + 1.98*sampleSD/(sampleSize**.5)]
    t99_5 = [sampleMean - 4.6*sampleSD/(sampleSize**.5), sampleMean + 4.6*sampleSD/(sampleSize**.5)]
    t99_40 = [sampleMean - 2.71*sampleSD/(sampleSize**.5), sampleMean + 2.71*sampleSD/(sampleSize**.5)]
    t99_120 = [sampleMean - 2.62*sampleSD/(sampleSize**.5), sampleMean + 2.62*sampleSD/(sampleSize**.5)]


    if n95[0] < m <n95[1]:
        n95Counter += 1
    if n99[0] < m <n99[1]:
        n99Counter += 1
    if t95_5[0] < m <t95_5[1]:
        t95_5Counter += 1
    if t95_40[0] < m <t95_40[1]:
        t95_40Counter += 1
    if t95_120[0] < m <t95_120[1]:
        t95_120Counter += 1
    if t99_5[0] < m <t99_5[1]:
        t99_5Counter += 1
    if t99_40[0] < m <t99_40[1]:
        t99_40Counter += 1
    if t99_120[0] < m <t99_120[1]:
        t99_120Counter += 1

def clearAll():
    n95Counter = 0
    n99Counter = 0
    t95_5Counter = 0
    t95_40Counter = 0
    t95_120Counter = 0
    t99_5Counter = 0
    t99_40Counter = 0
    t99_120Counter = 0



run5_10_000 = [experiment(5) for x in range(10_000)]
n95p = n95Counter/10_000
print("Normal 95",n95p)
n99p = n99Counter/10_000
print("Normal 99",n99p)
t95_5p = t95_5Counter/10_000
print("t 95 5",t95_5p)
t99_5p = t99_5Counter/10_000
print("t 99 5",t99_5p)
clearAll()
run40_10_000 = [experiment(40) for x in range(10_000)]
t95_40p = t95_40Counter/10_000
print("t 95 40",t95_40p)
t99_40p = t99_40Counter/10_000
print("t 99 40",t99_40p)
clearAll()
run120_10_000 = [experiment(120) for x in range(10_000)]

t99_120p = t99_120Counter/10_000
print("t 99 120",t99_120p)
t95_120p = t95_120Counter/10_000
print("t 95 120",t95_120p)
clearAll()
