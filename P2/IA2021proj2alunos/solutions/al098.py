# -*- coding: utf-8 -*-
"""
Grupo al098
Student id #92510
Student id #93737
"""

# calcular probabilidades dos ganhos e definir gi min de profundidade e retornar 
# o valor mais provavel (valor do y)

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



def createTreeAux(D, Y, noise = False, f_index = -1, f_list = []):
    total = len(Y)

    p = Y.count(1)
    n = total - p
    initial_entropy = incerteza(p, n)
    if initial_entropy == 0:
        if Y[0]:
            return [0, 1, 1]
        return [0, 0, 0]

    ''' get number of features '''
    features = len(D[0])

    ''' caculate GI and entropies '''
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

    maxGI = max(GI)
    feature_index = GI.index(maxGI)
    if maxGI == 0:
        ''' no information gain '''
        ''' returns a recursive function call for each of the right and left branches '''

        feature_index = f_index + 1
        ''' left tree branch '''
        D0 = []
        D1 = []
        ''' right tree branch '''
        Y0 = []
        Y1 = []
        while (True):
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
        L1 = createTreeAux(D0, Y0, noise, feature_index, f_list)
        ''' recursively build the right branch '''
        L2 = createTreeAux(D1, Y1, noise, feature_index, f_list)
        # print(L1)
        # print(L2)

        if L1 == L2:
            ''' avoid long trees '''
            ''' por exemplo:
                [0, [1, [2, 0, 1], [2, 1, 0]], [1, [2, 0, 1], [2, 1, 0]]] -> [1, [2, 0, 1], [2, 1, 0]] '''
            L = L1
        if L1[1] == L2[1]:
            L = [L1[0], L1[1], [feature_index, L1[2], L2[2]]]
        else: #elif L1 != L2:
            L = [feature_index, L1, L2]
        return L

    ''' if the information gain is neither maximum or minimum,
        call the recursive function on the feature element(s) that stil has(have) entropy (incerteza != 0) '''
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
                    if Y[i]:
                        L += [1]
                    else:
                        L += [0]
                    break
    L1 = L[1]
    L2 = L[2]
    if type(L1) == list and type(L2) == list and L1[1] == L2[1]:
        # L = [feature_index, L1[0], L1[1]]
        L = [L1[0], L1[1], [feature_index, L1[2], L2[2]]]

    return L

def createdecisiontree(D,Y, noise = False):

    ''' transfrom numpy array into list '''
    Y_list = list(Y.tolist())
    # [11, [6, [1, 1, [3, 0, [4, 0, 1]]], [4, 0, [3, 0, 1]]], [6, [1, 1, [3, 0, [4, 0, 1]]], 1]]
    ''' call the recursive function '''
    T = createTreeAux(D, Y_list)
    print(T)

    return T

#  [11, [6, [1, 1, [3, 0, [4, 0, 1]]], [4, 0, [3, 0, 1]]], [6, [1, 1, [3, 0, [4, 0, 1]]], 1]]

#  L1 = [6, [1, 1, [3, 0, [4, 0, 1]]], [4, 0, [3, 0, 1]]]
#  L1feature = 
#  L2 = [6, [1, 1, [3, 0, [4, 0, 1]]], 1]
D = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = np.array([0, 0, 0, 1])
createdecisiontree(D, Y)
#                          11
#                  6               6
#         padrao      val1   padrao    1
# # [6, [1, 1, [3, 0, [4, 0, 1]]], [4, 0, [3, 0, 1]]
# # [6, [1, 1, [3, 0, [4, 0, 1]]], 1]

#         if L1[1] == L2[1]:
#             L = [L1[0], L1[1], [feature_index, L1[2], L2[2]]]
        

            
# [6, [1, 1, [3, 0, [4, 0, 1]]], [11, [4, 0,1 [3, 0, 1]], 1]]