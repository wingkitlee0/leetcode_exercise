import numpy as np

"""
Author:
    Kit Lee (wklee4993@gmail.com)
Licensing:
    This code is distributed under the GNU LGPL license. 

Based on the example written by Mike Sussman.
"""

# tolerance of residual relative to f
TOL_RES = 1e-12

def vcycle ( A, f ):

#*****************************************************************************80
#
## VCYCLE performs one v-cycle on the matrix A.
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
#  Parameters:
#
#    Input, A(*,*), the matrix.
#
#    Input, f(*), the right hand side.
#
#    Output, v(*), the solution of A*v=f.
#
  
  import scipy.linalg as la

  sizeF = np.size ( A, axis = 0 )
#
#  directSize=size for direct inversion
#
  if sizeF < 15:
    v = la.solve(A,f)
    return v
#
#  N1=number of Gauss-Seidel iterations before coarsening
#
  N1 = 5;
  v = np.zeros(sizeF);
  for numGS in range(N1):
    for k in range(sizeF):
      v[k] = (f[k] - np.dot(A[k,0:k], v[0:k]) \
                   -np.dot(A[k,k+1:], v[k+1:]) ) / A[k,k];
# 
#  construct interpolation operator from next coarser to this mesh
#  next coarser has ((n-1)/2 + 1 ) points
#
#  assert ( sizeF%2 == 1 )
#  sizeC =  ( sizeF - 1 ) // 2 + 1
#  P = np.zeros((sizeF,sizeC));
#
#  Copy these points.
#
#  for k in range(sizeC):
#    P[2*k,k] = 1;
#
#  Average these points:
#
#  for k in range(sizeC-1):
#    P[2*k+1,k] = .5;
#    P[2*k+1,k+1] = .5;
  assert ( sizeF%2 == 0 )
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

#
#  compute residual
#
  residual = f - np.dot(A,v)
#
#  project residual onto coarser mesh
#
  #residC = np.dot(P.transpose(),residual)
  residC = np.dot(RR,residual)
#
#  Find coarser matrix  (sizeC X sizeC)
#
  #AC = np.dot(P.transpose(),np.dot(A,P))
  AC = np.dot(RR,np.dot(A,P))

  vC = vcycle(AC,residC);
#
# extend to this mesh
#
  v = np.dot(P,vC)
#
#  N2=number of Gauss-Seidel iterations after coarsening
#
  N2 = 5;
  for numGS in range(N2):
    for k in range(sizeF):
      v[k] = (f[k] - np.dot(A[k,0:k], v[0:k]) \
                   - np.dot(A[k,k+1:], v[k+1:]) ) / A[k,k];
  return v

def vcycle_test ( ):

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

  N = 2**5
  x = np.linspace(0,1,N);
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

  A = A / h**2
#
#  The right hand side is a vector of 1's.
#
#  f = np.ones ( N, dtype = float )
  f = np.sin(x)
#
#  UDIRECT is the exact solution, from Gauss elimination.
#
  udirect = la.solve ( A, f )

  u = np.zeros(N) # initial guess

  for iters in range ( 100 ):
    r = f - np.dot(A,u)
    if la.norm(r)/la.norm(f) < TOL_RES:
      print('\nVCYLE_TEST: Tolerance achieved.')
      break
    du = vcycle(A, r)
    u += du

    print('step {:5d}, rel error={:10.3e}'.format(iters, 
        la.norm(u-udirect)/la.norm(udirect) ) )

  
#
#  Terminate.
#
  print('norm(r) = ', la.norm(r))
  print ( '' )
  print ( 'VCYCLE_TEST:' )
  print ( '  Normal end of execution.' )


if ( __name__ == '__main__' ):
  vcycle_test ( )
