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

def vcycle( A, f , N1=5, N2=5):
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
    sizeF = A.shape[0]
    assert ( sizeF%2 == 0 )
#
#  directSize=size for direct inversion
#
    if sizeF < N_MIN:
        v = la.solve(A,f)
        return v

#  Gauss-Seidel iterations before coarsening
    v = np.zeros(sizeF)
    for numGS in range(N1):
        for k in range(sizeF):
            v[k] = (f[k] - np.dot(A[k,0:k], v[0:k]) \
                -np.dot(A[k,k+1:], v[k+1:]) ) / A[k,k]

    sizeC = sizeF // 2
    P = np.zeros((sizeF, sizeC))
    P[0,0] = 0.5
    for i in range(sizeC-1):
        P[1+2*i, i+0] = 0.75
        P[1+2*i, i+1] = 0.25
        P[2+2*i, i+0] = 0.25
        P[2+2*i, i+1] = 0.75
    P[-1,-1] = 0.5

    RR = np.zeros((sizeC, sizeF))
    for i in range(sizeC):
        RR[i,2*i+0] = 0.5
        RR[i,2*i+1] = 0.5

    #  compute residual
    residual = f - np.dot(A,v)

    #  project residual onto coarser mesh
    residC = np.dot(RR,residual)

    #  Find coarser matrix  (sizeC X sizeC)
    AC = np.dot(RR,np.dot(A,P))
    vC = vcycle(AC,residC)

    # extend to this mesh
    v = np.dot(P,vC)

    #  Gauss-Seidel iterations after coarsening
    for numGS in range(N2):
        for k in range(sizeF):
            v[k] = (f[k] - np.dot(A[k,0:k], v[0:k]) \
                - np.dot(A[k,k+1:], v[k+1:]) ) / A[k,k]
    return v

def vcycle_test(N):

#*****************************************************************************80
#
## VCYCLE_TEST tests VCYCLE.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    02 October 2016
#
#  Author:
#
#    Mike Sussman
#
  import numpy as np
  import platform
  import scipy.linalg as la

  print ( '' )
  print ( 'VCYCLE_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  VCYCLE applies one V-cycle to a matrix.' )

  #x = np.linspace(0,1,N)
  x = np.linspace(0,1,N, endpoint=False) + 0.5/N
  h = x[1]-x[0]
#
#  A is the [-1,2,-1]/h^2 tridiagonal matrix
#
  A = np.diag ( 2.0 * np.ones(N)       ) \
    - np.diag (       np.ones(N-1),  1 ) \
    - np.diag (       np.ones(N-1), -1 )

  A[ 0, :] = 0.0
  A[ 0, 0] = 3.0; A[0,1] = -1.0
  A[-1, :] = 0.0
  A[-1,-1] = 3.0; A[-1,-2] = -1.0

  A = - A / h**2

  # right hand size
  f = np.sin(x)

  # UDIRECT is the exact solution, from Gauss elimination.
  udirect = la.solve ( A, f )

  # initial guess
  u = x * (1.0-x)

  print('{:>5s}, {:>12s}, {:>12s}'.format('step', 'rel err', 'norm of res'))
  for iters in range ( 100 ):
    r = f - np.dot(A,u)
    if la.norm(r)/la.norm(f) < TOL_RES:
      print('\nVCYLE_TEST: Tolerance achieved.')
      break
    du = vcycle(A, r)
    u += du

    print('{:5d}, {:12.5e}, {:>12.5e}'.format(iters, 
        la.norm(u-udirect)/la.norm(udirect), la.norm(r) ) )

  sol_f = lambda x: -np.sin(x) + np.sin(1.0) * x
  u_sol = sol_f(x)
  error = np.sum( (u-u_sol)**2 )
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
  ax.plot(x, u_sol, 'k-')

  plt.show()


if ( __name__ == '__main__' ):
  import sys
  N = int(sys.argv[1])
  vcycle_test(N)
