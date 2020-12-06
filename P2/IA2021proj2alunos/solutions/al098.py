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

def calculate(D, Y, total, p, n, initial_entropy, features, incertezas, GI):
    features = len(D[0])

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

def shortenTree(L):
    ''' avoid long trees '''
    ''' por exemplo:
    [0, [1, [2, 0, 1], [2, 1, 0]], [1, [2, 0, 1], [2, 1, 0]]] 
    -> [1, [2, 0, 1], [2, 1, 0]] 
    ou 
    [11, [6, [1, 1, [3, 0, [4, 0, 1]]], [4, 0, [3, 0, 1]]], [6, [1, 1, [3, 0, [4, 0, 1]]], 1]]
    -> [6, [1, 1, [3, 0, [4, 0, 1]]], [11, [4, 0,1 [3, 0, 1]], 1]]
    '''

    left = L[1]
    right = L[2]
    feature_index = L[0]

    if left == right:
        L = left

    if type(left) == list and type(right) == list and (len(left) > 1) and (len(right) > 1):
        if left[1] == right[1]:
            L = [left[0], left[1], [feature_index, left[2], right[2]]]
        elif left[2] == right[2]:
            L = [left[0], [feature_index, left[1], right[1]], left[2]]
    return L

''' =================================================
                Main Recursive Function
    =================================================
'''
def createTreeAux(D, Y, noise = False, f_index = -1):

    TrueNoise = False
    if noise:
        TrueNoise = True
    total = len(Y)

    p = Y.count(1)
    n = total - p
    initial_entropy = incerteza(p, n)
    if initial_entropy == 0:
        if Y[0]:
            return 1
        return 0

    features = 0
    incertezas = []
    GI = []
    calculate(D, Y, total, p, n, initial_entropy, features, incertezas, GI)

    maxGI = max(GI)
    feature_index = GI.index(maxGI)

    L = []

    if maxGI == 0 or TrueNoise:

        ''' No information gain '''
        ''' Returns a recursive function call for each of the right and left branches of a feature.
            The chosen feature has not been expanded yet. '''

        feature_index = f_index + 1
        ''' left tree branch '''
        D0 = []
        D1 = []
        ''' right tree branch '''
        Y0 = []
        Y1 = []

        while (True):
            if (feature_index == len(D[0]) or maxGI <= 0.05) and TrueNoise:
            ''' This is the part that concerns the tests with noise 
            ''' 
                positive = 0
                negative = 0
                for e in Y:
                    if e:
                        positive += 1
                    else:
                        negative += 1
                if positive > negative:
                    return 1
                return 0 
            ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''
            D0 = []
            D1 = []
            Y0 = []
            Y1 = []
            for i in range(len(D)):
                if D[i][feature_index] == 0:
                    Y0 += [Y[i]]
                    D0 += [D[i]]
                elif D[i][feature_index] == 1:
                    Y1 += [Y[i]]
                    D1 += [D[i]]
            if D0 == [] or D1 == []:
                feature_index += 1
            else:
                break

        ''' recursively build the left branch '''
        left = createTreeAux(D0, Y0, TrueNoise, feature_index)
        ''' recursively build the right branch '''
        right = createTreeAux(D1, Y1, TrueNoise, feature_index)

        L = [feature_index, left, right]
    
    else:
        ''' if the information gain is not 0, call the recursive function on the
            feature element(s) that stil has(have) entropy (incerteza != 0) '''
        L = [feature_index]

        for key in [0,1]:
            if incertezas[feature_index][key] != 0:
                new_D = []
                new_Y = []
                for i in range(len(Y)):
                    if D[i][feature_index] == key:
                        new_D += [D[i]]
                        new_Y += [Y[i]]
                L += [createTreeAux(new_D, new_Y, TrueNoise)] 
            else:
                for i in range(len(D)):
                    if D[i][feature_index] == key:
                        if Y[i]:
                            L += [1]
                        else:
                            L += [0]
                        break
    L = shortenTree(L)
    return L

def createdecisiontree(D,Y, noise = False):
    ''' transfrom numpy array into list '''
    Y_list = list(Y.tolist())
    ''' call the recursive function '''
    T = []
    if len(set(Y)) == 1:
        if Y[0]:
            return [0, 1, 1]
        return [0, 0, 0]
    if noise:
        T = createTreeAux(D, Y_list, noise = True)
    else:
        T = createTreeAux(D, Y_list)
    return T


