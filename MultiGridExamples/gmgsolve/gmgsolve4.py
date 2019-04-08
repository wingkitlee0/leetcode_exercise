import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

"""
Author:
    Kit Lee (wklee4993@gmail.com)
Licensing:
    This code is distributed under the GNU LGPL license. 

Note:
    - Based on the multigrid example written by Mike Sussman.
    - Modified for cell-centered grid
"""

# tolerance of residual relative to f
TOL_RES = 1e-12
# minimum size for direct solve
N_MIN = 16
# maximum iterations of V-cycle
MAX_ITER = 100

class Grid:
    """
    Create a cell-centered grid
    """
    def __init__(self, N, xmin=0.0, xmax=1.0):
        self.N = N
        self.xmin = xmin
        self.xmax = xmax

        assert(N % 2 == 0)
        self.NC = self.N // 2

    def set_RR(self, N):
        assert(N % 2 == 0)

        RR = np.zeros((N//2, N))
        for i in range(N//2):
            RR[i,2*i+0] = 0.5
            RR[i,2*i+1] = 0.5
        return RR

    def set_II(self, N, gL=-1.0, gR=-1.0):
        """
        Matrix for interpolation. 
        Args:
            gL : coefficients of u_-1 (u_-1= gL * u_0). default zero BC
            gR : coefficients of u_-1 (u_N = gR * u_N-1)
        """
        assert(N % 2 == 0)

        II = np.zeros((N, N//2))
        II[0,0] = 0.75 + 0.25 * gL
        for i in range(N//2-1):
            II[1+2*i, i+0] = 0.75
            II[1+2*i, i+1] = 0.25
            II[2+2*i, i+0] = 0.25
            II[2+2*i, i+1] = 0.75
        II[-1,-1] = 0.75 + 0.25 * gR
        return II
      

class LinearSystem(Grid):
    def __init__(self, N, xmin=0.0, xmax=1.0, lbc=0, rbc=0):
        Grid.__init__(self, N, xmin, xmax)
        self.x = np.linspace(self.xmin,self.xmax, N, endpoint=False) + 0.5*(self.xmax-self.xmin)/self.N
        self.h = self.x[1]-self.x[0]
        self.h2 = self.h**2
        self.lbc = lbc
        self.rbc = rbc

        self.gL = -1.0; self.gR = -1.0; 
        if self.lbc == 0:
            self.gL = -1.0
        elif self.lbc == 1:
            self.gL = 1.0

        if self.rbc == 0:
            self.gR = -1.0
        elif self.rbc == 1:
            self.gR = 1.0

        self.A = self.set_AA(gL=self.gL, gR=self.gR)
        self.A += np.diag( self.x)

    def set_AA(self, gL=-1.0, gR=-1.0):
        """
        A is the [-1,2,-1]/h^2 tridiagonal matrix
        """
        N = self.N
        A = np.diag ( 2.0 * np.ones(N)       ) \
            - np.diag (       np.ones(N-1),  1 ) \
            - np.diag (       np.ones(N-1), -1 )

        A[ 0, 0] = A[ 0, 0] - gL 
        A[-1,-1] = A[-1,-1] - gR

        A = - A / self.h2
        return A

def vcycle( A, f , N1=5, N2=5, gL=-1.0, gR=-1.0):
    """
    Single V-cycle

    Licensing:
        This code is distributed under the GNU LGPL license. 
    Author:
        Mike Sussman
    Args:
        A, f: matrix and rhs
    Output:
        v : solution of A*v=f
    """
    NF = A.shape[0]
    assert ( NF%2 == 0 )
#
#  directSize=size for direct inversion
#
    if NF < N_MIN:
        v = la.solve(A,f)
        return v

#  Gauss-Seidel iterations before coarsening
    v = np.zeros(NF)
    for numGS in range(N1):
        for k in range(NF):
            v[k] = (f[k] - np.dot(A[k,0:k], v[0:k]) \
                -np.dot(A[k,k+1:], v[k+1:]) ) / A[k,k]

    grid = Grid(NF)
    II = grid.set_II(NF, gL=gL, gR=gR)
    RR = grid.set_RR(NF)

    #  compute residual
    residual = f - np.dot(A,v)

    #  project residual onto coarser mesh
    residC = np.dot(RR,residual)

    #  Find coarser matrix  (sizeC X sizeC)
    AC = np.dot(RR,np.dot(A,II))
    vC = vcycle(AC,residC)

    # extend to this mesh
    v = np.dot(II,vC)

    #  Gauss-Seidel iterations after coarsening
    for numGS in range(N2):
        for k in range(NF):
            v[k] = (f[k] - np.dot(A[k,0:k], v[0:k]) \
                - np.dot(A[k,k+1:], v[k+1:]) ) / A[k,k]
    return v

def vcycle_driver(N,lbc=0, rbc=0):
    print ( 'VCYCLE_TEST:' )

    linearsystem = LinearSystem(N, xmin=0.0, xmax=1.0, lbc=lbc, rbc=rbc)
    x = linearsystem.x
    A = linearsystem.A
    gL= linearsystem.gL
    gR= linearsystem.gR

    kx = 10.0
    # right hand size
    f = np.sin(kx*x)
    # analytical solution
    #sol_f = lambda x: -np.sin(kx*x)/kx**2 + np.sin(kx)/kx**2 * x
    sol_f = lambda x: -np.sin(kx*x)/kx**2 + np.cos(kx)/kx * x

    # UDIRECT is the exact solution, from Gauss elimination.
    udirect = la.solve ( A, f )

    # initial guess
    u = x * (1.0-x)

    print('{:>5s}, {:>12s}, {:>12s}'.format('step', 'rel err', 'norm of res'))
    for iters in range(MAX_ITER):
        r = f - np.dot(A,u)
        if la.norm(r)/la.norm(f) < TOL_RES:
            print('\nVCYLE_TEST: Tolerance achieved.')
            break
        du = vcycle(A, r, gL=gL, gR=gR)
        u += du

        print('{:5d}, {:12.5e}, {:>12.5e}'.format(iters, 
        la.norm(u-udirect)/la.norm(udirect), la.norm(r) ) )


    u_sol = sol_f(x)
    error = np.sum( (udirect-u_sol)**2 )
    #
    #  Terminate.
    #
    print('norm(r) = ', la.norm(r))
    print('error (compared to the analytical solution) = {:10.5e}'.format(error))
    print ( '' )
    print ( 'VCYCLE_TEST:' )
    print ( '  Normal end of execution.' )

    fig, ax = plt.subplots()
    ax.plot(x, u, 'o', markersize=5)
    ax.plot(x, udirect, '+', markersize=5)
    #ax.plot(x, u_sol, 'k-')

    plt.show()


if ( __name__ == '__main__' ):
  import sys
  N = int(sys.argv[1])
  vcycle_driver(N, lbc=1, rbc=1)
