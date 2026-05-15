# Two-Spin Transverse-Field Ising Hamiltonian

## Topic

Condensed Matter Physics / Quantum Dynamics

## Difficulty

Undergraduate / Early Graduate

## Problem Statement

Consider a two-spin transverse-field Ising Hamiltonian given by

$$
H = J Z_1 Z_2 + h(X_1 + X_2),
$$

where $X_i$ and $Z_i$ are Pauli operators acting on spin $i$, $J$ is the Ising coupling strength, and $h$ is the transverse-field strength.

1. Explain the physical meaning of each term in the Hamiltonian.
2. Write the matrix representation of $Z_1Z_2$ in the computational basis

$$
\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}.
$$

3. Determine which computational basis states are energetically favored by the interaction term $JZ_1Z_2$ when $J < 0$ and when $J > 0$.
4. Explain qualitatively how the transverse-field term affects the dynamics of the system.

## Expected Reasoning Skills

- Understanding of Pauli operators.
- Construction of tensor-product operators.
- Interpretation of spin-spin interactions.
- Distinction between ferromagnetic and antiferromagnetic coupling.
- Qualitative understanding of transverse-field-induced dynamics.

## Target Result

The interaction operator is

$$
Z_1Z_2 =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.
$$

For $J < 0$, the energetically favored states are $|00\rangle$ and $|11\rangle$.

For $J > 0$, the energetically favored states are $|01\rangle$ and $|10\rangle$.
