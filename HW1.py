# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import matplotlib.pyplot as plt
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
#K=200 #200種可能
X = numpy.random.randint(0,21,size=(n,1))
#print(X)
X_sum = numpy.zeros((1,1),int)
j = 0
for j in range(n):
    X_sum = X_sum + X[j]
#print(X_sum)

#Xi總和的限制式-----------------------------------------------------------
while(X_sum > h):
    point=0 #見HW_help1
    for i in range(n): #X.size=10
        if( X[point] < X[i] ):
            point = i #做位置紀錄，可以找到最大值的位置
    #print("The largest value", X[point], "is in the position",point)
    X[point] = 50 - (X_sum - X[point])
    if(X[point] < 0):
        X[point] = 0
    X_sum = 0
    for j in range(n):
        X_sum = X_sum + X[j]
    mux_sum = numpy.zeros((1,1),float) #算出uiXi的總和------------------------
    for j in range(n):
        mux_sum = mux_sum + (mu[j] * X[j])
    while(mux_sum < rho): #uixi總和的限制式
        X = numpy.random.randint(0,21,size=(n,1))
        X_sum = numpy.zeros((1,1),int)
        j = 0
        for j in range(n):
            X_sum = X_sum + X[j]
#print(X)
#print(X_sum)
#print(mux_sum)

while(X_sum < h):
    point=0 #見HW_help1
    for i in range(n): #X.size=10
        if( X[point] > X[i] ):
            point = i #做位置紀錄，可以找到最小值的位置
    #print("The smallest value", X[point], "is in the position",point)
    X[point] = X[point] + (50 - X_sum)
    if(X[point] > 20):
        X[point] = 20
    X_sum = 0
    for j in range(n):
        X_sum = X_sum + X[j]
    mux_sum = numpy.zeros((1,1),float) #算出uiXi的總和------------------------
    for j in range(n):
        mux_sum = mux_sum + (mu[j] * X[j])
    while(mux_sum < rho): #uixi總和的限制式
        X = numpy.random.randint(0,21,size=(n,1))
        X_sum = numpy.zeros((1,1),int)
        j = 0
        for j in range(n):
            X_sum = X_sum + X[j]
#print(X)
#print(X_sum)
#print(mux_sum)   

#HW1-------------------------------------------------------------------   
"""
Ite=50
K=200 #200種可能
X=numpy.random.randint(0,21,size=(K,n)) #範圍介於0~100
Objective=[0]*K

for k in range(K):
    while(( mu * X[k][n] < rho ) or (X[k][n]!=h)):
        for i in range(n):
            X[k][i]=numpy.random.randint(0,21)
        #X[k][1]=np.random.randint(0,21)
        #X[k][2]=np.random.randint(0,21)
        #X[k][3]=np.random.randint(0,21)
        #X[k][4]=np.random.randint(0,21)
#print(X)
        
for k in range(K):
    Objective[k]=sigma*X[k][i]*X[k][j]
    #print(Objective[k])

Point_k=0
for k in range(1,k):
    if(Objective[k]<Objective[Point_k]):
        Point_k=k

print("Incumbent solution:", end="\t")
print("x1=",X[Point_k][0],":\t x2=",X[Point_k][1],":\t x3=",X[Point_k][2],":\t x4=",X[Point_k][3],":\t x5=",X[Point_k][4])

x = [0] * Ite
y = [0] * Ite

for iteration in range (Ite): #重複執行50次
    for k in range (0,k):
        if(k!=Point_k): #只要不是最好的那一個Point_k就重取
            X[k][0]=np.random.randint(0,101)
            X[k][1]=np.random.randint(0,101)
            X[k][2]=np.random.randint(0,101)
            X[k][3]=np.random.randint(0,101)
            X[k][4]=np.random.randint(0,101)
            while((X[k][0]-X[k][1]<23) or (X[k][1]-2*X[k][2]<25) or (X[k][2]+X[k][3]<26) or (X[k][3]-X[k][4]<12)):
                X[k][0]=np.random.randint(0,101)
                X[k][1]=np.random.randint(0,101)
                X[k][2]=np.random.randint(0,101)
                X[k][3]=np.random.randint(0,101)
                X[k][4]=np.random.randint(0,101)
            Objective[k]=3*X[k][0]+10*X[k][1]+5*X[k][2]+2*X[k][3]-3225*X[k][4]-3*X[k][0]*X[k][2]-4*X[k][1]*X[k][2]+6*X[k][2]*X[k][2]
        for k in range (0,K):
            if(Objective[k]<Objective[Point_k]):
                Point_k=k
        print("Incumbent solution:",iteration+1, end="\t")
        print("x1=",X[Point_k][0],":\t x2=",X[Point_k][1],":\t x3=",X[Point_k][2],":\t x4=",X[Point_k][3],":\t x5=",X[Point_k][4])
        x[iteration]=iteration+1
        y[iteration]=Objective[Point_k]
#Display the visualization results
plt.plot(x, y) #line plot線圖
plt.ylabel('Objective value')
plt.xlabel('Iterations')
plt.show()
"""
