
# Solution: Inclined Plane with Friction and an External Force

## Step 1: Identify the forces

The forces acting on the block are:

- The applied force $F$, directed upward along the incline.
- The gravitational force $mg$, directed vertically downward.
- The normal force $N$, perpendicular to the plane.
- The kinetic friction force $f_k$, directed opposite to the motion.

Since the block is moving upward, kinetic friction points downward along the incline.

## Step 2: Decompose the gravitational force

The component of gravity parallel to the incline is

$$
mg\sin\theta,
$$

directed downward along the plane.

The component of gravity perpendicular to the incline is

$$
mg\cos\theta.
$$

Since there is no acceleration perpendicular to the plane,

$$
N = mg\cos\theta.
$$

## Step 3: Write the kinetic friction force

The kinetic friction force is

$$
f_k = \mu_k N.
$$

Using $N = mg\cos\theta$, we obtain

$$
f_k = \mu_k mg\cos\theta.
$$

This force points downward along the incline because it opposes the upward motion.

## Step 4: Apply Newton's second law along the incline

Choose the positive direction upward along the incline.

The forces along the incline are:

- $F$, positive.
- $mg\sin\theta$, negative.
- $\mu_k mg\cos\theta$, negative.

Therefore,

$$
F_{\text{net}} = F - mg\sin\theta - \mu_k mg\cos\theta.
$$

Using Newton's second law,

$$
ma = F - mg\sin\theta - \mu_k mg\cos\theta.
$$

Dividing by $m$,

$$
a = \frac{F}{m} - g\sin\theta - \mu_k g\cos\theta.
$$

## Final Answer

$$
\boxed{
a = \frac{F}{m} - g\sin\theta - \mu_k g\cos\theta
}
$$

## Common Mistakes

- Assuming friction points upward instead of downward.
- Forgetting to decompose gravity into parallel and perpendicular components.
- Using $mg$ instead of $mg\cos\theta$ for the normal force.
- Omitting the friction term.
- Writing the applied force contribution as $F$ instead of $F/m$ in the acceleration.

## Physical Interpretation

The applied force tends to accelerate the block upward along the incline. Gravity and kinetic friction both oppose this upward motion.

If

$$
F > mg\sin\theta + \mu_k mg\cos\theta,
$$

then the acceleration is positive and the block speeds up while moving upward.

If

$$
F < mg\sin\theta + \mu_k mg\cos\theta,
$$

then the acceleration is negative and the block slows down while still moving upward.
