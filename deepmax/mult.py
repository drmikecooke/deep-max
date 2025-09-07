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
# The multiplicative velocity basis is
#
# $$m_n=\exp(-inz)\sqrt{1-\exp(-iz)}$$
#
# The potential basis is:
#
# $$\mu_n=-2i\sum_k(-1)^k\binom{n-1}{k}\frac{\xi^{2k+3}}{2k+3}$$
#
# The square root singularity requires $\sum C_n=\pm1$ when we do the linear problem of finding coefficients that give $P=0$, We can thus replace the zero row by 1, $A_{0n}=1$, to enforce this, via $\sum_nA_{0n}C_n=\pm1=B_0$.
#
# The rest of the matrix problem is then $AC=B$ with $A_{kn}=Q_{kn}=\psi_n(z_k)=\Im\chi_n(z_k),B_k=0$ for $k>1$.

# %%
import numpy as np

from scipy.special import comb

def m_n(z,N):
    '''Evaluate m_n=exp(-inz)*sqrt(1-exp(-iz)) for n in range(N)'''
    z=np.array([z])
    ez=np.exp(-1j*z)
    xi=np.sqrt(1-ez)
    ezN=np.power.outer(ez,np.arange(N))
    return (xi.reshape(*xi.shape,1)*ezN)[0]

def C_n(Z):
    CHI=mu_n(Z[1:],len(Z))
    a=np.array([np.ones(len(Z)),*CHI.imag])
    b=np.zeros(len(Z))
    b[0]=1
    return np.linalg.solve(a,b)


# %%
def M_kn(k,n):
    return -2j*(-1)**k*comb(n-1,k)/(2*k+3)


# %%
def mu_n(Z,N):
    z=np.array([Z])
    ez=np.exp(-1j*z)
    xi=np.sqrt(1-ez)
    K=np.arange(3,2*(N+1),2)
    xiK=np.power.outer(xi,K)
    MU=(xiK@np.fromfunction(M_kn,(N,N)))
    MU[...,0]=2j*(xi+np.log((1-xi)/(1+xi))/2)
    return MU[0]

wchiC=(m_n,mu_n,C_n)
