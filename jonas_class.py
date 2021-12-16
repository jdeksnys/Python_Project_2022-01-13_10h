import os
os.ssytem('Clear')

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp 
import sys



def f(x):
    return np.sin(x)
n=4
max_iter=10
lower=0
upper=2*np.pi
reference=list(np.linspace(lower,upper,n+2))
print(reference)

tol=1.e-8

for i in range(max_iter+1):
    
    Y=np.array([f(i) for i in reference])
    
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
    # =============================================================================
    #     print(X)
    # =============================================================================
    
    def p(x):
        return X[0]+X[1]*x+X[2]*(x**2)+X[3]*(x**3)+X[4]*(x**4)
    
    
    
    error=([abs(f(x)-p(x)) for x in np.linspace(lower,upper,100)])
    max_error=max(error)
    if max_error-abs(X[-1])<tol:
        print(f'convergense observaed after {i} iterations, the coefficients of the polynomial that is the best approx of f are:{X[:-2]}')
        np.delete(M,1)
        break
    # =============================================================================
    #     print(max_error)
    # =============================================================================
    index=error.index(max_error)
    interval=list(np.linspace(lower,upper,100))
    eta=interval[index]
    reference.append(eta)
    reference.sort()
    # =============================================================================
    #     print(reference)
    #     print(reference.index(eta))
    # =============================================================================
    if reference[0]<=eta<=reference[-1]:
        if np.sign(f(eta)-p(eta))==np.sign(f(reference[reference.index(eta)-1])-p(reference[reference.index(eta)-1])):
            reference.remove(reference[reference.index(eta)-1])
        else:
            reference.remove(reference[reference.index(eta)+1])
    if eta<reference[0]:
        if np.sign(f(eta)-p(eta))==np.sign(f(reference[0])-p(reference[0])):
            reference.remove(reference[0])
        else:
            reference.remove(reference[-1])
    if eta>reference[-1]:
        if np.sign(f(eta)-p(eta))==np.sign(f(reference[-1])-p(reference[-1])):
            reference.remove(reference[-1])
        else:
            reference.remove(reference[0])
    reference.sort()
    Y[reference.index(eta)]=f(eta)
    for i in range(1,n+1):
        M[reference.index(eta),i]=(reference[reference.index(eta)])**i


print(reference)
print(error_absolute_h)

   
x=np.linspace(lower,upper,100)
plt.plot(x,f(x),'k')
plt.plot(x,p(x),'r:',linewidth=4)

  












