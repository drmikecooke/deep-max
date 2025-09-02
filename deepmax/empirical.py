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
# # Some empirical data and approximations
#
# $$Ye(X):=\frac{2\pi}{\sqrt3\sinh(1/2)}(\cosh((1-X/\pi)/2)-\cosh(1/2))$$
#
# was [apparently given by Fenton](https://en.wikipedia.org/wiki/Stokes_wave#Highest_wave) as a good approximation to the maximum waveform (suitably shifted to give the peak at $x=0$.

# %%
import numpy as np

def Ye(X):
    return -(np.cosh(1/2)-np.cosh((1-X/np.pi)/2))*2*np.pi/np.sqrt(3)/np.sinh(1/2)


# %% [markdown]
# We also have empirically/numerically derived value for the maximum wave height:
#
# $$\frac{H}{\lambda}=0.1410633\pm4\times10^{-7}$$

# %%
H_L=0.1410633
L=2*np.pi
H=L*H_L
