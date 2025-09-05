# Basis potentials

## $\alpha_n$ potentials

The additive basis functions $a_n=1-\exp(-inz)$ have potentials $\alpha_n=\int_0^na_ndz$, which are pretty easy to evaluate:

$$\alpha_n=z-\frac in[\exp(-inz)]_0^z=z+\frac in[1-\exp(-inz)]=z+\frac ina_n,n>0$$

We leave the evaluation of $\alpha_0$ from $a_0=\sqrt{1-\exp(-iz)}$, since it is also part of the $m_n$ basis, and is more easily evaluated in that context.

## $\mu_n$ potentials

The $m_n=\exp(-inz)\sqrt{1-\exp(-iz)}$ are more difficult, but not impossible. Defining $\xi=\sqrt{1-\exp(-iz)}$, we have $m_n=(1-\xi^2)^n\xi$. The transformation also gives the 1-form/line-integral transformation $2\xi d\xi=d(1-\exp(-iz))=i\exp(-iz)dz$ or $dz=-2i\xi d\xi/(1-\xi^2)$, thus:

$$\mu_n=\int_0^zm_ndz=-\int_0^\xi\frac{2i(1-\xi^2)^n\xi^2}{1-\xi^2}d\xi=-\int_0^\xi2i(1-\xi^2)^{n-1}\xi^2d\xi$$

Again, the only ticklish term is $n=0$. Delaying that for now, the binomial theorem and standard power integration gives:

$$\mu_n=-2i\int_0^\xi\sum_k\binom{n-1}{k-1}\xi^{2k}d\xi=-2i\sum_k\binom{n-1}{k}\frac{\xi^{2k+1}}{2k+1}$$

The sum is zero outside $[1,2,\dots,n]$.

## The hard bit

We now tackle:

$$\alpha_0=\mu_0=-2i\int_0^\xi\frac{\xi^2}{1-\xi^2}d\xi$$

First we reduce the integrand:

$$\frac{\xi^2}{1-\xi^2}=1-\frac1{1-\xi^2}$$

Then express the faction as linear parts:

$$\frac1{1-\xi^2}=\frac12\left[\frac1{1-\xi}+\frac1{1+\xi}\right]$$

Thus:

$$\alpha_0=\mu_0=-2i\left[\xi+\frac12\log\frac{1-\xi}{1+\xi}\right]$$