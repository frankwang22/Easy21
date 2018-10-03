import numpy as np
import step as play
from numpy.random import randint

class Qtable:
    def __init__(self):
        self.Q = np.zeros([22, 11, 2])          # 21,11,2
        self.Naction = np.zeros([22, 11, 2])    # 21,11,2
        self.Nstate=np.zeros([40,20])           # 21,11
        self.N0=100

    def Qupdate(self, playersum,dealersum,action,reward):
        self.Naction[playersum,dealersum,action]=self.Naction[playersum,dealersum,action]+1
        self.Q[playersum,dealersum,action]=self.Q[playersum,dealersum,action]+(reward-self.Q[playersum,dealersum,action])/self.Naction[playersum,dealersum,action]

    def getaction(self, playersum, dealersum):
        self.Nstate[playersum,dealersum]=self.Nstate[playersum,dealersum]+1
        e=self.N0/(self.N0+self.Nstate[playersum,dealersum])
        if np.random.random()<e:
            if np.random.random()<0.5:
                return 0
            else:
                return 1
        else:
            if self.Q[playersum, dealersum, 0]>=self.Q[playersum, dealersum, 1]:
                return 0
            else:
                return 1

