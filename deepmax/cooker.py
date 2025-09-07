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
# # Cooker for finding optimum components for maximum-height wave

# %%
import numpy as np
from scipy.optimize import root

chi_n,w_n,C_n=None,None,None

def set_n(W,CHI,C_N):
    global w_n,chi_n,C_n
    w_n,chi_n,C_n=W,CHI,C_N


# %% [markdown]
# We assume the lists of complex velocity components, and corresponding complex potentials, are given by $\{w_n(Z)|n\in N\}$ and $\{\chi_n(Z)|n\in N\}$, respectively.

# %%
def chi(Z,C):
    '''Complex potential with coefficients {C_n}:
    the chi_n need to be defined (in module?)'''
    return chi_n(Z,len(C))@C

def P(Z,C):
    '''Stream function, psi=chi.imag'''
    return chi(Z,C).imag

def w(Z,C):
    '''Complex velocity with coefficients {C_n}:
    the w_n need to be defined (in module?)'''
    return w_n(Z,len(C))@C

def R(Z,C):
    '''Evaluate Bernoulli function (sans pressure) as |w|^2/2+y (with z=x+iy).'''
    z=np.array(Z)
    watz=w(Z,C)
    return abs(watz)**2/2+z.imag


# %% [markdown]
# Uneven x-grid of form
#
# $$x_k=\pi(k/N)^\alpha$$
#
# This biases the evaluation points towards 0 (1) for $\alpha>1$ ($\alpha>1$). Experiment suggests $\alpha\approx1.35$ gives better results than $\alpha=1$, an evenly spaced grid.

# %%
def X_N(N,alpha=1.35):
    return np.pi*np.linspace(0,1,N)**alpha


# %% [markdown]
# Given a suggested wave profile, $z_k$, we can fix:
#
# $$P=\psi(z_k)=\sum_n\psi_n(z_k)C_n=QC=0$$
#
# if we ensure enough evaluation points to give a square matrix $Q_{kn}=\psi_n(z_k)$. However, $\psi_n(0)=0$, so we have to exclude this point,$x_0$ or $Q$ would be singular.
#
# There is another factor to remember, the square root singularity imposes an extra constraint on the coefficients that can replace the zero row. However, this constraint depends on the form of $w_n$ as $z\rightarrow0$.

# %%
def FR(Y,X):
    Z=X+1j*np.array([0,*Y])
    return R(Z,C_n(Z))[1:]


# %%
def cooker(Y0,X):
    sol=root(FR,Y0[1:],args=(X,))
    if not sol.success:
        print(sol)
        raise Exception('See above')
    return sol.x


# %%
def Z_N(Y,N,alpha):
    X=X_N(N,alpha)
    return X+1j*Y(X)

def fR(Y,X):
    Z=X+1j*Y
    return R(Z,C_n(Z))

def Zcooker(Z0):
    X,Y0=Z0.real,Z0.imag
    sol=root(fR,Y0,args=(X,))
    if not sol.success:
        print(sol)
        raise Exception('See above')
    return X+1j*sol.x
