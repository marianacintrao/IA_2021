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

def createTreeAux(D, Y, noise = False, f_index = 0):
    
    total = len(Y)
    n = Y.count(0)
    p = total - n
    initial_entropy = incerteza(p, n)

    features = len(D[0])  

    incertezas = []
    GI = []

    for feature in range(0, features):

        resto = 0
        incerteza_feature = {}

        feature_Y_list = [] 
        for i in range(0, total):
            feature_Y_list += [[D[i][feature], Y[i]]]

        for e in [0, 1]:
            p_instances = feature_Y_list.count([e, 1])
            n_instances = feature_Y_list.count([e, 0])
            I = incerteza(p_instances, n_instances)
            incerteza_feature[e] = I
            resto += ((p_instances + n_instances) / total) * I

        GI += [initial_entropy - resto]
        incertezas += [incerteza_feature]

    # print(GI, incertezas)

    # feature com maior valor de GI
    feature_index = GI.index(max(GI))
    if max(GI) == 0:
        if feature_index == f_index:
            feature_index += 1
        L = [feature_index] 
        D0 = []
        D1 = []
        Y0 = []
        Y1 = []
        for i in range(len(D)):
            if D[i][feature_index] == 0:
                Y0 += [Y[i]]
                D0 += [D[i]]
            else: # D[i][feature_index] == 1:
                Y1 += [Y[i]]
                D1 += [D[i]]

        if D0 == []:
            return [1]
        else:
            L += [createTreeAux(D0, Y0, noise, feature_index)] 
        if D1 == []:
            return [0]
        else:               
            L += [createTreeAux(D1, Y1, noise, feature_index)]  
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
    T = createTreeAux(D, Y)
    print(T)

    return [0,0,1] # to remove
    # return T


D = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
Y = [0, 1, 1, 0, 0, 1, 1, 0]


# # este afinal estava certo, passei foi o teste mal
# D = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
# Y = [0, 1, 0, 1, 0, 1, 0, 1]

# D = [[0,0], [0,1], [1,0], [1,1]]
# Y = [0, 0, 0, 1]
# createdecisiontree(D, Y)




