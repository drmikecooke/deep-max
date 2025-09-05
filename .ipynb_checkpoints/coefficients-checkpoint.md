# Coefficient collocation

In collocation treatments I have seen, the $C_n$ have been independent variables, along with a surface profile $\{z_k\}$. However, note that:

$$\psi(z_k)=\sum_nC_n\psi_n(z_k)=\sum_nA_{kn}C_n=AC=0$$

in what I hope is an obvious matrix notation. The $C_n$ are real, since this is needed for $w=\sum_nC_nw_n$ to be real for imaginary $z=iy$, where the $y$-component of the velocity should be zero.

We note that $\psi(0)=0$ has been built into our bases.

For this to be a well-defined problem linking the $z_k$ and the $C_n$, we need to break the homogeneity. This is done differently in the additive and multiplicative versions.

## Additivity

Here we separate out the singular term $\alpha_0$ from the others to give:

$$\psi(z_k)=C_0\alpha_0(z_k)+\sum_{n=1}C_n\alpha_n(z_k)=C_0B_k+\sum_nA_{kn}C_n=C_0B+AC=0$$

But $C_0=\pm1$ according to ones directive taste. Given $N$ $\{z_k\}$, one can evaluate $N$ non-zero $C_n$ by solving $AC=-C_0B$.

The wave speed is given by $w=\sum_nC_na_n$ as $y\rightarrow-\infty$. We note the exponentials in the velocity basis $a_n$ go to zero, so $a_n\rightarrow1$, choosing the postive root for $a_0$, and projecting the sign to $C_0=\pm1$. Therefore the wave speed is $c:=|\sum_nC_n|$.

## Multiplicativity

Here all the terms are singular $m_n=\exp(-inz)\sqrt{1-\exp(-iz)}$, choosing the positive root, projecting the sign onto the $C_n$ vector.

As $z\rightarrow0$, the $m_n\rightarrow\sqrt{iz}$, so we need an extra condition $\sum_nC_n=\pm1$. We can attach this as an extra row to $A$, i.e. $A_{0n}=1$, giving the matrix problem $AC=B$ with $B_0=\pm1$ and $B_k=0$ otherwise.

Again we consider the deep water flow, but this time $m_n\rightarrow0,n\ne0$. Therefore we have $c:=|C_0|$.