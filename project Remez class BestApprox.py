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
lower=0
upper=2*np.pi
n=4
reference_points=list(np.linspace(lower,upper,n+2))

class BestApprox:
    tol=1.e-8
    max_iter=100
    a=[]
    
    def __init__(self,function):
        self.function=function
    def remez(self,reference,n):
        self.reference=reference
        self.n=n
        for i in range(self.max_iter+1):
            Y=np.array([self.function(i) for i in reference])
            M=np.zeros((n+2)**2).reshape(n+2,n+2)
        
            for i in range(n+2):
                M[i,0]=1
                M[i,-1]=(-1)**i
            for i in range(n+2):
                for j in range(1,n+1):
                    M[i,j]=(reference[i])**j
               
            X=sp.solve(M,Y)
            error_absolute_h=[]
            error_absolute_h.append(abs(X[-1])) 
            def p(x):
                return X[0]+X[1]*x+X[2]*(x**2)+X[3]*(x**3)+X[4]*(x**4)
            
            error=([abs(f(x)-p(x)) for x in np.linspace(lower,upper,100)])
            max_error=max(error)
            if max_error-abs(X[-1])<self.tol:
                print(f'convergense observed after {i} iterations, the coefficients of the polynomial that is the best approx of f are:{X[:-2]}')
                print(f'{error_absolute_h}')
                self.a=(X[:-1])
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
        return plt.plot(x,self.function(x),x,self.a[0]+self.a[1]*x+self.a[2]*(x**2)+self.a[3]*(x**3)+self.a[4]*(x**4))

sin=BestApprox(f)
print(sin.remez(reference_points,4)) 
print(sin.plot_f_remez())
print(sin.plot_f_remez())
    




    
    






    

  


  












