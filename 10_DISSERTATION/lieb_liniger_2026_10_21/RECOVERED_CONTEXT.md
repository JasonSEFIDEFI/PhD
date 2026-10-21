# Recovered research context and audit

The author supplied the conversation as `Pasted text.txt` on 21 October 2026. SHA-256: `12D5EACFB073A0B48583924454F304B773CA7183148A1E6C4C98AF6EAFAC132E`. The raw conversation is retained in the local attachment; this note records the mathematical substance without republishing the surrounding social-media content.

## Research intent and stopping point

Let the mathematics determine the claims and eventual paper. Suggestions about SEFI's single/dual-body description are questions to investigate, not assumptions. Preserve exact, conditional, numerical, open and hypothetical statements separately. Keep counterexamples and failures. A formula derived in this project is not thereby new to the literature.

The original thread progressed through idealized fractional fillings, reduced density matrices, their information loss and dynamical hierarchy, then the finite-N Bethe/Gaudin response and local pair correlation. Its last proposed calculation was the interaction-cycle map for an exact two-body system, followed by larger N. It explicitly distinguished eigenstate continuation from finite-time unitary evolution. The initial PR reproduced the finite-N baseline but did not yet perform this next calculation.

## Audit of the recovered mathematics

| Recovered statement | Assessment and limits |
|---|---|
| For filling theta(lambda)=nu on [−Q,Q], M0=2nu Q and M2=2nu Q³/3 | Correct. Q=sqrt(3M2/M0), nu=M0/(2Q) within this specified family. For shifted distributions use central moments. These are moments of filling, not automatically physical particle/energy densities. Those require the interacting root density rho_p=theta rho_t. |
| Width and filling reconstructed from central moments are invariant under rapidity translation | Correct for that transformation. It says nothing by itself about an interaction cycle. |
| Fourier kernel nu sin(Qx)/(pi x) | Correct transform with the stated 1/(2pi) convention. It is not generally the physical bosonic one-body correlation in the interacting gas. |
| A spectral-radius criterion for an attracting cycle-map fixed point | Conditional on an actual differentiable map and the stated function-space assumptions. Full unitary evolution preserves trace distance and cannot be a strict global contraction. No attracting FFS manifold was derived. |
| Tr gamma1=N; Tr gamma2=N(N−1); Tr_2 gamma2=(N−1)gamma1 | Correct for the unnormalized reduced-density-matrix convention, N≥2 for contraction back to gamma1. |
| C2=rho2−(N−1)rho rho/N has zero integral in its second coordinate | Correct at fixed N. This is a chosen finite-N reference subtraction, distinct from the usual cumulant rho2−rho rho, whose integral is −rho. C2=0 for a pure condensate product; it is not a general independence theorem for arbitrary multimode bosonic states. |
| Same gamma1 can coexist with different gamma2 | Correct. The states |1u,1v> and (|2u,0v>+|0u,2v>)/sqrt(2) share gamma1 but have <nu nv>=1 and 0. Thus an ordinary one-body reduced state cannot be a universal complete encoding of the many-body state. |
| i hbar dot gamma1=[h,gamma1]+Tr_2[V12,gamma2] | Correct in the stated unnormalized convention, with appropriate domains/contact boundary conditions. This hierarchy is not closed by the scalar contact g²(0). |
| G k'=b, physical E'=(hbar²/m) k^T G^−1 b | Correct on the smooth repulsive branch. The PR proves positive definiteness there. |
| g²(0)=2 k^T G^−1 b/(L n²), and N=2 expression 4Lq²/[L(c²+4q²)+4c] | Correct, matching the current implementation and independent wavefunction normalization. |
| Delta g² after a cycle is a trace against the evolved density operator | Correct identity when the state and observable have finite expectation. It becomes a prediction only after specifying initial state and cycle evolution. |

No nontrivial SEFI invariant or closure theorem was established. The phrases suggesting a strongest scientific contribution were research judgments, not a literature proof that the cycle problem is unsolved. Two-body and N-body Lieb–Liniger holonomy already have a 2013 literature; the continuation now added is an attributed baseline.

## Restored next step

TWO_BODY_CYCLE.md derives the real-root spectral map and compares its endpoint pair correlation. It does not identify this formal map with a finite-time experiment. The next unresolved input for that calculation is a specified physical protocol, including the treatment of the strongly repulsive-to-attractive transition, timing and bound-state leakage. These must be chosen and documented before a numerical finite-time evolution is meaningful.
