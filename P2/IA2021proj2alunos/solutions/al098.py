# -*- coding: utf-8 -*-
"""
Grupo al098
Student id #92510
Student id #93737
"""

from collections import Counter
import numpy as np

def incerteza(p, n):
    ''' returns I( p / p+n, n / p+n )  '''
    if p == 0 or n == 0:
        return 0
    P = p/(p+n)
    N = n/(p+n)
    x = np.array([P, N])
    xlog = np.log2(x)
    return (-P * xlog[0]) - (N * xlog[1])



def createTreeAux(D, Y, noise = False, f_index = -1):

    total = len(Y)

    p = Y.count(1)
    n = total - p
    initial_entropy = incerteza(p, n)
    if initial_entropy == 0:
        return [0, Y[0], Y[0]]

    features = len(D[0])

    incertezas = []
    GI = []

    for feature in range(0, features):
        resto = 0
        incerteza_feature = {}

        p0 = 0
        n0 = 0
        p1 = 0
        n1 = 0

        feature_Y_list = []
        for i in range(0, total):
            l = [D[i][feature], Y[i]]
            feature_Y_list += [l]
            if l[0] == 0 and l[1] == 0:
                n0 += 1
            elif l[0] == 0 and l[1] == 1:
                p0 += 1
            elif l[0] == 1 and l[1] == 0:
                n1 += 1
            else: #if l[0] == 1 and l[1] == 1:
                p1 += 1

        I0 = incerteza(p0, n0)
        incerteza_feature[0] = I0
        resto += ((p0 + n0) / total) * I0
        I1 = incerteza(p1, n1)
        incerteza_feature[1] = I1
        resto += ((p1 + n1) / total) * I1

        GI += [initial_entropy - resto]
        incertezas += [incerteza_feature]

    feature_index = GI.index(max(GI))
    # print(GI)
    if max(GI) == 0:

        feature_index = f_index + 1
        D0 = []
        D1 = []
        Y0 = []
        Y1 = []

        for i in range(len(D)):
            if D[i][feature_index] == 0:
                Y0 += [Y[i]]
                D0 += [D[i]]
            else:
                Y1 += [Y[i]]
                D1 += [D[i]]

        L1 = createTreeAux(D0, Y0, noise, feature_index)
        L2 = createTreeAux(D1, Y1, noise, feature_index)
        if L1 != L2:
            L = [feature_index, L1, L2]
        else: # if L1 != L2:
            L = L1
        return L

    if max(GI) == 1:

        L = [feature_index]
        for key in [0,1]:
            for i in range(len(D)):
                if D[i][feature_index] == key:
                    L += [Y[i]]
                    break
        return L

    L = [feature_index]

    for key in [0,1]:
        if incertezas[feature_index][key] != 0:
            new_D = []
            new_Y = []
            for i in range(len(Y)):
                if D[i][feature_index] == key:
                    new_D += [D[i]]
                    new_Y += [Y[i]]
            L += [createTreeAux(new_D, new_Y)]
        else:
            for i in range(len(D)):
                if D[i][feature_index] == key:
                    L += [Y[i]]
                    break
    return L

def createdecisiontree(D,Y, noise = False):

    Y_list = list(Y.tolist())
    T = createTreeAux(D, Y_list)
    print(T)

    # return [0,0,1] # to remove
    return T


D = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
Y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
# D = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Y = np.array([0, 0, 0, 0])

# D = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Y = np.array([0, 0, 0, 1])
# D = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Y = np.array([0, 0, 1, 1])
# D = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Y = np.array([0, 1, 1, 1])
# D = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# Y = np.array([0, 1, 0, 1, 0, 1, 0, 1])
# D = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# Y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
# D = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# Y = np.array([0, 1, 0, 1, 1, 1, 1, 1])
# D = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# Y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
# D = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# Y = np.array([0, 0, 1, 1, 1, 1, 0, 0])
# D = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# Y = np.array([1, 0, 0, 0, 0, 0, 0, 1])

# vai entrar no max gi = 0:
# D0 = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1]]
# Y0 = [0, 1, 1, 0]
#     vai entrar no max gi = 0:
#     D0 = [[0, 0, 0], [0, 0, 1]]
#     Y0 = [0, 1]



createdecisiontree(D, Y)


# < 22 > #points > 5000 #feat > 12
# [[ True  True  True ...  True False False]
#  [ True  True  True ... False False False]
#  [False False False ... False False False]
#  ...
#  [ True  True False ...  True  True False]
#  [ True  True  True ...  True False  True]
#  [False False False ... False  True  True]]
# [False  True  True ...  True  True  True]
# Test failed
# points 0 /23 short 0 /2