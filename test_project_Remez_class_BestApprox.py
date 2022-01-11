import unittest
import project_Remez_class_BestApprox
import numpy as np



class TestBestApprox(unittest.TestCase):

    def test_remez(self):
        reference_points='abc'
        def f(x):
            return np.sin(x)
        a=project_Remez_class_BestApprox.BestApprox(f)
        self.assertRaises(TypeError,a.remez,reference_points)
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                             
                 
