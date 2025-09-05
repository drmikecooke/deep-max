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
# # {code}`deepmax.add` submodule
#
# We implement the additive basis:
#
# $$a_n=1-\exp(-inz)$$
#
# and corresponding potential sequence:
#
# $$\alpha_n=z+\frac ina_n$$
#
# The singular parts are:
#
# $$a_0=\sqrt{1-\exp(-iz)}=\sqrt{a_1}$$
#
# $$\alpha_0=2i\left[a_0+\frac12\ln\frac{1-a_0}{1+a_0}\right]$$
#
# The square root singularity requires $C_0=\pm1$ when we do the linear problem of finding coefficients that give $\psi(z_k)=\sum_n\Im\alpha_n(z_k)C_n=0$. We can thus replace the zero row by 0, except for $A_{00}=1$, to enforce this, via $\sum_nA_{0n}C_n=C_0=\pm1=B_0$.
#
# The rest of the matrix problem is then $AC=B$ with $A_{kn}=\psi_n(z_k)=\Im\alpha_n(z_k),B_k=0$ for $k>0$.

# %%
import numpy as np

def a_n(z,N):
    '''Evaluate additive basis a_n for n in range(N)'''
    z=np.array([z])
    ez=np.exp(-1j*z)
    aN=1-np.power.outer(ez,np.arange(N))
    aN[...,0]=np.sqrt(aN[...,1])
    return aN[0]

def alpha_n(z,N):
    '''Evaluate alpha_n from z=0'''
    z=np.array([z])
    aN=a_n(z,N)
    alpN=aN@np.diag([1,*(1j/np.arange(1,N))])+z.reshape((*z.shape,1))
    a0=aN[...,0]
    alpN[...,0]=2j*(a0+np.log((1-a0)/(1+a0))/2)
    return alpN[0]

def C_n(Z):
    PSI=alpha_n(Z,len(Z)).imag
    PSI[0,0]=1
    b=np.zeros(len(Z))
    b[0]=1
    return np.linalg.solve(PSI,b)
