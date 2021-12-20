# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 07:51:39 2021

@author: graesoan
"""
import numpy as np

def pol(Coeficient,point):  # construct polynomial(general) 
    N = len(Coeficient)
    Result = 0
    Result = Coeficient[0]
    for i in range(1,N-1):
        Result+= Coeficient[i]*(point**i)
    return Result


class BestApprox:  # Task 1: Creating a class
    
    maxiter = 1000
    tol = 1e-6
    
    def __init__(self,f):
        self.f = f

    def remez(self,f,reference,n):
       Error = 1000
       Point = reference  
       while Error>self.tol:
        
            # Task 2
            b = np.transpose(np.zeros((1,n+2)))  # construct a system of equations to find err, coefficients of pol. 
            Matriz = np.zeros((n+2,n+2))
            for i in range(n+2):
                for j in range(n+2):
                    if j==0:
                        Matriz[i,j] = 1
                    elif j==n+1:
                        Matriz[i,j] = (-1)**i
            for i in range(n+2):
                for j in range(1,n+1):
                    Matriz[i,j] = reference[i]**j
            
            for i in range(n+2):
                b[i] = f(reference[i])
            
            
            A_Coefficient = np.linalg.solve(Matriz,b)  # solve the system of equation
            Coefficient = []
            for element in A_Coefficient:
                Coefficient.append(float(element))
                
            if abs(Coefficient[-1])<self.tol:
                return Coefficient
            
            for i in range(len(reference)-1):  # step 4 of Remez algorithm
                number = 10
                interval = np.linspace(reference[i],reference[i+1],number)
                h = (interval[-1]-interval[1])/number
                for element in interval:
                    Df = ((f(element)-pol(Coefficient,element)) - (f(element-h)-pol(Coefficient,element-h)))/h
                    if Df<1e-6:
                        if element>= reference[i] and element<= reference[i+1]:
                            if np.sign(f(element)-pol(Coefficient,element)) == np.sign(f(reference[i])-pol(Coefficient,reference[i])) :
                                reference[i] = element
                            else:
                                reference[i+1] = element
                        elif element<reference[0]:
                            if np.sign(f(element)-pol(Coefficient,element)) == np.sign(f(reference[0])-pol(Coefficient,reference[0])) :
                                reference[0] = element
                            else:
                                reference[i+1] = element
                        
                        elif element>reference[i+1]:
                            if np.sign(f(element)-pol(Coefficient,element)) == np.sign(f(reference[i+1])-pol(Coefficient,reference[i+1])) :
                                reference[i+1] = element
                            else:
                                reference[0] = element
                                
# Test Class
function = lambda x : np.sin(x)+ 8

myClass = BestApprox(function)
print(myClass)
print(myClass.maxiter)

myClass.maxiter = 300
print(myClass.maxiter)
print(myClass.tol)
myClass.tol = 1e-10
print(myClass.tol)
Result = myClass.remez(function,[2,3,4,5],2)
print(Result)  # function converges 





