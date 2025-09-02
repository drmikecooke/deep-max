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
# # Basis of singular velocity with added Fourier sequence

# %% [markdown]
# We need to adjust the Fourier velocity sequence to be zero at $z=0$, to maintain this property for the maximum wave:
#
# $$w_n=1-\exp(-inz)$$
#
# The corresponding potential sequence is:
#
# $$\chi_n=\int_0^zw_ndz=\frac in(1-\exp(-inz)+z=\frac inw_n+z$$
#
# The singular parts are:
#
# $$w_0=\sqrt{1-\exp(-iz)}$$
#
# $$\chi_0=2i\left[w_0+\frac12\ln\frac{1-w_0}{1+w_0}\right]$$
#
# The square root singularity requires $\sum C_0=\pm1$ when we do the linear problem of finding coefficients that give $P=0$. We can thus replace the zero row by 0, except for $A_{00}=1$, to enforce this, via $\sum_nA_{0n}C_n=C_0=\pm1=B_0$.
#
# The rest of the matrix problem is then $AC=B$ with $A_{kn}=Q_{kn}=\psi_n(z_k)=\Im\chi_n(z_k),B_k=0$ for $k>1$.

# %%
import numpy as np

from scipy.special import comb

def w_n(z,N):
    '''Evaluate w_n=exp(-inz)*sqrt(1-exp(-iz)) for n in range(N)'''
    z=np.array([z])
    ez=np.exp(-1j*z)
    wN=1-np.power.outer(ez,np.arange(N))
    wN[...,0]=-np.sqrt(wN[...,1])
    return wN[0]

def chi_0(Z):
    z=np.array([Z])
    ez=np.exp(-1j*z)
    xi=np.sqrt(1-ez)
    return 2j*(xi+np.log((1-xi)/(1+xi))/2)[0]

def chi_n(Z,N):
    '''Evaluate chi_n from z=0 (see Fuchs.md)'''
    Z=np.array([Z])
    wN=w_n(Z,N)
    chiN=wN@np.diag([1,*(1j/np.arange(1,N))])+Z.reshape((*Z.shape,1))
    w0=wN[...,0]
    chiN[...,0]=2j*(w0+np.log((1-w0)/(1+w0))/2)
    return chiN[0]

def C_n(Z):
    CHI=chi_n(Z[1:],len(Z))
    zerorow=np.zeros(len(Z))
    zerorow[0]=1
    a=np.array([zerorow,*CHI.imag])
    b=np.zeros(len(Z))
    b[0]=1
    return np.linalg.solve(a,b)
