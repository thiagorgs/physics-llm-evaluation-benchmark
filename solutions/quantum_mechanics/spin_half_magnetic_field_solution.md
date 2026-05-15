# Solution: Spin-1/2 Particle in a Magnetic Field

## Step 1: Identify the energy eigenstates

The Hamiltonian is

\[
H = -\gamma B S_z.
\]

Since

\[
S_z |+\rangle_z = \frac{\hbar}{2}|+\rangle_z,
\]

and

\[
S_z |-\rangle_z = -\frac{\hbar}{2}|-\rangle_z,
\]

the corresponding energies are

\[
E_+ = -\frac{\gamma B\hbar}{2},
\]

and

\[
E_- = +\frac{\gamma B\hbar}{2}.
\]

## Step 2: Apply time evolution

For a time-independent Hamiltonian, each energy eigenstate evolves as

\[
|E\rangle \rightarrow e^{-iEt/\hbar}|E\rangle.
\]

The initial state is

\[
|\psi(0)\rangle =
\frac{1}{\sqrt{2}}\left(|+\rangle_z + |-\rangle_z\right).
\]

Therefore,

\[
|\psi(t)\rangle =
\frac{1}{\sqrt{2}}
\left(
e^{-iE_+t/\hbar}|+\rangle_z
+
e^{-iE_-t/\hbar}|-\rangle_z
\right).
\]

Substituting the energies,

\[
|\psi(t)\rangle =
\frac{1}{\sqrt{2}}
\left(
e^{i\gamma Bt/2}|+\rangle_z
+
e^{-i\gamma Bt/2}|-\rangle_z
\right).
\]

## Step 3: Write \(S_x\)

The \(x\)-component of the spin operator is

\[
S_x = \frac{\hbar}{2}\sigma_x.
\]

In the \(S_z\) basis,

\[
\sigma_x =
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}.
\]

So,

\[
S_x =
\frac{\hbar}{2}
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}.
\]

## Step 4: Compute \(\langle S_x(t)\rangle\)

In the \(S_z\) basis, the state can be written as

\[
|\psi(t)\rangle =
\frac{1}{\sqrt{2}}
\begin{pmatrix}
e^{i\gamma Bt/2} \\
e^{-i\gamma Bt/2}
\end{pmatrix}.
\]

The expectation value is

\[
\langle S_x(t)\rangle =
\langle \psi(t)|S_x|\psi(t)\rangle.
\]

Using the matrix form,

\[
\langle S_x(t)\rangle =
\frac{\hbar}{2}
\frac{1}{2}
\left(
e^{-i\gamma Bt/2}e^{-i\gamma Bt/2}
+
e^{i\gamma Bt/2}e^{i\gamma Bt/2}
\right).
\]

Thus,

\[
\langle S_x(t)\rangle =
\frac{\hbar}{4}
\left(
e^{-i\gamma Bt}
+
e^{i\gamma Bt}
\right).
\]

Using

\[
e^{ix}+e^{-ix}=2\cos x,
\]

we obtain

\[
\langle S_x(t)\rangle =
\frac{\hbar}{2}\cos(\gamma Bt).
\]

## Final Answer

\[
\boxed{
\langle S_x(t)\rangle =
\frac{\hbar}{2}\cos(\gamma Bt)
}
\]

## Common Mistakes

- Forgetting that \(|+\rangle_z\) and \(|-\rangle_z\) acquire different phases.
- Using the same energy for both spin states.
- Confusing \(S_x\) and \(S_z\) eigenstates.
- Dropping the relative phase, which is responsible for the oscillation.
- Missing the factor of \(\hbar/2\) in the spin operator.

## Physical Interpretation

The initial state is an equal superposition of spin-up and spin-down states along the \(z\)-axis. Since these two components have different energies in the magnetic field, they acquire a relative phase over time.

This relative phase causes the expectation value of the spin along the \(x\)-axis to oscillate. Physically, this is the precession of the spin around the magnetic field direction, with angular frequency

\[
\omega = \gamma B.
\]
