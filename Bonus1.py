# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 20:11:10 2019

@author: user
"""

import numpy as np
from gurobipy import *

try:
    f = open('dataset_Bonus_1.txt')
    n = int(f.readline())
    m = int(f.readline())
    h = int(f.readline())
    rho = float(f.readline())
    #print(n, m, h, rho)
    #Create a new Model
    no_input_factors=2; #sigma, mu
    no_output_factors=1; #x
    no_units=10;
    M = Model('Bonus_1') #自己給定模型名稱
    
    #把sigma讀進來---------------------------------------------------------
    sigma = np.zeros((n,n),float)
    for i in range(n):
        j=0
        for x in f.readline().strip().split('\t'):
            sigma[i][j] = float(x)
            #print('sigma[i][j]=',sigma[i][j])
            j = j + 1
    #把mu讀進來------------------------------------------------------------ 
    mu = np.zeros((n),float)
    j = 0
    for x in f.readline().strip().split('\t'):
        mu[j] = float(x)
        #print('mu[j]=', mu[j])
        j = j + 1
   
    #Create variables
    X = M.addVars(no_units, vtype=GRB.BINARY, name="X")
    #print(type(X))
    #Integrate new variables
    M.update()
    #Set objective MINIMIZE 算目標式
    obj = 0
    for i in range(n):
        j=0
        for j in range(n):
            obj = obj + (sigma[i][j] * X[i] * X[j])
    M.setObjective(obj, GRB.MINIMIZE)
    #print(Objective)
    
    #Set Constrains
    #算出Xi的總和----------------------------------------------------------
    X_sum = 0
    j = 0
    for j in range(n):
        X_sum += X[j]
    #print(X_sum)
    M.addConstr(X_sum == 1) #呼叫Constrain這個模型進來，X_sum要等於1
    #算出uiXi的總和--------------------------------------------------
    mux_sum = 0
    j = 0
    for j in range(n):
        mux_sum += mu[j] * X[j]
    M.addConstr(mux_sum >= rho) #形成第二個Constrain

    M.optimize()
    M.write('mip1.lp')
    
    for v in M.getVars(): #從m裡面拿到的變數一個一個丟到v裡面
        print(v.varName,'=',v.X) #一個一個v把它的結果吐出來
    print('Obj=', m.objVal)

except GurobiError:
    print('Encountered a Gurobi error')