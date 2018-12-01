import numpy as np
class dmat:
    def __init__ ( self , x , y ):
        self.dmatrix = np.zeros((x,y,x,y))
    def ddu(self,x,y):
        self.dmatrix[x][y][x][y] = -4
        self.dmatrix[x][y][x-1][y] = 1
        self.dmatrix[x][y][x][y-1] = 1
        self.dmatrix[x][y][x+1][y] = 1
        self.dmatrix[x][y][x][y+1] = 1

