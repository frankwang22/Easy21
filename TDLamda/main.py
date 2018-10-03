import Q as Q
import QMC as QMC
import numpy as np
from numpy.random import randint
import step as play
import train as train


#print playerstate, dealerstate

QSARSA = Q.Qtable()

Qbest=train.train(1000000)
MSE = np.zeros([11])

for a in range (0,11):
    lamda = float(a) / 10
    for b in range (0,1000):
        playerstate = randint(1, 11)
        dealerstate = randint(1, 11)
        QSARSA.New(playerstate,dealerstate,lamda)
    for x in range(1, 21):
        for y in range(1, 11):
            for z in range(0, 2):
                MSE[a] += (QSARSA.Q[x, y, z] - Qbest[x, y, z]) ** 2
    print "lamda", lamda, "a", a, "x", x ,"y", y, "z", z
    print "Qsarsa",QSARSA.Q
    print "Qbest", Qbest






print MSE