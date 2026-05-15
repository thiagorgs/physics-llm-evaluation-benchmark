# Solution: Electric Field of a Uniformly Charged Spherical Shell

## Step 1: State Gauss's law

Gauss's law states that

$$
\oint \mathbf{E}\cdot d\mathbf{A}
=
\frac{Q_{\text{enc}}}{\varepsilon_0},
$$

where $Q_{\text{enc}}$ is the total charge enclosed by the Gaussian surface.

Because the charge distribution is spherically symmetric, the electric field must be radial and depend only on the distance $r$ from the center:

$$
\mathbf{E}(r) = E(r)\hat{\mathbf{r}}.
$$

## Step 2: Choose a Gaussian surface

Choose a spherical Gaussian surface of radius $r$ centered at the same point as the charged shell.

On this Gaussian surface, the electric field has constant magnitude and is parallel to the area element $d\mathbf{A}$.

Therefore,

$$
\oint \mathbf{E}\cdot d\mathbf{A}
=
E(r)\oint dA.
$$

Since the surface area of a sphere is $4\pi r^2$,

$$
\oint \mathbf{E}\cdot d\mathbf{A}
=
E(r)4\pi r^2.
$$

## Step 3: Region inside the shell, $r < R$

For a Gaussian sphere inside the shell, no charge is enclosed:

$$
Q_{\text{enc}} = 0.
$$

Using Gauss's law,

$$
E(r)4\pi r^2 = \frac{0}{\varepsilon_0}.
$$

Thus,

$$
E(r) = 0.
$$

Therefore, for $r < R$,

$$
\mathbf{E}(r) = 0.
$$

## Step 4: Region outside the shell, $r > R$

For a Gaussian sphere outside the shell, the full charge $Q$ is enclosed:

$$
Q_{\text{enc}} = Q.
$$

Using Gauss's law,

$$
E(r)4\pi r^2 = \frac{Q}{\varepsilon_0}.
$$

Solving for $E(r)$,

$$
E(r) =
\frac{Q}{4\pi\varepsilon_0 r^2}.
$$

Since the field is radial,

$$
\mathbf{E}(r) =
\frac{1}{4\pi\varepsilon_0}
\frac{Q}{r^2}
\hat{\mathbf{r}}.
$$

## Final Answer

For $r < R$,

$$
\boxed{
\mathbf{E}(r) = 0
}
$$

For $r > R$,

$$
\boxed{
\mathbf{E}(r) =
\frac{1}{4\pi\varepsilon_0}
\frac{Q}{r^2}
\hat{\mathbf{r}}
}
$$

## Common Mistakes

- Assuming the field inside the shell is the same as the field outside.
- Forgetting that the enclosed charge is zero for $r < R$.
- Choosing a Gaussian surface that does not respect the symmetry.
- Treating the shell as if the charge were uniformly distributed throughout a solid sphere.
- Forgetting the radial direction $\hat{\mathbf{r}}$ in the vector expression.

## Physical Interpretation

Outside the spherical shell, the electric field is the same as if all the charge were concentrated at the center of the shell.

Inside the shell, the electric field vanishes because a Gaussian surface with $r < R$ encloses no net charge, and spherical symmetry ensures that the field cannot have a preferred direction.
