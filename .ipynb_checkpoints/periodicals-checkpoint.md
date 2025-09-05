# Periodicals

So we have a flow form $w\approx\pm\sqrt{iz}$ that gives the sort of behaviour we expect from a maximum wave. The $\pm$ sign gives the direction of travel: if +, the water deep down is flowing in the forward direction, and thus the peak would travel in the negative direction. This flow form is not a serious contender for our problem. We expect waves, as opposed to solitons, say, to repeat themselves, at least approximately for a time. In the ideal limit, the "wave" would repeat forever with a wavelength $\lambda$. To represent repeating functions we naturally think of something like Fourier series. However, our desired waveform has a discontinuous slope, which imposes problems in terms of convergence.

First we look for a periodic function which has the desired singularity at $z=n\lambda,n\in\mathbb Z$ ($\mathbb Z$ is the set of integers). Although Fourier series can be posed in terms of trigonometric functions, in the analytic domain we prefer the exponential representation $w_k=\exp(ikz)$, where $k$ is the "wave vector". These functions have periodicity in the real direction: $w_k(z+\lambda)=w_k(z)$ if $k\lambda=2n\pi$. We have already proposed units such that $g=1$, and if we were interested in pressure $\rho=1$. We now propose to scale so that $\lambda=2\pi$, so that our basis functions are $w_n,n\in\mathbb Z$.

Another factor we need to consider is that we want these functions to be finite as $y\rightarrow-\infty$. This requires $\exp(in(x+iy))=\exp(-ny)\exp(inx)$ to be such that the $y$ exponential factor to be finite. Since we are only in $y\le0$, we need $n\le0$, so that $-ny\rightarrow-\infty$.

Now for the singular part, $w_0-w_{-1}=1-\exp(-iz)\approx iz$ as $z\rightarrow0$, so $\pm\sqrt{1-\exp(-iz)}$ has the sort of periodic behavior we want.

Our strategy will be to combine this function with basis functions ($b_n$) to improve the fit between the Bernoulli principle and surface profile, as given by the stream function $\psi$.

So we have $w=\sum_nC_nb_n$, and corresponding $\chi=\sum_nC_nc_n$, where the $c_n=\int_0^zb_ndz$. We need the $b_n\rightarrow0$ as $z\rightarrow$ at least as fast as $\sqrt{iz}$. We choose 0 as the base point for the $c_n$ so that the surface profile is given by $\psi=\Im\chi=0$. This isn't stricly necessary, but convenient.

We have implemented two approaches, "additive" and "multiplicative", which both seem to give reasonable results. Other bases might give better results, particularly if one attempts to use multiple precision for more accurate results. However, our bases manage to reach the accuracy suggested on the Wikipedia page in the references.

## Additive approach

The additive approach is to define $a_0=\sqrt{1-\exp(-iz)}$, and for $n\ne0$, $a_n=1-\exp(-inz)$. This is essentially a Fourier series added to the singular part. Deep in the water, where $|\exp(-iz)|\ll1$, the singular part can also be seen as a Fourier series based on the binomial theorem for $\frac12$ exponent.

## Multiplicative approach.

The multiplicative basis is $m_n=\exp(-inz)\sqrt{1-\exp(-iz)}$.

We now need to work out the corresponding potential basis.