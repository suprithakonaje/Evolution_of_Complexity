import numpy as np

import math

from utils import hebbian_learning, calculateutility, relaxation, modconmatrix, initialiseweightsformodularconnmatrix

if __name__ == '__main__':
    # For S2

    si = modconmatrix(10, 5, 0.01)
    sj = modconmatrix(10, 5, 0.01)
    w = initialiseweightsformodularconnmatrix(10)

    lr_rate = 0.002
    N = 150
    relax_rate = math.exp(150)

    u_o = {}
    u_o_before_change = {}
    count_o = 0

    u_l = {}
    u_l_after_change = {}
    count_l = 0

    for i in range(N):
        count_o += 1
        utility = calculateutility(si, sj, w, 10)
        u_o[count_o] = utility
        w = relaxation(N, 10, si, sj, relax_rate, w)
        if count_o > 100:
            u_o_before_change[count_o] = np.mean(np.abs(u_o))
            u_o = {}
            count_o = 0

    for i in range(N):
        count_l += 1
        w = hebbian_learning(si, sj, w, lr_rate)
        utility = calculateutility(si, sj, w, 10)
        u_l[count_l] = utility
        w = relaxation(N, 10, si, sj, relax_rate, w)
        if count_l > 100:
            u_l_after_change[count_l] = np.mean(np.abs(u_l))
            u_l = {}
            count_l = 0
