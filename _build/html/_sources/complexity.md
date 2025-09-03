# Complexity makes life simpler

We look at how our basic equations simplify in the complex domain.

In 2D, the incompressibility equation $\mathbf{\nabla} \cdot \mathbf{v}=0$ becomes $u_x+v_y=0$, where the subscript represent the corresponding partial derivative, and the $x,y$ components of $\mathbf{v}$ are $u,v$.

Irrotational motion $\mathbf{\nabla} \times \mathbf{v}=0$ is given by $v_x-u_y=0$.

## Cauchy-Riemann

These relations are reminiscent of the Cauchy-Riemann relations at the root of analytic function theory.

An _analytic function_ is a mapping of open subsets of the complex planes $z=x+iy$ and $f=g+ih$, such that $f$ can be represented as a convergent power series of $z$ in such domains.

Cauchy and Riemann studied this situation and found it was necessary and sufficient that the mapping had the form of being differentiable, and $g_x=h_y$, $g_y=-h_x$. These can be derived by considering $df/dz$ as giving the same result when $dz=dx$ and $dz=idy$:

$$g_x+ih_x=\frac1i(g_y+ih_y)$$

For our velocity relations, we can define a complex function $w=u-iv$. The minus sign is necessary to make $w$ satisfy the Cauchy-Riemann equations, according to the incompressibility and irrotational conditions above.

Differentiating the Cauchy-Riemann equations, $g_{xx}=h_{yx}=h_{xy}=-g_{yy}$, gives the 2D Laplace equation $\nabla^2g=0$, and $\nabla^2h=0$, similarly. The functions $g,h$ connected by their being part of an analytic function $f$ are called harmonic conjugates.

![cauchy](cauchy.svg)

Another aspect of analytic functions we need is Cauchy's integral theorem that contour integrals in simply connected domains $\oint fdz=0$. This means that in such domains we can define potential functions $\int_{z_0}^zfdz$ that are independent of the path from the base point $z_0$:

>Going "up" along one path and back along the other gives a closed contour, which integral is zero, according to Cauchy's integral theorem. But this closed contour can also be viewed as giving the difference in value between the two paths integrals, so they give the same value!

This all works so long as the function is analytic on the domain. More interesting effects arise where there are singularities either within or near the relevant domain. Such singularities include poles, logarithms, and algebraic roots. We will see how some of these features affect the maximum wave that we are interested in here.