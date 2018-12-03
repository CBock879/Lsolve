import numpy as np
import matplotlib.pyplot as plt
from Dmatrix import dmat
x = 8 #size of rectangular region 
y= 6 #y = y size of rectangular region

#A*sols = solmat

# currently set up to be Prandtal stress function
#defines region
Region = dmat(x,y)

#boundries
solmat = np.ones((x,y))
solmat[:,0] = 0
solmat[:,y-1] = 0
solmat[0,:]  = 0
solmat[x-1,:] = 0

#sets up inital matrix
for i in range(1,x-1):
    for j in range(1,y-1):
        Region.ddu(i,j)

#qol thing
x= x-1 
y = y-1

#boundry conditions
for i in range(0,x+1):

    #on upper and lower bounds y velocity is zero
    #top boundry
    Region.dmatrix[i][0][i][0] = 1
    #Region.dmatrix[i][0][i][1] = -1
    #bottom boundry
    Region.dmatrix[i][y][i][y] = 1
    #Region.dmatrix[i][y][i][y-1] = -1

for i in range(0,y):
    #left boundry 
    Region.dmatrix[0][i][0][i] = 1
    #Region.dmatrix[0][i][1][i] = -1

    #right boundry
    Region.dmatrix[x][i][x][i] = 1
    #Region.dmatrix[x][i][x-1][i] = -1

#gets differential matrix 
A = Region.outmatrix()

#inverts differential matrix
A = np.linalg.inv(A)

#reshapes matrix to be solvable
solmat  = solmat.reshape((x+1)*(y+1))

np.set_printoptions(threshold = np.nan)
#solves the matrix 
sols = np.matmul(A,solmat)

#reshapes solutions and graphs
sols = sols.reshape(x+1,y+1)
plt.contourf(sols)

plt.show()
