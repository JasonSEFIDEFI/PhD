# Two-body spectral continuation and pair-correlation transport

Status: exact branch identities; conditional cycle interpretation; reproducible static endpoint calculations. This continues the stopping point recovered from the author's conversation. Use hbar=2m_atom=1, N=2, total momentum zero, circumference L. Restore physical energy by multiplying by hbar²/(2m_atom).

## Derive the branch map before assigning physical dynamics

The bosonic relative wavefunction is proportional to cos[q(r−L/2)] on 0≤r≤L. The contact boundary condition gives

$$c=2q\tan(qL/2),\qquad E=2q^2.$$

For repulsion, label the branch by integer m≥0:

$$2m\pi<qL<(2m+1)\pi,\qquad qL+2\arctan(2q/c)=(2m+1)\pi.$$

Its ordered Bethe numbers are (−m−1/2,m+1/2). The m=0 branch starts at q=0 in the c→0+ limit. Differentiating the boundary equation gives

$$\frac{dc}{dq}=2\tan(qL/2)+qL\sec^2(qL/2),\quad
q'=\frac{4q}{L(c^2+4q^2)+4c}.$$

On the negative-c real-root gas branch, retain the odd-pi logarithmic label and take

$$ (2m+1)\pi<qL<(2m+2)\pi.$$

There tan is negative. Multiplying dc/dq by cos²(qL/2) gives sin(qL)+qL>0 on this interval, so the gas branch is monotone and the derivative is nonsingular. The attractive bound state q=i kappa is a separate sector, deliberately excluded, not shown to be unpopulated by this calculation.

The exact endpoint limits of these branches are

$$q(0^+,m)=2m\pi/L,\quad q(+\infty,m)=(2m+1)\pi/L,$$
$$q(-\infty,m)=(2m+1)\pi/L,\quad q(0^-,m)=(2m+2)\pi/L.$$

The eigenfunctions as well as the energies match at the impenetrable ±infinity seam and at the zero-coupling seam with the next repulsive branch. Thus, **if** we prescribe branch following through +infinity→−infinity on the real-root gas sector and continue through zero, a loop based at any c0>0 gives

$$m\longmapsto m+1,\qquad (-m-1/2,m+1/2)\longmapsto(-m-3/2,m+3/2).$$

Starting at m=0, W such formal loops yield Bethe spacing 2W+1 for N=2. This explains why the spacing-three two-particle benchmark is the candidate one-loop endpoint under this prescription. It does not establish the preparation of an N-body thermodynamic fractional-filling state.

The endpoint equations and matching limits are exact spectral statements. Their interpretation as physical transport assumes a specified branch-following protocol at the singular seams. A smooth finite bounded excursion on a nondegenerate eigenbranch that retraces c returns to that same eigenspace up to phase. It cannot be substituted for this compactified infinite-coupling prescription. A finite experimental jump between large positive and negative coupling has overlaps and transition probabilities that the spectral map alone does not compute.

## Pair correlation transforms; it need not be invariant

For either real-root branch, normalization gives A=L/2+sin(qL)/(2q). Hellmann–Feynman and direct coincidence probability agree:

$$g^{(2)}_m(0;c)=\frac{L}{2}\frac{\cos^2(qL/2)}{A}
=\frac{4Lq^2}{L(c^2+4q^2)+4c}.$$

With q=q(c,m), a formal loop based at c0 has

$$\Delta g^{(2)}=g^{(2)}_{m+1}(0;c_0)-g^{(2)}_m(0;c_0).$$

This is an explicit transformation law once branch transport is prescribed. It is not a new invariant. For m=0 and c0→0+, initial g²→1/2 while final g²→1, so Delta g²→1/2. Therefore local pair correlation is not conserved by this formal loop. At fixed positive finite c, the endpoint energy increases since q(c,m+1)>q(c,m). This is a precise example of a closed parameter prescription changing the state.

The code compares m=0 and m=1 at L=2 and c0=0.1,1,10,100; see cycle_results.json. It solves scalar equations separately on their known root brackets and verifies repulsive results against the N-body Gaudin solver. Negative-c gas results are checked against wavefunction normalization and finite differences. This does not extend the repulsive solver to general attractive N-body states.

## Separate the finite-time response problem

Let H_epsilon(t)=H0(t)+epsilon V(t), with a fixed initial rho0. Suppose a well-defined unitary propagator and its parameter derivative exist (automatically for a finite Hermitian matrix regularization; continuum contact domains require care). Write

$$A=\frac{1}{\hbar}\int_0^Tdt\,U_0(t)^\dagger V(t)U_0(t),\quad
O_H=U_0(T)^\dagger O U_0(T).$$

First-order Dyson expansion gives U_epsilon(T)=U0(T)(1−i epsilon A)+O(epsilon²), hence

$$\left.\partial_\epsilon\langle O\rangle_T\right|_0=i\,\mathrm{Tr}\{\rho_0[A,O_H]\}.$$

For fixed density and a pair-density observable O, divide by n² to obtain the protocol susceptibility chi2 proposed in the recovered thread. In a spatially homogeneous calculation one may use O=L^−1∫dx psi†²psi². If the initial state or observable also varies with epsilon, their derivative terms must be added. For V(t)=delta c(t)∫dx psi†²psi² in the dimensionless Hamiltonian, the response requires unequal-time pair-operator correlations. Static E' and E'' alone do not supply those correlations.

This identifies exactly what is still missing: a protocol H0(t), perturbation V(t), initial state and converged propagator/correlators. No numerical value of finite-time chi2 is claimed here. Nor is a SEFI description assumed to close this dynamical problem.

## Reproduce and existing literature

```sh
python -m unittest -v test_response test_cycle
python two_body_cycle.py
```

- [Yonezawa, Tanaka and Cheon, Quantum holonomy in Lieb–Liniger model (2013)](https://arxiv.org/abs/1304.5041): existing work on cyclic spectral transport through free, TG and sTG regimes.
- [Tanaka, Yonezawa and Cheon, Exotic quantum holonomy and non-Hermitian degeneracies in two-body Lieb–Liniger model (2013)](https://arxiv.org/abs/1305.1693): established two-body holonomy and eigenspace geometry. The branch map above is a direct derivation in this checkpoint's conventions, not a novelty claim.
- [Bastianello et al., fractional Fermi seas (2026)](https://arxiv.org/html/2602.17656v1): the many-body GHD setting remains distinct from the two-body spectral construction.

Next research target: compare a fully specified finite protocol with this formal branch map and quantify endpoint pair-correlation error and bound-sector population. Determine what is already known in the holonomy/GHD literature before proposing an original contribution.
