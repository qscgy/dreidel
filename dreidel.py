import numpy as np
import matplotlib.pyplot as plt
from numpy.testing._private.utils import assert_equal

nplayers = 7
startcoins = 5
winners = np.zeros(nplayers)

for i in range(1000):
    coins = np.zeros(nplayers)+startcoins
    pot = startcoins
    while True:
        nz = np.nonzero(coins)[0]
        if len(nz) < 2:
            break
        for i in nz:
            roll = np.random.randint(0, high=4)
            if roll==0:
                # nun
                pass
            elif roll==1:
                # gimel
                coins[i]+=pot
                pot = 0
            elif roll==2:
                # hey
                half = pot//2
                coins[i]+=half
                pot -= half
            else:
                # shin
                coins[i] -= 1
                pot += 1
    # print(np.nonzero(coins)[0][0])
    winners[np.nonzero(coins)[0][0]] += 1
print(winners)