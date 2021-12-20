# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:29:41 2021
@author: otto_
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp 
import sys

def f(x):
    return np.sin(x)
lower=-np.pi
upper=np.pi
n=4
reference_points=list(np.linspace(lower,upper,n+2))
print(reference_points)

class BestApprox:
    tol=1.e-12
    max_iter=100
    a=[]
    error_absolute_h=[]
    def __init__(self,function):
        self.function=function
    def remez(self,reference,n):
        self.reference=reference
        self.n=n
        error_absolute_h=[]
        for i in range(self.max_iter):
            Y=np.array([self.function(i) for i in reference])
            M=np.zeros((n+2)**2).reshape(n+2,n+2)
        
            for i in range(n+2):
                M[i,0]=1
                M[i,-1]=(-1)**i
            for i in range(n+2):
                for j in range(1,n+1):
                    M[i,j]=(reference[i])**j
               
            X=sp.solve(M,Y)
            
            error_absolute_h.append(abs(X[-1])) 
            
            def p(x):
                return sum(X[i]*x**i for i in range(n+1))
            
            error=([abs(f(x)-p(x)) for x in np.linspace(lower,upper,100)])
            max_error=max(error)
            if max_error-abs(X[-1])<self.tol:
                
                np.set_printoptions(precision=4)
                print(f'convergense observed after {i+1} iterations, the coefficients of the polynomial that is the best approx of f are:{X[:-1]}')
                
                print([(p(reference[i])-f(reference[i])) for i in range(len(reference))])
                print(error_absolute_h)
                
                self.a=X[:-1]
                break
            index=error.index(max_error)
            interval=list(np.linspace(lower,upper,100))
            eta=interval[index]
            reference.append(eta)
            reference.sort()
            
            
            if reference[0]<=eta<=reference[-1]:
                if np.sign(f(eta)-p(eta))==np.sign(f(reference[reference.index(eta)-1])-p(reference[reference.index(eta)-1])):
                    reference.remove(reference[reference.index(eta)-1])
                else:
                    reference.remove(reference[reference.index(eta)+1])
            elif eta<reference[0]:
                if np.sign(f(eta)-p(eta))==np.sign(f(reference[0])-p(reference[0])):
                    reference.remove(reference[0])
                else:
                    reference.remove(reference[-1])
            elif eta>reference[-1]:
                if np.sign(f(eta)-p(eta))==np.sign(f(reference[-1])-p(reference[-1])):
                    reference.remove(reference[-1])
                else:
                    reference.remove(reference[0])
            reference.sort()
            Y[reference.index(eta)]=f(eta)
            for i in range(1,n+1):
                M[reference.index(eta),i]=(reference[reference.index(eta)])**i
    def plot_f_remez(self):
        x=np.linspace(lower,upper,100)
        return plt.plot(x,self.function(x),'r',x,sum(self.a[i]*(x**i) for i in range(n+1)),'k:')

sin=BestApprox(f)
print(sin.remez(reference_points,4)) 
print(sin.plot_f_remez())

    




    
    






    

  


  












