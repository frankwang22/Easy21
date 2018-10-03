import numpy as np
from numpy.random import randint
def step (dealercard, playersum, a):
    if a == 0:
        if randint(0, 3) < 2:
            newplayersum = playersum+randint(1, 11)
        else:
            newplayersum = playersum-randint(1, 11)
        if newplayersum>21 or newplayersum<1:
            return [dealercard, newplayersum, -1, 1]
        else:
            return [dealercard, newplayersum, 0, 0]

    if a == 1:
        dealersum = dealercard
        while dealersum > 0 and dealersum < 17:
            if randint(0,3) < 2:
                dealersum = dealersum+randint(1, 11)
            else:
                dealersum = dealersum-randint(1, 11)
        if dealersum < 1 or dealersum > 21:
            return [dealersum, playersum, 1, 1]
        elif dealersum > playersum:
            return [dealersum, playersum, -1, 1]
        elif playersum > dealersum:
            return [dealersum, playersum, 1, 1]
        else:
            return [dealersum, playersum, 0, 1]
