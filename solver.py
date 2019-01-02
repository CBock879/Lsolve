import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
from Dmatrix import dmat
from Pboundry import Pbound,normal

# b,h base and height of retangular region
b = 8 
h =  8

vector_field = False  

#parametric equation for boundry
pb_steps = 200
xb, yb, zb = Pbound(pb_steps,0)

x = 80 # X resoltion
dx = b/x

y = 80 # y resolution
dy = h/ y
 

#currently set up to be Prandtal stress function
#defines region
Region = dmat(x,y,h,b)

#plots internal boundries
plt.plot(xb,yb) 

# edge boundries on the top bottom left and right sides
solmat = np.ones((x,y))
solmat = np.negative(solmat)
solmat[:,0] =   1
solmat[:,y-1] = 1  
solmat[0,:]  =  1
solmat[x-1,:] = 1

#sets up inital matrix
for i in range(1,x-1):
    for j in range(1,y-1):
        Region.ddu(i,j)

#qol thing
x= x-1 
y = y-1

for i in range(0,y+1):
    #left boundry 
    #Region.dmatrix[0][i][0][i] = -1
    Region.dmatrix[0][i][1][i] = 1
    #right boundry
    Region.dmatrix[x][i][x][i] = 1
    #Region.dmatrix[x][i][x-1][i] = -1

#boundry conditions
for i in range(0,x):
    #top boundry
    Region.dmatrix[i][0][i][0] = 1
    #Region.dmatrix[i][0][i-1][0] = -1
    #Region.dmatrix[i][0][i][1] = -1
    #bottom boundry
    Region.dmatrix[i][y][i][y] = 1
    #Region.dmatrix[i][y][i-1][y] = -1
    #Region.dmatrix[i][y][i][y-1] = -1
A = Region.outmatrix()

#print(solmat)
#reshapes matrix to be solvable
solmat  = solmat.reshape((x+1)*(y+1))

#solves the region
sols =  linalg.solve(A,solmat)

#reshapes solutions and graphs
sols = sols.reshape(x+1,y+1)
sols = np.matrix.transpose(sols)

px = np.linspace(0,b,x+1)
py = np.linspace(0,h,y+1)

#graphs
plt.gca().set_aspect("equal")
function = plt.contourf(px,py, sols,10)
plt.colorbar(function)

if (vector_field):
    #converts px and py into mesh grid for vectors
    px, py = np.meshgrid(px,py) 
    gradient = np.gradient(sols)
    plt.quiver(px,py,gradient[1],gradient[0])
    
#np.set_printoptions(precision=1)
#print(sols)

plt.show()
