#TODO: rename x and y # create map


import numpy as np
class dmat:
    def __init__ ( self , x , y,H,B ):
        self.dmatrix = np.zeros((x,y,x,y) ) 
        self.X, self.Y,self.b, self.h = x,y,B,H
        self.dx = B/x
        self.dy = H/y 

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
        self.dmatrix[x][y][x+1][y] = -nx
        self.dmatrix[x][y][x][y+1] = -ny    
        self.dmatrix[x][y][x-1][y] = nx
        self.dmatrix[x][y][x][y-1] = ny
    
   
    #map function made for use with might not be needed 
  #  def (self,a,b):
  #      if (a>0):
  #          p = 1
  #      else if(a = 0):
  #          p = 0
  #      else: 
  #          p = -1

  #      if (b>0):
  #          q = 1
  #      else if (b = 0):
  #          q = 0
  #      else:
  #          q = -1

  #      return(p,q)
