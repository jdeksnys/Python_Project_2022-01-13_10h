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

# reference_points=list(np.linspace(0,2*np.pi,6))
# reference_points='a'


class BestApprox:
    tol=1.e-12
    max_iter=100
    a=[]
    
    def __init__(self,function):
        self.f=function
    def remez(self,reference=None):
        self.name_dict={'lower':'lower bound','upper':'upper bound','n':'degree of polynomial'}
        self.var_dict={'lower':None,'upper':None,'n':None}
        if reference!=None: # if initial guesses provided, utilise given list
            if not isinstance(reference,list):
                raise TypeError("Oops! Initial guess not of 'list' data type.")
            else:
                self.reference=reference
                self.var_dict['lower']=min(self.reference)
                self.var_dict['upper']=max(self.reference)
                self.n=len(self.reference)-2
        elif reference==None: # if no initial guesses provided, prompt until user gives correct input
            for i in self.var_dict:
                while True:
                    try:
                        self.var_dict[str(i)]=float(input(f'Please specify {self.name_dict[str(i)]}: '))
                    except ValueError:
                        raise TypeError('Oops! Input non-numeric! Try again')
                    else:
                        break
            self.n=int(self.var_dict['n']) # for better readability, n will also be stored as attribute instead of dict.
            self.reference=list(np.linspace(self.var_dict['lower'],self.var_dict['upper'],self.n+2))

        error_absolute_h=[]
        max_error_list=[]
        for i in range(self.max_iter):
            Y=np.array([self.f(i) for i in self.reference])
            M=np.zeros((self.n+2)**2).reshape(self.n+2,self.n+2)
        
            for i in range(self.n+2):
                M[i,0]=1
                M[i,-1]=(-1)**i 
            for i in range(self.n+2):
                for j in range(1,self.n+1):
                    M[i,j]=(self.reference[i])**j
               
            X=sp.solve(M,Y)
            
            error_absolute_h.append(abs(X[-1])) 
            
            def p(x):
                return sum(X[i]*x**i for i in range(self.n+1))
            
            error=([abs(f(x)-p(x)) for x in np.linspace(self.var_dict['lower'],self.var_dict['upper'],100)])
            max_error=max(error)
            max_error_list.append(max_error)
            if max_error-abs(X[-1])<self.tol:
                
                np.set_printoptions(precision=4)
                # print(f'convergense observed after {i+1} iterations, the coefficients of the polynomial that is the best approx of f are:{X[:-1]}')
                
                self.h_vals=[(p(self.reference[i])-self.f(self.reference[i])) for i in range(len(self.reference))]
                # print(self.h_vals)
                
                plt.plot(range(1,len(max_error_list)+1),max_error_list,label='max error')
                plt.plot(range(1,len(max_error_list)+1),error_absolute_h,label='h')
                plt.xlabel('number of iterations')
                plt.legend()
                
                self.a=X[:-1]
                break
            index=error.index(max_error)
            interval=list(np.linspace(self.var_dict['lower'],self.var_dict['upper'],100))
            eta=interval[index]
            self.reference.append(eta)
            self.reference.sort()
            
            
            if self.reference[0]<=eta<=self.reference[-1]:
                if ((self.f(eta)-p(eta))/(self.f(self.reference[self.reference.index(eta)-1])-p(self.reference[self.reference.index(eta)-1])))>0:
                    self.reference.remove(self.reference[self.reference.index(eta)-1])
                else:
                    self.reference.remove(self.reference[self.reference.index(eta)+1])
            elif eta<self.reference[0]:
                if ((self.f(eta)-p(eta))/(self.f(self.reference[0])-p(self.reference[0]))):
                    self.reference.remove(self.reference[0])
                else:
                    self.reference.remove(self.reference[-1])
            elif eta>self.reference[-1]:
                if ((self.f(eta)-p(eta))/(self.f(self.reference[-1])-p(self.reference[-1]))):
                    self.reference.remove(self.reference[-1])
                else:
                    self.reference.remove(self.reference[0])
            self.reference.sort()
            Y[self.reference.index(eta)]=self.f(eta)
            for i in range(1,self.n+1):
                M[self.reference.index(eta),i]=(self.reference[self.reference.index(eta)])**i
    def plot_f_remez(self):
            x=np.linspace(self.var_dict['lower'],self.var_dict['upper'],100)
            plt.plot(x,self.f(x),'r',label='function')
            plt.plot(x,sum(self.a[i]*(x**i) for i in range(self.n+1)),'k:',label='polynomial')
            plt.legend()
            # plt.show()

#def f(x):#testing manually
#    func=[np.sin(x),np.cos(x),np.tan(x),np.arcsin(x),np.arccos(x),np.arctan(x)]
#    return func[1]
#if ValueError:
# reference_points=list(np.linspace(-2/np.pi,2/np.pi,6))
#elif IndexError:
#    reference_points=list(np.linspace(0,2*np.pi,4))


# sin=BestApprox(f)
# print(sin.remez(reference_points)) # with initial guess
# sin.remez() # without initial guess (user input)
# sin.plot_f_remez()
# plt.figure(2)
# print(sin.plot_f_remez())

    




    
    






    

  


  












