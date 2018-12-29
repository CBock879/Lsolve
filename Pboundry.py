import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
#container file for parametric boundry functions
#TODO allow for user to input own internal boundries at runtime

#param: is _closed: to be used to trim matrix
#param steps: number of step the parametrix boundry goes for
def Pbound(steps,is_closed):
    #parametric equation for boundry
    pr = np.linspace(0,np.pi*2,steps) 
    p = sp.symbols('p')

    #ype = y parametric function expression
    yin = sp.sin(p)* 2+ 4
    yp = sp.lambdify(p,yin)
    y = yp(pr)

    
    #yp =np.random.rand(steps) * 7.7

    xpe = sp.cos(p)*2+4
    xb = sp.lambdify(p,xpe)
    xp = xb(pr) 
   
    #xp =np.random.rand(steps) * 7.7
    
    zpe = p * (2-2)
    zb = sp.lambdify(p,zpe)

    zp = pr * 0   
    
    #print(zb) 

    return(xp,yp,zp)


def as_lambda(xpr):
    p = sp.symbols('p')
    parse_expr(xpr)
    function = sp.lambdify(p,xpr)
    return (function)

def normal(dx,dy,z): 
    dd = np.array([dx,dy,0])
    v = np.array([0,0,z])
    n = np.norm(np.cross(dd,v))
    nx = n[0]
    ny = n[1]
    return (nx,ny) 
