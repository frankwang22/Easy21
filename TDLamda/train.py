import numpy as np
import QMC as Q
from numpy.random import randint
import step as play


def train(iteration):
    LookupTable = Q.Qtable()
    for x in range(1, iteration):
        playersum = np.zeros(30)
        actionstaken = np.zeros(30)
        playerstate = randint(1, 11)
        dealerstate = randint(1, 11)
        x = 0

        action = LookupTable.getaction(playerstate, dealerstate)
        state = play.step(dealerstate, playerstate, action)
        playersum[0] = playerstate
        actionstaken[0] = action
        # print "state action space first", playerstate, dealerstate, action
        if state[3] == 1:
            LookupTable.Qupdate(playerstate, dealerstate, action, state[2])
            # print "state action space", state[1], state[0], action
            # print "reward", state[2]

        while state[3] == 0:
            x = x + 1
            playersum[x] = state[1]
            action = LookupTable.getaction(state[1], state[0])
            actionstaken[x] = action
            state = play.step(state[0], state[1], action)

        while x > 0:
            LookupTable.Qupdate(int(playersum[x]), dealerstate, int(actionstaken[x]), state[2])
            # print "state action space", int(playersum[x]), dealerstate, int(actionstaken[x])
            # print "reward", state[2]
            x = x - 1
            '''
            LookupTable.Qupdate(playerstate, dealerstate, action, state[2])

            playerstate=20
            dealerstate=randint(1,11)
            action=LookupTable.getaction(playerstate,dealerstate)
            state=play.step()
            LookupTable.Qupdate(playerstate,dealerstate,action,state[2])
            '''
    return LookupTable.Q
