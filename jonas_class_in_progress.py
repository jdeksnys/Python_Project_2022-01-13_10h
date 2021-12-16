import os
os.system('Clear')

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp



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
    
    Y=np.array([f(i) for i in reference])                                        # f(a) result matrix
    M=[]                                                                         # coefficient matrix (pre-calc). append()
    for j in reference:
        coeff_ls=[]
        for i in range(0,n+1):
            coeff_ls.append(j**i)                                                # starts from power 0, so includes 1st a
        coeff_ls.append((-1)**j)
        M.append(coeff_ls)
    M=np.array(M)
    
    
    X=sp.solve(M,Y)                                                              # coefficient matrix (calculate)
    error_absolute_h=abs(X[-1])                                                  # deleted append(), set var. directly
    # =============================================================================
    print(X)
    # =============================================================================
    
    def p(x):                                                                      # changed to sum()
        return sum(a*x**count for a, count in enumerate(X))
    
    
    
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
