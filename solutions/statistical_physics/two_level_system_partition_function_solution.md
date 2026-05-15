# Solution: Two-Level System and Partition Function

## Step 1: Define the canonical partition function

In the canonical ensemble, the partition function is

$$
Z = \sum_i e^{-\beta E_i},
$$

where

$$
\beta = \frac{1}{k_B T}.
$$

For this system, there are two energy levels:

$$
E_0 = 0
$$

and

$$
E_1 = \epsilon.
$$

Therefore,

$$
Z = e^{-\beta E_0} + e^{-\beta E_1}.
$$

Substituting the energies,

$$
Z = e^{0} + e^{-\beta \epsilon}.
$$

Thus,

$$
Z = 1 + e^{-\beta \epsilon}.
$$

## Step 2: Compute the average energy

The average energy in the canonical ensemble is

$$
\langle E \rangle =
\frac{1}{Z}\sum_i E_i e^{-\beta E_i}.
$$

For the two-level system,

$$
\langle E \rangle =
\frac{E_0 e^{-\beta E_0} + E_1 e^{-\beta E_1}}{Z}.
$$

Substituting $E_0 = 0$ and $E_1 = \epsilon$,

$$
\langle E \rangle =
\frac{0\cdot e^{0} + \epsilon e^{-\beta \epsilon}}{1 + e^{-\beta \epsilon}}.
$$

Therefore,

$$
\langle E \rangle =
\frac{\epsilon e^{-\beta \epsilon}}{1 + e^{-\beta \epsilon}}.
$$

## Step 3: Low-temperature limit

The low-temperature limit corresponds to

$$
T \rightarrow 0.
$$

Since

$$
\beta = \frac{1}{k_B T},
$$

we have

$$
\beta \rightarrow \infty.
$$

Therefore,

$$
e^{-\beta \epsilon} \rightarrow 0.
$$

The partition function becomes

$$
Z \rightarrow 1,
$$

and the average energy becomes

$$
\langle E \rangle \rightarrow 0.
$$

## Step 4: High-temperature limit

The high-temperature limit corresponds to

$$
T \rightarrow \infty.
$$

Then

$$
\beta \rightarrow 0,
$$

so

$$
e^{-\beta \epsilon} \rightarrow 1.
$$

The partition function becomes

$$
Z \rightarrow 2,
$$

and the average energy becomes

$$
\langle E \rangle \rightarrow \frac{\epsilon}{2}.
$$

## Final Answer

$$
\boxed{
Z = 1 + e^{-\beta \epsilon}
}
$$

and

$$
\boxed{
\langle E \rangle =
\frac{\epsilon e^{-\beta \epsilon}}{1 + e^{-\beta \epsilon}}
}
$$

with

$$
\beta = \frac{1}{k_B T}.
$$

In the low-temperature limit,

$$
\langle E \rangle \rightarrow 0.
$$

In the high-temperature limit,

$$
\langle E \rangle \rightarrow \frac{\epsilon}{2}.
$$

## Common Mistakes

- Forgetting the Boltzmann factor $e^{-\beta E_i}$.
- Writing the partition function as a simple sum of energies.
- Confusing the low-temperature and high-temperature limits.
- Forgetting that $E_0 = 0$ contributes a factor of $1$ to the partition function.
- Missing the normalization by $Z$ when computing $\langle E \rangle$.

## Physical Interpretation

At low temperature, thermal energy is not sufficient to populate the excited state. The system is almost always found in the ground state, so the average energy approaches zero.

At high temperature, both energy levels become nearly equally populated. Since the system spends approximately half of the time in each level, the average energy approaches $\epsilon/2$.
