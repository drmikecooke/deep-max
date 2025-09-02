# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
def contours(G,F,L,C=None):
    '''Contours of values F on grid G
    L=levels,T=title,C=colors'''
    cp = plt.contour(*G, F,levels=L,colors=C)
    plt.clabel(cp, fontsize=10)
    return cp

# %%
def grid(a,b,N=200):
    Nj=N*1j
    return np.mgrid[b.real:a.real:Nj,b.imag:a.imag:Nj]
