# Solution: Two-Spin Transverse-Field Ising Hamiltonian

## Step 1: Interpret the Hamiltonian

The Hamiltonian is

$$
H = J Z_1 Z_2 + h(X_1 + X_2).
$$

It contains two types of terms:

- $JZ_1Z_2$: an Ising interaction between the two spins.
- $h(X_1 + X_2)$: a transverse field acting independently on each spin.

The Ising term favors different spin configurations depending on the sign of $J$. The transverse-field term does not commute with the $Z$ basis and therefore can induce transitions between computational basis states.

## Step 2: Recall the Pauli matrices

The relevant Pauli matrices are

$$
Z =
\begin{pmatrix}
1 & 0 \\
0 & -1
\end{pmatrix}
$$

and

$$
X =
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}.
$$

The operator $Z_1Z_2$ means

$$
Z_1Z_2 = Z \otimes Z.
$$

## Step 3: Build $Z_1Z_2$ in the computational basis

The computational basis is

$$
\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}.
$$

Using the eigenvalue convention

$$
Z|0\rangle = +|0\rangle
$$

and

$$
Z|1\rangle = -|1\rangle,
$$

we compute:

$$
Z_1Z_2|00\rangle = (+1)(+1)|00\rangle = +|00\rangle,
$$

$$
Z_1Z_2|01\rangle = (+1)(-1)|01\rangle = -|01\rangle,
$$

$$
Z_1Z_2|10\rangle = (-1)(+1)|10\rangle = -|10\rangle,
$$

and

$$
Z_1Z_2|11\rangle = (-1)(-1)|11\rangle = +|11\rangle.
$$

Therefore, in the computational basis,

$$
Z_1Z_2 =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.
$$

## Step 4: Energies from the interaction term

The interaction contribution to the energy is

$$
E_{\text{int}} = J \lambda,
$$

where $\lambda$ is the eigenvalue of $Z_1Z_2$.

For the states $|00\rangle$ and $|11\rangle$,

$$
\lambda = +1,
$$

so

$$
E_{\text{int}} = J.
$$

For the states $|01\rangle$ and $|10\rangle$,

$$
\lambda = -1,
$$

so

$$
E_{\text{int}} = -J.
$$

## Step 5: Case $J < 0$

If $J < 0$, then

$$
J < -J.
$$

Therefore, the lower-energy states are those with

$$
\lambda = +1.
$$

Thus, for $J < 0$, the interaction favors

$$
|00\rangle
$$

and

$$
|11\rangle.
$$

These are aligned spin configurations. This corresponds to a ferromagnetic interaction.

## Step 6: Case $J > 0$

If $J > 0$, then

$$
-J < J.
$$

Therefore, the lower-energy states are those with

$$
\lambda = -1.
$$

Thus, for $J > 0$, the interaction favors

$$
|01\rangle
$$

and

$$
|10\rangle.
$$

These are anti-aligned spin configurations. This corresponds to an antiferromagnetic interaction.

## Step 7: Effect of the transverse field

The transverse-field term is

$$
h(X_1 + X_2).
$$

The operator $X$ flips a spin:

$$
X|0\rangle = |1\rangle
$$

and

$$
X|1\rangle = |0\rangle.
$$

Therefore, $X_1$ flips the first spin and $X_2$ flips the second spin.

For example,

$$
X_1|00\rangle = |10\rangle
$$

and

$$
X_2|00\rangle = |01\rangle.
$$

This means the transverse field couples different computational basis states and generates nontrivial quantum dynamics.

## Final Answer

The interaction matrix is

$$
\boxed{
Z_1Z_2 =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
}
$$

For $J < 0$, the interaction favors

$$
\boxed{|00\rangle \text{ and } |11\rangle}
$$

which are aligned configurations.

For $J > 0$, the interaction favors

$$
\boxed{|01\rangle \text{ and } |10\rangle}
$$

which are anti-aligned configurations.

The transverse-field term $h(X_1 + X_2)$ flips spins and couples different computational basis states, producing quantum dynamics beyond the classical Ising interaction.

## Common Mistakes

- Confusing the sign convention for ferromagnetic and antiferromagnetic coupling.
- Forgetting that $Z_1Z_2 = Z \otimes Z$.
- Assuming the transverse-field term is diagonal in the computational basis.
- Forgetting that $X$ flips computational basis states.
- Treating $JZ_1Z_2$ and $h(X_1 + X_2)$ as if they always commute.

## Physical Interpretation

The $JZ_1Z_2$ term behaves like a classical Ising interaction in the computational basis. It assigns different energies to aligned and anti-aligned spin configurations.

The transverse-field term introduces genuinely quantum behavior because it flips spins and mixes computational basis states. This competition between interaction and transverse field is the basic mechanism behind the transverse-field Ising model, which is widely used in quantum magnetism, quantum phase transitions, and quantum simulation.
