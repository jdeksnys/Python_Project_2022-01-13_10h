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
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
