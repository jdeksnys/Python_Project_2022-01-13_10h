import os
os.system('Clear')

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp
from datetime import datetime



def f(x):
    return np.sin(x)




class BestApprox:

    def __init__(self,f):
        self.f=f
        self.tol=1.e-8
        self.max_iter=10

    def remez(self,n,lower,upper):
        self.n=n
        self.lower=lower
        self.upper=upper
        self.reference=list(np.linspace(self.lower,self.upper,n+2))

        for i in range(self.max_iter+1):

            Y=np.array([f(i) for i in self.reference])                                        # f(a) result matrix
            M=[]                                                                         # coefficient matrix (pre-calc). append()
            for count, j in enumerate(self.reference,start=0):
                coeff_ls=[]
                for i in range(0,n+1):
                    coeff_ls.append(j**i)                                                # starts from power 0, so includes 1st a
                coeff_ls.append((-1)**count)
                M.append(coeff_ls)
            M=np.array(M)
            X=sp.solve(M,Y)                                                              # coefficient matrix (calculate)


            def p(x):                                                                      # changed to sum()
                return sum(a*x**count for count,a in enumerate(X[:-1]))
            
            error_absolute_h=abs(X[-1])                                                  # deleted append(), set var. directly    
            error=([abs(f(x)-p(x)) for x in np.linspace(self.lower,self.upper,100)])
            max_error=max(error)

            if (max_error-error_absolute_h)<self.tol:
                print(f'convergense observaed after {i} iterations, the coefficients of the polynomial that is the best approx of f are:{X[:-2]}')
                # np.delete(M,1) ????????
                break


            index=error.index(max_error)                                                 # find x of max error
            interval=list(np.linspace(self.lower,self.upper,100))
            eta=interval[index]
            self.reference.append(eta)
            self.reference.sort()


            if self.reference[0]<=eta<=self.reference[-1]:                                           # replace sign checking, faster
                if (f(eta)-p(eta))/(f(self.reference[self.reference.index(eta)-1])-p(self.reference[self.reference.index(eta)-1]))>0:
                    self.reference.remove(self.reference[self.reference.index(eta)-1])
                else:
                    self.reference.remove(self.reference[self.reference.index(eta)+1])
            if eta<self.reference[0]:
                if ((f(eta)-p(eta))/(f(self.reference[0])-p(self.reference[0])))>0:
                    self.reference.remove(self.reference[0])
                else:
                    self.reference.remove(self.reference[-1])
            if eta>self.reference[-1]:
                if (f(eta)-p(eta))/(np.sign(f(self.reference[-1])-p(self.reference[-1])))>0:
                    self.reference.remove(self.reference[-1])
                else:
                    self.reference.remove(self.reference[0])
            self.reference.sort()
            Y[self.reference.index(eta)]=f(eta)
            for i in range(1,n+1):
                M[self.reference.index(eta),i]=(self.reference[self.reference.index(eta)])**i

        # print(self.reference)
        # print(error_absolute_h)
        # x=np.linspace(self.lower,self.upper,100)
        # plt.plot(x,f(x),'k')
        # plt.plot(x,p(x),'r:',linewidth=4)






def f(x):
    return np.sin(x)

a=BestApprox(f).remez(4,0,6)