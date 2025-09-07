# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Module using multiplicative basis
#
# The square root singularity requires $\sum C_n=\pm1$ when we do the linear problem of finding coefficients that give $P=0$, We can thus replace the zero row by 1, $A_{0n}=1$, to enforce this, via $\sum_nA_{0n}C_n=\pm1=B_0$.
#
# The rest of the matrix problem is then $AC=B$ with $A_{kn}=Q_{kn}=\psi_n(z_k)=\Im\chi_n(z_k),B_k=0$ for $k>1$.

# %%
import numpy as np

from scipy.special import comb

def w_n(z,N):
    '''Evaluate w_n=exp(-inz)*sqrt(1-exp(-iz)) for n in range(N)'''
    z=np.array([z])
    ez=np.exp(-1j*z)
    xi=np.sqrt(1-ez)
    ezN=np.power.outer(ez,np.arange(N))
    return (xi.reshape(*xi.shape,1)*ezN)[0]

def chi_0(Z):
    z=np.array([Z])
    ez=np.exp(-1j*z)
    xi=np.sqrt(1-ez)
    return 2j*(xi+np.log((1-xi)/(1+xi))/2)[0]

def chi_n(Z,N):
    '''Evaluate chi_n from z=0 (see Fuchs.md)'''
    z=np.array([Z])
    ez=np.exp(-1j*z)
    xi=np.sqrt(1-ez)
    K=np.arange(3,2*N,2)
    xiK=np.power.outer(xi,K)@np.diag((-1)**np.arange(len(K))/K)
    C=np.array([[comb(a,b) for a in range(N-1)] for b in range(N-1)])
    return np.insert(-2j*xiK@C,0,chi_0(z),axis=-1)[0]

def C_n(Z):
    CHI=chi_n(Z[1:],len(Z))
    a=np.array([np.ones(len(Z)),*CHI.imag])
    b=np.zeros(len(Z))
    b[0]=1
    return np.linalg.solve(a,b)

wchiC=(w_n,chi_n,C_n)
