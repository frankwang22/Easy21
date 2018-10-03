import numpy as np
import step as play
from numpy.random import randint


class Qtable:

    def __init__(self):
        self.Q = np.zeros([22, 11, 2])  # 21,11,2
        self.Naction = np.zeros([22, 11, 2])  # 21,11,2
        self.Nstate = np.zeros([40, 20])  # 21,11
        self.E = np.zeros([22, 11, 2])
        self.N0 = 100

    def New(self, playersum, dealersum,lamda):
        self.E = np.zeros([22, 11, 2])
        terminal = 0
        action = self.getaction(playersum, dealersum)
        while terminal == 0:
            #print "action:", action
            state = play.step(dealersum, playersum, action)
            #print state
            self.Naction[playersum, dealersum, action] = self.Naction[playersum, dealersum, action] + 1
            if state[3] == 0:
                action1 = self.getaction(state[1], state[0])
                #print "action1:", action1
                gamma = state[2] + self.Q[state[1], state[0], action1] - self.Q[playersum, dealersum, action]
                self.E[playersum, dealersum, action] += 1
                for x in range(0, 21):
                    for y in range(0, 10):
                        for z in range(0, 1):
                            #if self.Naction[x, y, z] != 0:
                            if self.E[x,y,z]!=0:
                                self.Q[x, y, z] += (gamma * self.E[x, y, z]) / \
                                                                    (self.Naction[x, y, z])
                                self.E[x,y,z] = lamda*self.E[x,y,z]
                                #print "Q0",x,y,z, self.Q[x,y,z]
                playersum = state[1]
                dealersum = state[0]
                action = action1
                terminal = state[3]
                if state[3] == 1:
                    terminal = 1
                    self.E = np.zeros([22, 11, 2])
            if state[3] == 1:
                #print "terminating calc"
                gamma = state[2] - self.Q[playersum, dealersum, action]
                self.E[playersum, dealersum, action] += 1
                for x in range(1, 21):
                    for y in range(1, 11):
                        for z in range(0, 2):
                            #if self.Naction[x,y,z]!=0:
                            if self.E[x,y,z]!=0:
                                self.Q[x, y, z] += (gamma * self.E[x, y, z]) / (self.Naction[x, y, z])
                                self.E[x, y, z] = lamda * self.E[x, y, z]
                                #print "Q1",x,y,z, self.Q[x,y,z]
                self.E = np.zeros([22, 11, 2])
                terminal=1


    def getaction(self, playersum, dealersum):
        self.Nstate[playersum, dealersum] = self.Nstate[playersum, dealersum] + 1
        e = self.N0 / (self.N0 + self.Nstate[playersum, dealersum])
        if np.random.random() < e:
            if np.random.random() < 0.5:
                return 0
            else:
                return 1
        else:
            if self.Q[playersum, dealersum, 0] >= self.Q[playersum, dealersum, 1]:
                return 0
            else:
                return 1


'''                   
   def Qupdate(self, playersum, dealersum,action,reward,playersum1,dealersum1, terminal):
       self.Naction[playersum,dealersum,action]=self.Naction[playersum,dealersum,action]+1
       if terminal == 0:
           action1 = self.getaction(playersum1,dealersum1)
           gamma = reward + self.Q([playersum1,dealersum1,action1]) - self.Q([playersum,dealersum,action])
           self.E[playersum,dealersum,action]+=1
           for x in range (0,21):
               for y in range(0,10):
                   for z in range (0,1):
                       self.Q[playersum,dealersum,action]+=(gamma*self.E[playersum,dealersum,action])/self.Naction[playersum,dealersum,action]
                       self.E[playersum,dealersum,action]=self.E[playersum,dealersum,action]*self.lamda
           return action1
       if terminal == 1:
           gamma = reward - self.Q[playersum,dealersum]
           self.E = np.zeros([22,11,2])
'''


