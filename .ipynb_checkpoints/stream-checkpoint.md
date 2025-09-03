# Potential for streaming

We have seen that incompressible, irrotational flows in 2D can be expressed as analytic functions $w=u-iv$ of $z=x+iy$. We now define a complex potential $\chi=\int_{z_0}^zwdz$. Thus $w=d\chi/dz$. Different base points $z_0$ change the value $\chi(z)$ by a constant (possibly a complex number). This is similar to gauge invariance in electromagnetic and Yang-Mills theory.

Separating $\chi=\phi+i\psi$, we find $u=\phi_x=\psi_y$ and $v=\phi_y=-\psi_x$. Returning to vector notation $\mathbf v=\mathbf\nabla\phi$, so $\phi$ is a potential function for the flow.

The $\psi$ function is a little more difficult to interpret. One could see it as a remnant of the curl of the $z$-component of a 3D vector function where the other components are zero everywhere. Let us instead view $\psi$ as a 0-form, and look at the change in $\psi$ along $\mathbf v$: $d\psi(\mathbf v)=u\psi_x+v\psi_y=-uv+uv=0$. The flow is parallel to the constant $\psi$ contours. This is a very useful property for finding free surfaces and other boundaries. The function  $\psi$ is generally called the stream function.

A further observation is that the potential and stream functions separately satisfy the Laplace equation. This can either be traced to the incompressibility and irrotationality, or more generally to the Cauchy-Riemann equations, as seen previously.