import math
import numpy as np
import scipy.sparse as sparse
from numpy.random.mtrand import RandomState


def sprandsym(n=30, density=0.06):
    s1 = sparse.random(n, n, density=density, random_state=RandomState(1))
    return s1.toarray()


def modconmatrix(n, k=5, p=0.01):
    s2 = np.random.rand(n, n)
    return s2


def semimodmatrix(n):
    s2 = np.random.rand(n, n)
    for i in range(s2.shape[0]):
        for j in range(s2.shape[1]):
            if np.random.uniform(0, 1) < 0.5:
                s2[i][j] = -s2[i][j]
    return s2


def initialiseweightsforsymmetricmatrix(n=30):
    weightmatrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if np.random.uniform(0, 1) < 0.5:
                weightmatrix[i][j] = -1
            else:
                weightmatrix[i][j] = 1
    return weightmatrix


def randomize_states(n):
    np.random.seed()
    s = np.array((n, n))
    for i in range(n):
        for j in range(n):
            if np.random.uniform(0, 1) < 0.5:
                s[i][j] = -1
            else:
                s[i][j] = 1


def initialiseweightsformodularconnmatrix(n=10, k=5, p=0.01):
    weightmatrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if (i / k) == (j / k):
                weightmatrix[i][j] = 1
            else:
                weightmatrix[i][j] = p

    return weightmatrix


def calculateutility(si, sj, w, n):
    utility = 0
    for a in range(n):
        for b in range(n):
            utility += np.abs(w[a][b] * si[a][b] * sj[a][b])
            # print(original_utility)
    return utility


def relaxation(N, n, si, sj, relax_rate, w):
    seq = [-1, 1]
    actual_state = np.zeros((n, n))

    relaxation_factor = math.exp(N) * (3 / 4) * math.log(N / 2)
    fitness = 0
    conn_with_change = 0
    conn_without_change = 0
    cumm_eff = 0

    old_actual_state = actual_state
    cumm_eff += (relax_rate) * np.linalg.norm(np.matmul(np.matmul(si, sj), actual_state) - old_actual_state)
    while relaxation_factor > cumm_eff:
        for i in range(w.shape[0]):
            for j in range(w.shape[1]):
                fitness = fitness + w[i][j]
                # print(relaxation_factor, cumm_eff)
                conn_without_change = conn_without_change + fitness * actual_state[i][j] * si[i][j] * sj[i][j]

                actual_state[i][j] = np.random.uniform(0, 1)
                conn_with_change = conn_with_change + fitness * (-actual_state[i][j]) * si[i][j] * sj[i][j]

                if conn_without_change < conn_with_change:
                    old_actual_state = actual_state[i][j]
                    actual_state[i][j] = -actual_state[i][j]
                    cumm_eff += (relax_rate) * np.linalg.norm(
                        np.matmul(np.matmul(si, sj), actual_state) - old_actual_state)
    return actual_state


def hebbian_weight(weight):
    if weight < -1:
        return -1
    elif weight > 1:
        return 1
    else:
        return weight


def hebbian_learning(si, sj, w, lr):
    for p in range(w.shape[0]):
        for q in range(w.shape[1]):
            if w[p][q] is not None:
                w[p][q] = hebbian_weight(w[p][q] + (lr * si[p][q] * sj[p][q]))
    return w
