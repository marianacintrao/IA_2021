# -*- coding: utf-8 -*-
"""
Grupo al098
Student id #92510
Student id #93737
"""

from collections import Counter
import numpy as np

incertezas = []
GI = []

def incerteza(p, n):
    ''' returns I( p / p+n, n / p+n )  '''
    if p == 0 or n == 0:
        return 0
    P = p/(p+n)
    N = n/(p+n)
    x = np.array([P, N])
    xlog = np.log2(x)
    return (-P * xlog[0]) - (N * xlog[1])

def createTreeAux(D,Y, noise = False):
    total = len(Y)
    n = Y.count(0)
    p = total - n
    initial_entropy = incerteza(p, n)

    features = len(D[0])  

    global incertezas
    incertezas = []
    global GI
    GI = []

    for feature in range(0, features):

        resto = 0
        incerteza_feature = {}

        #feature Y list is a list of pairs [feature instance, Y instance] 
        feature_Y_list = [] 
        #feature elements is a set of all unique feature elements
        feature_elements = set() 
        for i in range(0, total):
            feature_Y_list += [[D[i][feature], Y[i]]]
            feature_elements.add(D[i][feature])

        for e in feature_elements:
            p_instances = feature_Y_list.count([e, 1])
            n_instances = feature_Y_list.count([e, 0])
            I = incerteza(p_instances, n_instances)
            incerteza_feature[e] = I
            resto += ((p_instances + n_instances) / total) * I

        GI += [initial_entropy - resto]
        incertezas += [incerteza_feature]

    # feature com maior valor de GI
    max_f = GI.index(max(GI))
    return 


def createdecisiontree(D,Y, noise = False):

    Daux = D.copy()
    Yaux = Y.copy()
    
    while(1):
        createTreeAux(Daux, Yaux)
        feature_index = GI.index(max(GI))
        if max(GI) == 0 or all(value == 0 for value in incertezas[feature_index].values()):
            break
        for i in range(len(Yaux)):
            if Daux[i][feature_index] != "++"




    return [0,0,1] # to remove
    # return T


D = [['a', '+', 'n'], ['a', '++', 's'], ['m', '+', 'n'], ['a', '++', 'n'], ['b', '+++', 's'], ['m', '+++', 's'], ['a', '+++', 's'], ['b', '+', 's']]
Y = [0, 1, 0, 0, 1, 1, 1, 0]
createdecisiontree(D, Y)
# createdecisiontree([[0,0],[0,1],[1,0],[1,1]], [0,0,0,1])
# createdecisiontree([['s', 's', 'b'],['n', 'n', 'a'], ['s', 's', 'c'], ['s', 'n', 'c'], ['n', 's', 'b'], ['n', 'n', 'a'], ['s', 'n', 'c'], ['n', 'n', 'a']], [0, 1, 0, 0, 0, 1, 0, 0])
D = [['a', '+', 'n'], ['a', '++', 's'], ['m', '+', 'n'], ['a', '++', 'n'], ['b', '+++', 's'], ['m', '+++', 's'], ['a', '+++', 's'], ['b', '+', 's']]
Y = [0, 1, 0, 0, 1, 1, 1, 0]





