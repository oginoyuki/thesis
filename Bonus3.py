# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:11:10 2019

@author: user
"""

import numpy as np
from gurobipy import *

try:
    f = open('dataset_Bonus_3.txt')
    n = int(f.readline())
    rho = int(f.readline())
    h = int(f.readline())

    #Create a new Model
    no_units=40;
    M = Model('Bonus_3') #自己給定模型名稱
    
    #把sigma讀進來---------------------------------------------------------
    sigma = np.zeros((n,n),float)
    for i in range(n):
        j=0
        for x in f.readline().strip().split('\t'):
            sigma[i][j] = float(x)
            j = j + 1
    #把mu讀進來------------------------------------------------------------ 
    mu = np.zeros((n),float)
    j = 0
    for x in f.readline().strip().split('\t'):
        mu[j] = float(x)
        j = j + 1
   
    #Create variables
    X = M.addVars(no_units, vtype=GRB.BINARY, name="X")
    Y = M.addVars(no_units, no_units, vtype=GRB.CONTINUOUS, name="Y")
    print(X)
    print(Y)
    #Integrate new variables
    M.update()
    
    #Set objective MINIMIZE 算目標式
    obj = 0
    for i in range(n):
        j=i+1
        for j in range(n):
            obj = obj + (sigma[i][j] * Y[(i,j)])
    M.setObjective(obj, GRB.MINIMIZE)

    #Set Constrains
    #算出Xi的總和----------------------------------------------------------
    X_sum = 0
    j = 0
    for j in range(n):
        X_sum += X[j]
    M.addConstr(X_sum == h) #呼叫Constrain這個模型進來，X_sum要等於1
    
    #算出uiXi的總和--------------------------------------------------
    mux_sum = 0
    j = 0
    for j in range(n):
        mux_sum += mu[j] * X[j]
    M.addConstr(mux_sum >= rho) #形成第二個Constrain
    
    for i in range(n):
        j=i+1
        for j in range(n):
            M.addConstr(Y[(i,j)] >= 0)
            M.addConstr(Y[(i,j)] <= X[i])
            M.addConstr(Y[(i,j)] <= X[j])
            M.addConstr(Y[(i,j)] >= (X[i]+X[j]-1))
            

    M.optimize()
    M.write('mip1.lp')
    
    for v in M.getVars(): #從m裡面拿到的變數一個一個丟到v裡面
        print(v.varName,'=',v.x) #一個一個v把它的結果吐出來
        #print(v)
    print('Obj=', M.objVal)

except GurobiError:
    print('Encountered a Gurobi error')
