import train as train
import numpy as np
import Q as Q
import numpy as np
from numpy.random import randint
import step as play
from plot import plot

A=train.train(5000000)

print A
#Z=np.transpose(np.max(A,axis=2))

#plot (Z)

