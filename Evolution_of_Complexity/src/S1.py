import numpy as np

import math

from utils import sprandsym, initialiseweightsforsymmetricmatrix, hebbian_learning, calculateutility, relaxation

if __name__ == '__main__':
    # For S1

    si = sprandsym(30, 0.06)
    sj = sprandsym(30, 0.06)
    w = initialiseweightsforsymmetricmatrix(30)

    lr_rate = 0.0002
    N = 500
    relax_rate = math.exp(N)

    u_o = {}
    u_o_before_change = {}
    count_o = 0

    u_l = {}
    u_l_after_change = {}
    count_l = 0

    for i in range(N):
        count_o += 1
        utility = calculateutility(si, sj, w, 30)
        u_o[count_o] = utility
        w = relaxation(N, 30, si, sj, relax_rate, w)
        if count_o > 100:
            u_o_before_change[count_o] = np.mean(np.abs(u_o))
            u_o = {}
            count_o = 0

    for i in range(N):
        count_l += 1
        w = hebbian_learning(si, sj, w, lr_rate)
        utility = calculateutility(si, sj, w, 30)
        u_l[count_l] = utility
        w = relaxation(N, 30, si, sj, relax_rate, w)
        if count_l > 100:
            u_l_after_change[count_l] = np.mean(np.abs(u_l))
            u_l = {}
            count_l = 0
