import unittest
import project_Remez_class_BestApprox
import numpy as np



class TestBestApprox(unittest.TestCase):

    def test_remez(self):
        func1=[np.sin,np.cos,np.tan]
        for n in func1:
            reference_points='abc'
            a=project_Remez_class_BestApprox.BestApprox(f)
            self.assertRaises(TypeError,a.remez,reference_points)
        

    def test_signs(self):
        func=[np.sin,np.cos,np.tan]
        for n in func:
            reference_points=list(np.linspace(0,2*np.pi,6))
            a=project_Remez_class_BestApprox.BestApprox(f)
            a.remez(reference_points)
            for i in range(0,len(a.h_vals)-1):
              if (a.h_vals[i]/a.h_vals[i+1])<0:
                pass
              else:
                raise Exception('h-values not alternating in sign!')
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                             
                 
