# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy
f = open('dataset.txt')
n = int(f.readline())
m = int(f.readline())
h = int(f.readline())
rho = float(f.readline())
#print(n, m, h, rho)

#把sigma讀進來---------------------------------------------------------
sigma = numpy.zeros((n,n),float)
for i in range(n):
    j=0
    for x in f.readline().strip().split('\t'):
        sigma[i][j] = float(x)
        #print('sigma[i][j]=',sigma[i][j])
        j = j + 1

#把mu讀進來------------------------------------------------------------                
mu = numpy.zeros((n),float)
j = 0
for x in f.readline().strip().split('\t'):
    mu[j] = float(x)
    #print('mu[j]=', mu[j])
    j = j + 1

#算出Xi的總和----------------------------------------------------------
K=400 #200種可能
X = numpy.random.randint(0,21,size=(K,n))
#print(X)
X_sum = [0]*K
for k in range(K):
    j = 0
    for j in range(n):
        X_sum[k] = X_sum[k] + X[k][j]
    #print(X_sum[k])

#Xi總和的限制式-----------------------------------------------------------
mux_sum = [0]*K
for k in range(K):
    while(X_sum[k] > h):
        point=0 #見HW_help1
        for i in range(n): #X.size=10
            if( X[k][point] < X[k][i] ):
                point = i #做位置紀錄，可以找到最大值的位置
        #print("The largest value", X[point], "is in the position",point)
        X[k][point] = 50 - (X_sum[k] - X[k][point])
        if(X[k][point] < 0):
            X[k][point] = 0
        X_sum[k] = 0
        for j in range(n):
            X_sum[k] = X_sum[k] + X[k][j]
        #算出uiXi的總和--------------------------------------------------
        for j in range(n):
            mux_sum[k] = mux_sum[k] + (mu[j] * X[k][j])
        while(mux_sum[k] < rho): #uixi總和的限制式
            X = numpy.random.randint(0,21,size=(K,n))
            X_sum = [0]*K
            j = 0
            for j in range(n):
                X_sum[k] = X_sum[k] + X[k][j]    
    
    while(X_sum[k] < h):
        point=0 #見HW_help1
        for i in range(n): #X.size=10
            if( X[k][point] > X[k][i] ):
                point = i #做位置紀錄，可以找到最小值的位置
        #print("The smallest value", X[point], "is in the position",point)
        X[k][point] = X[k][point] + (50 - X_sum[k])
        if(X[k][point] > 20):
            X[k][point] = 20
        X_sum[k] = 0
        for j in range(n):
            X_sum[k] = X_sum[k] + X[k][j]
        #算出uiXi的總和------------------------------------------------------
        for j in range(n):
            mux_sum[k] = mux_sum[k] + (mu[j] * X[k][j])
        while(mux_sum[k] < rho): #uixi總和的限制式
            X = numpy.random.randint(0,21,size=(K,n))
            X_sum = [0]*K
            j = 0
            for j in range(n):
                X_sum[k] = X_sum[k] + X[k][j]
#print(X)
#print(X_sum)
#print(mux_sum)
            
#算目標式
Objective = [0]*K
for k in range(K):
    for i in range(n):
        j = 0
        for j in range(n):
            Objective[k] = Objective[k] + (sigma[i][j] * X[k][i] * X[k][j])
#print(Objective)

#找目標式最小值-------------------------------------------------------------
Point_k=0
for k in range(1,k):
    if(Objective[k] < Objective[Point_k]):
        Point_k=k
#print(Objective[Point_k])

Ite = 50
x = [0] *Ite
y = [0] *Ite

for iteration in range(Ite):
    for k in range (K):
        #print(k,Point_k)
        if(k!=Point_k):
            X_sum[k] = 0
            mux_sum[k] = 0
            Objective[k] = 0
            X[k][0] = numpy.random.randint(0,21)
            X[k][1] = numpy.random.randint(0,21)
            X[k][2] = numpy.random.randint(0,21)
            X[k][3] = numpy.random.randint(0,21)
            X[k][4] = numpy.random.randint(0,21)
            X[k][5] = numpy.random.randint(0,21)
            X[k][6] = numpy.random.randint(0,21)
            X[k][7] = numpy.random.randint(0,21)
            X[k][8] = numpy.random.randint(0,21)
            X[k][9] = numpy.random.randint(0,21)
            
            #print('Point_k=',Point_k,'k=',k)
            #print(X[k][0])
            for j in range(n):
                X_sum[k] = X_sum[k] + X[k][j]
            #print(X_sum[k])
            while(X_sum[k] > h):
                point=0 
                for i in range(n): 
                    if( X[k][point] < X[k][i] ):
                        point = i #做位置紀錄，可以找到最大值的位置
                X[k][point] = 50 - (X_sum[k] - X[k][point])
                if(X[k][point] < 0):
                    X[k][point] = 0
                X_sum[k] = 0
                for j in range(n):
                    X_sum[k] = X_sum[k] + X[k][j]
            #print(X_sum[k])
               #算出uiXi的總和--------------------------------------------------
                for j in range(n):
                    mux_sum[k] = mux_sum[k] + (mu[j] * X[k][j])
                while(mux_sum[k] < rho): #uixi總和的限制式
                    X = numpy.random.randint(0,21,size=(K,n))
                    X_sum = [0]*K
                    j = 0
                    for j in range(n):
                        X_sum[k] = X_sum[k] + X[k][j]    
            #print(X_sum[k])
            while(X_sum[k] < h):
                point=0 
                for i in range(n): 
                    if( X[k][point] > X[k][i] ):
                        point = i #做位置紀錄，可以找到最小值的位置
                X[k][point] = X[k][point] + (50 - X_sum[k])
                if(X[k][point] > 20):
                    X[k][point] = 20
                X_sum[k] = 0
                for j in range(n):
                    X_sum[k] = X_sum[k] + X[k][j]
                #算出uiXi的總和------------------------------------------------------
                for j in range(n):
                    mux_sum[k] = mux_sum[k] + (mu[j] * X[k][j])
                while(mux_sum[k] < rho): #uixi總和的限制式
                    X = numpy.random.randint(0,21,size=(K,n))
                    X_sum = [0]*K
                    j = 0
                    for j in range(n):
                        X_sum[k] = X_sum[k] + X[k][j]
                
            for i in range(n):
                for j in range(n):
                    Objective[k] = Objective[k] + (sigma[i][j] * X[k][i] * X[k][j])
            #print(Objective[k])
        for k in range (0,K):
            if(Objective[k] < Objective[Point_k]):
                Point_k = k
        print("Incumbent solution:",iteration+1, end="\t")
        for j in range(n):
            print("xj=",X[Point_k][j],"\t")
        x[iteration]=iteration+1
        y[iteration]=Objective[Point_k]
#Display the visualization results
plt.plot(x, y) #line plot線圖
plt.ylabel('Objective value')
plt.xlabel('Iterations')
plt.show()
print(Objective[Point_k])
