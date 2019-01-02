import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
#container file for parametric boundry functions
#TODO allow for user to input own internal boundries at runtime
"""
"""
class  
    """
    Represents a parametric function to br used in a region
    """
    def __init__ (self,steps)
        """
        Args:
            steps: number of steps of parameter p

        Default is a circle
        """
         #parametric equation for boundry
         pr = np.linspace(0,0.1,steps) 

         p = sp.symbols('p')

         #ype = y parametric function expression
         yin = sp.sin(p)+ 4
         yp = sp.lambdify(p,yin)
         yp = yp(pr)

         #yp =np.random.rand(steps) * 7.7

         xpe = sp.cos(p)+4
         xb = sp.lambdify(p,xpe)
         xp = xb(pr) 
        
         #xp =np.random.rand(steps) * 7.7
         
         zpe = p * (2-2)
         zb = sp.lambdify(p,zpe)

         zp = pr * 0   
         
         #print(zb)

         return(xp,yp,zp)
     def generate(self)
     """
     generates the points for the the parametrix function

     """


def normal(dx,dy,z): 
    a = unit([-dy,dx])
    print(a)
    return (a[1],a[0]) 

#get the unit vector of vector a
def unit(a):
    A = np.linalg.norm(a)
    a  = a/A
    return a
