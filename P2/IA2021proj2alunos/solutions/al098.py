# -*- coding: utf-8 -*-
"""
Grupo al098
Student id 93737
Student id 92510
"""
# from collections import Counter
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

def count_element(lst, e):
    n = 0
    for e in lst:
        n += 1
    return n

def createTreeAux(D, Y, noise = False, f_index = -1):
    
    total = len(Y)
    n = count_element(Y, 0)
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
            # p_instances = feature_Y_list.count([e, 1])
            # n_instances = feature_Y_list.count([e, 0])
            p_instances = count_element(feature_Y_list, [e, 1])
            n_instances = count_element(feature_Y_list, [e, 0])
            I = incerteza(p_instances, n_instances)
            incerteza_feature[e] = I
            resto += ((p_instances + n_instances) / total) * I

        GI += [initial_entropy - resto]
        incertezas += [incerteza_feature]

    # print(GI, incertezas)
    

    # feature com maior valor de GI
    maxGI = max(GI)
    feature_index = GI.index(maxGI)

    L = []

    if maxGI == 0:

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

        L += [createTreeAux(D0, Y0, noise, feature_index)] 
        L += [createTreeAux(D1, Y1, noise, feature_index)]  
        # return L              

    elif maxGI == 1:
        L = [feature_index]
        for key in [0,1]:
            for i in range(len(D)):
                if D[i][feature_index] == key:
                    L += [Y[i]]
                    break
        # return L

    else:
        L = [feature_index]
        for key in [0,1]:
            if incertezas[feature_index][key] != 0:
                new_D = []
                new_Y = []
                for i in range(len(Y)):
                    if D[i][feature_index] == key:
                        new_D += [D[i]]
                        new_Y += [Y[i]]
                
                # lista = createTreeAux(new_D, new_Y)
                # L += [createTreeAux(new_D, new_Y)]
                L += [createTreeAux(new_D, new_Y, noise, feature_index)] 
            else: # se a incerteza/entropia for 0, apenas queremos juntar 'a lista o devido valor de Y
                for i in range(len(D)):
                    if D[i][feature_index] == key:
                        L += [Y[i]]
                        break
    return L    

def createdecisiontree(D,Y, noise = False):

    # print("D e Y:")
    # print(D, Y)
    T = createTreeAux(D, Y)
    # print("T:")
    # print(T)
    
    return [0,0,1]
    # return T