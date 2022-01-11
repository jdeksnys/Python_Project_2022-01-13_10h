<<<<<<< HEAD
import os
os.system('Clear')
import unittest

import numpy as np
from project_Remez_class_BestApprox import BestApprox

def banana():
    return x**2

class TestBestApprox():
    def test___init__(self,function):
        self.assertRaises(Exception,__init__,x**2)
        #self.f='a'
    def test_remez(self):
        self.assertRaises(Exception,__init__)
        #self.f='a'
    
=======
import numpy as np
import matplotlib.pyplot as plt
from remez import BestApprox
import unittest
#import math

def f(x):
   func=[np.sin(x),np.cos(x),np.tan(x),np.log(x),np.arcsin(x),np.arccos(x),np.arctan(x)]
   reference_points=list(np.linspace(0,2*np.pi,6))
   return func[1]


b=BestApprox(f)
class TestBestApprox(unittest.TestCase):
    def test_remez(self):
         def f(x):
             func=[np.sin(x),np.cos(x),np.tan(x),np.arcsin(x),np.arccos(x),np.arctan(x)]
             for n in func:
                 self.assertRaises(TypeError,b.remez(),n)
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
>>>>>>> 01c97f76335f5bf98c0f15855d694ec0e1349e80
