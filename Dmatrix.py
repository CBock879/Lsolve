#TODO: rename x and y
# create map


import numpy as np
class dmat:
    def __init__ ( self , x , y,H,B ):
        self.dmatrix = np.zeros((x,y,x,y) ) 
        self.X, self.Y,self.b, self.h = x,y,h,b
        self.dx = self.b/ self.x
        self.dy = self.h/ self.y

        #self.map = np.zeros(x,y)
    def ddu(self,x,y):

        self.dmatrix[x][y][x][y] = -4
        self.dmatrix[x][y][x-1][y] = 1
        self.dmatrix[x][y][x][y-1] = 1
        self.dmatrix[x][y][x+1][y] = 1
        self.dmatrix[x][y][x][y+1] = 1

#spits out matrix to be solved
    def outmatrix(self):
        elements = self.X * self.Y
        dm = self.dmatrix.reshape(elements,elements)
        return( dm)

    #creates dirichlet type boundry condtion at index x and y
    def dirichelt(self,x,y):
        self.dmatrix[x][y][x][y]   = 1 
        self.dmatrix[x][y][x-1][y] = 0
        self.dmatrix[x][y][x][y-1] = 0
        self.dmatrix[x][y][x+1][y] = 0
        self.dmatrix[x][y][x][y+1] = 0 

    #create nuemann boundry condition at index x and y 
    #normal vector is nx and ny
    def nuemann(self,x,y,nx,ny):
        x_comp,y_comp  = self.map(nx,ny)

        #clears surrounding area
        self.dmatrix[x][y][x][y]   = 1 
        self.dmatrix[x][y][x-1][y] = 0
        self.dmatrix[x][y][x][y-1] = 0
        self.dmatrix[x][y][x+1][y] = 0
        self.dmatrix[x][y][x][y+1] = 0 
        
        #normal Vector
        self.dmatrix[x][y][x_comp][y] = -nx
        self.dmatrix[x][y][x][y_comp] = -ny    
         
    #map function made for 
    def map(self,a,b):
        if (a>0):
            p = int( np.ceil(a / self.dx ))
        else
        q = int( np.ceil(b / self.dy ))
        return(p,q)
