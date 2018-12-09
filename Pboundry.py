import numpy as np
import sympy as sp
#container file for parametric boundry functions
#TODO allow for user to input own internal boundries at runtime

#pb steps: steps for the parametric boundry
def Pbound(steps):
    #parametric equation for boundry
    p = sp.symbols('p')
    pr = np.linspace(0,np.pi*2,steps) 
    
    #ype = y parametric function expression
    ype = sp.sin(p)*2+4     #sympy expression of y
    yb = sp.lambdify(p,ype) #lambda function of y
    yp = yb(pr)             #yvalues of points on the boundry
    
    xpe = sp.cos(p)*2+4
    xb = sp.lambdify(p,xpe)
    xp = xb(pr) 
    
    zpe = 1+0*p 
    zb = sp.lambdify(p,zpe)
    zp = yb(pr)     
    return(xp,yp,zp)
