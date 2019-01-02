#TODO: rename x and y # create map


import numpy as np
class dmat:
    def __init__ ( self , x , y,H,B ):
        """
        Creates a region to be solved by A*U = B
        U: coloum vector of unknowns
        A: matrix of constraints
        B: coloum of given values

        Args:
            x: x resolution of region
            y: y resolution of region
            B: x dimention of region
            H: y dimention of region
        
        Values:
            solmat: the matrix that will be used to generate "B"
            dmatrix: matrix of constraints
            dx: x distance between elements
            dy: y distance between elements


        """
        self.dmatrix = np.zeros((x,y,x,y)) 

        self.solmat  = np.zeros((x,y))
        self.solmat.fill(0)

        self.X, self.Y,self.b, self.h = x,y,B,H
        self.dx = B/x
        self.dy = H/y 

        #self.map = np.zeros(x,y)
    def ddu(self,x,y):
        """
        Applies a constraint to the second derivative of the region 
        using finite difference method

        Args:
            x: x index of boundry
            y: y index of boundry

        """
        self.dmatrix[x][y][x][y] = -4
        self.dmatrix[x][y][x-1][y] = 1
        self.dmatrix[x][y][x][y-1] = 1
        self.dmatrix[x][y][x+1][y] = 1
        self.dmatrix[x][y][x][y+1] = 1

    def outmatrix(self):
        """
        Turns the 4D "A" matrix into a form that can be solved with matrix math
        
        Returns:
            dm: 2D version of the "A" matrixj
        """
        elements = self.X * self.Y
        dm = self.dmatrix.reshape(elements,elements)
        return( dm)

    def dirichelt(self,x,y):
        self.dmatrix[x][y][x][y]   = 1 
        self.dmatrix[x][y][x-1][y] = 0
        self.dmatrix[x][y][x][y-1] = 0
        self.dmatrix[x][y][x+1][y] = 0
        self.dmatrix[x][y][x][y+1] = 0 

    #create nuemann boundry condition at index x and y 
    #normal vector is nx and ny
    def nuemann(self,x,y,nx,ny):
        """
        creates a nuemann type boundry condition at x and y
        Uses finite difference method

        Args:
            x: x index of boundry
            y: y index of boundry
            nx: x component of normal vector 
            ny: y component of normal vector 

        """
        self.dmatrix[x][y][x][y]   = 0 
        self.dmatrix[x][y][x-1][y] = -nx
        self.dmatrix[x][y][x][y-1] = -ny
        self.dmatrix[x][y][x+1][y] = nx 
        self.dmatrix[x][y][x][y+1] = ny 


    def apply_boundry(self,b_type,p_expr):
        """
        Applys a internal boundry condition to the region
        
        Args:
            b_type: type of boundry (1 is dirichelt, 2 is Nuemann, 3 would be for robin)
            p_expr: the 
        """
        
        
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
    
    def map(self,a,b):
        """
        Maps a location to an index in the region 

        Args:
            a: x coordanate of the location 
            b: y coordanate of the location

        Returns:
            q: x index of location
            p: y index of location
        """
        p =  int(np.floor(a / self.dx ))
        q =  int(np.floor(b / self.dy ))
        #print(p,q) 
    
        return(p,q)
    
   
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
