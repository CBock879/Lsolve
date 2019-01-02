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
 
#Param a: x location to be mapped to the matrix
#Param b: y location to be mapped to the matrix 
#maps xy coordanates into array indices (p,q) for the corresponding element
def map(a,b):

    p =  int(np.floor(a / dx ))
    q =  int(np.floor(b / dy ))
    #print(p,q) 

    return(p,q)

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

#parametric boundry
sum_vals = 0  
num_vals = 1

#values that store index of last eleement mapped 
last_i = x+3 
last_j = y+3 

p_dx = np.gradient(xb)
p_dy = np.gradient(yb)
local_dx = 0
local_dy = 0
for i in range(0,pb_steps-1):

    i_pb , j_pb = map(xb[i],yb[i])

    if (True!=(i_pb > x or j_pb > y)):
        if(last_i==last_i & last_j==j_pb):
            local_dx += p_dx[i]
            local_dy += p_dy[i]
            
            num_vals += 1
            nx , ny = normal(local_dx/num_vals,local_dy/num_vals,1)
            Region.nuemann(i_pb,j_pb,nx,ny)

        else:
            num_vals = 1
            local_dx = p_dx[i]
            local_dy = p_dy[i] 
            nx , ny = normal(local_dx/num_vals,local_dy/num_vals,1)
            #print(nx,ny,i_pb,j_pb)
            Region.nuemann(i_pb,j_pb,nx,ny)
            #nuemann boundry condition

        solmat[i_pb,j_pb] = 0 
        last_i,last_j = i_pb, j_pb
    
# TODO move to the DMatrix file
#for i in range(0,pb_steps-1):
#    i_pb , j_pb = map(xb[i],yb[i])
#
#    if (True!=(i_pb > x or j_pb > y)):
#        if(last_i==last_i & last_j==j_pb):
#            sum_vals += zb[i]
#            num_vals += 1
#
#        else:
#            num_vals = 1
#            sum_vals = zb[i] 
#            
#            #dirichet boundry condition
#            Region.dirichlet(i_pd,j_pb,)
#
#
#        solmat[i_pb,j_pb] =  sum_vals/num_vals
#        last_i,last_j = i_pb, j_pb
#
#gets matrix of the entire region
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
