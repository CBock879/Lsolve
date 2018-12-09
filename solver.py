import numpy as np
import matplotlib.pyplot as plt
from Dmatrix import dmat
from Pboundry import Pbound

# b,h base and height of retangular region
b = 8 
h =  8

#parametric equation for boundry
pb_steps = 200
xb, yb, zb = Pbound(pb_steps)

x = 50 # X resoltion
dy = b/x

y = 50 # y resolution
dx = h/ y

#a is tuple of x,y coordanates
def map(a,b):
    p = int( np.floor(a / dx))
    q = int( np.floor(b / dy))

    return(p,q)

# currently set up to be Prandtal stress function
#defines region
Region = dmat(x,y)

#plots internal boundries
plt.plot(xb,yb) 

# edge boundries on the top bottom left and right sides
solmat = np.ones((x,y))
solmat = np.negative(solmat)
solmat[:,0] = 0
solmat[:,y-1] = 0   
solmat[0,:]  = 0
solmat[x-1,:] =0  


#sets up inital matrix
for i in range(1,x-1):
    for j in range(1,y-1):
        Region.ddu(i,j)

#qol thing
x= x-1 
y = y-1

#boundry conditions
for i in range(0,x+1):

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

#parametric boundry
sum_vals = 0  
num_vals = 1

#placeholders 
last_i = x+3 
last_j = y+3 
for i in range(0,pb_steps-1):
    i_pb , j_pb = map(xb[i],yb[i])
    if ((i_pb > x & j_pb > y)):
          print("x") 
    else:
        #print(i_pb)

        #if there are multiple points of parametric boundry in single elelment then it averages it 
        if(last_i==last_i & last_j==j_pb):
            sum_vals += zb[i]
            num_vals += 1

        else:
            num_vals = 1
            sum_vals = zb[i] 
            Region.dirichelt(i_pb,j_pb) 

        solmat[i_pb,j_pb] =  sum_vals/num_vals
        last_i,last_j = i_pb, j_pb


        

#gets total region matrix 
A = Region.outmatrix()

#inverts differential matrix
A = np.linalg.inv(A)

#print(solmat)
#reshapes matrix to be solvable
solmat  = solmat.reshape((x+1)*(y+1))

np.set_printoptions(threshold = np.nan)
#solves the matrix 
sols = np.matmul(A,solmat)

np.set_printoptions(precision  = 2, suppress = True)

#reshapes solutions and graphs
sols = sols.reshape(x+1,y+1)
sols = np.matrix.transpose(sols)

#for i in range(x):
#    for j in range(y):
#        if( (sols[i,j] > 0)):
#            a = 0
#
#        else:
#            print("help")

px = np.linspace(0,b,x+1)
py = np.linspace(0,h,y+1)

plt.gca().set_aspect("equal")


graph = plt.contour(px,py, sols,10,vmin=-0.00001)
plt.colorbar(graph)
np.set_printoptions(precision=1)
#print(sols)

plt.show()
