# Cyclic correlation transport: finite-jump seam audit

24 October 2026. Status: exact identities within a specified benchmark, floating-point experiments, and conditional endpoint calculations. No new physical law or novelty claim.

## Question and assumption ledger

Can geometry, distinguishable physical entities, and interactions emerge from minimally constrained structure? This session does not answer that question affirmatively. The Lieb–Liniger benchmark already assumes a one-dimensional ring, its length L, a fixed particle number N, bosonic exchange symmetry, a Hilbert space, time evolution, and contact interaction strength c. Periodicity is an imposed geometric identification even though a ring has no edge. No geometric boundary is inferred from these calculations. No additional container, particle trajectories, entity labels, preferred spatial origin, or SEFI layers are introduced.

Its narrower purpose is to audit correlation transport exactly before using it as a proposed analogy for emergence. A redistribution of correlations between identical bosons does not establish distinguishable physical entities. Bethe root indices order roots; they do not label distinguishable particles. The coupling is specified, not emergent. GWFM/SEFI/DEFI currently has no independently derived observable map to this calculation.

## Recovered context and repository inspection

The supplied Getting Transcripts preview lacks the mathematical assistant messages. No read_thread tool was exposed in this session; the full referenced chat was therefore not recovered. Instead, the October 21 local checkpoint and its RECOVERED_CONTEXT.md were inspected. Four copied Python files were verified byte-for-byte using Git blob hashes against the public research branch at a6d1e35a07551c7a07ff2b33c8508de17a038254:

| File | Git blob |
|---|---|
| response.py | f3f2625a0423da1d2d594703714dd8d66be504d7 |
| two_body_cycle.py | 7aa9f721c78fa57bdea5b255720eacb2f8e4ce35 |
| test_response.py | 162525ef2d6fdd729dd7928e1e138fe362b61f68 |
| test_cycle.py | bc1ddf191a1f19d4b14b8bab977659c50e9272c9 |

Public main snapshots inspected: PhD 5c3fc767621afaeac61246b93270f57bffd7d4e1; SEFI 9c93a57138b5d5c25b0aaa49ad5e42d72205919f; SEFI-PY 847a071351ed2b1c54e240fd9a520a1cce238178; SEFI-Manuscripts 4643ee8cd2cf06d29fc606af80be8763fb6bc3fb. Repository trees were inspected to locate the work, not to audit every file. The relevant calculation is on PhD's research/lieb-liniger-response-2026-10-21 branch, not its main branch. The local October 22 manuscript audit was also consulted for the missing observable-map limitation. Prior work and local staged changes were left untouched.

## Exact two-body seam identities

Use hbar=2m_atom=1, total momentum zero. H=-sum partial_xj^2+2c delta(x1-x2). With r in [0,L], normalized relative gas eigenfunctions are

    f_q(r) = cos[q(r-L/2)] / sqrt(A_q)
    A_q = L/2 + sin(qL)/(2q),     E_q = 2q^2
    c = 2q tan(qL/2).

At positive c=C, branch m has 2m*pi < qL < (2m+1)*pi. At c=-C, gas branch j has (2j+1)*pi < p_j L < (2j+2)*pi. These are the exact scalar Bethe solutions from the prior checkpoint.

Define S(z)=sin(z)/z, S(0)=1. Direct integration gives the signed overlap

    U_jm = L/[2 sqrt(A_q A_p)] *
           [S((q-p)L/2) + S((q+p)L/2)].

For a sudden +C to -C jump the state is continuous. Thus |U_jm|^2 is its exact probability in gas branch j immediately after the jump. These are continuum eigenfunctions; there is no spatial mesh or truncated Hamiltonian here.

There is also one even relative bound state. Its inverse length kappa>0 solves

    C = 2 kappa tanh(kappa L/2),  E_b=-2 kappa^2.

Let a=L/2, y=kappa*a, h(r)=exp(-y)cosh[kappa(r-a)], and

    B = integral h^2 dr = (L/2)exp(-2y) + (1-exp(-4y))/(4 kappa).
    V_bm = {kappa(1-exp(-kappa L))cos(qa)
             + q(1+exp(-kappa L))sin(qa)}
           / {(kappa^2+q^2)sqrt(A_q B)}.

Then P_b=|V_bm|^2. Exponential scaling avoids overflow at large C. The unique positive bound root follows because y*tanh(y) is strictly increasing from zero to infinity.

**Exact completeness statement:** in this fixed momentum, bosonic sector, the attractive bound state and gas eigenfunctions form the discrete Sturm–Liouville basis. Therefore P_b+sum_j |U_jm|^2=1. Numerically only a finite partial sum is evaluated. Orthogonality to the bound state and between different gas roots at the same coupling is checked separately.

**Independent boundary identity:** integration by parts with the contact boundary condition yields

    (2q^2-2p^2) U_jm = 4C f_q(0) f_p(0).

**Exact energy identity in the quadratic-form sense:** the pre-jump state need not belong to the post-jump operator domain, but belongs to its form domain. Since H(-C)-H(+C)=-4C delta(r),

    -2 kappa^2 P_b + sum_j 2p_j^2 |U_jm|^2
       = 2q^2 - 4C cos^2(qL/2)/A_q.

A finite sum underestimates this energy because omitted gas energies are positive. Small omitted probability does not bound the error of an unbounded observable such as energy. Cutoff doubling checks the energy error decreases; no claim of machine-precision energy completeness is made.

## Conditional cyclic correlation endpoint

The seam probabilities above need only an instantaneous jump and initial eigenstate. To translate them to an endpoint at c0=1 we additionally choose ideal branch-following ramps from c0 to +C and from -C through zero to c0. This is a mathematical limiting prescription, with no finite ramp duration claimed. Attractive gas branch j continues to repulsive branch j+1; the bound branch connects through the free ground state to repulsive branch zero. These match the two-body quantization limits.

We then explicitly **dephase in the final energy basis**. This additional channel may represent a long-time average at c0 in this nondegenerate sector; it is not instantaneous coherent unitary evolution. The conditional prediction is

    g2_dephased = P_b g2_0(c0) + sum_j |U_jm|^2 g2_(j+1)(c0).

Without dephasing, phase-dependent off-diagonal matrix elements contribute. We have neither simulated finite-duration ramps nor calculated coherent endpoint phases. The displayed endpoint is not their substitute. For repulsion, 0<=g2_j<1 follows from the exact two-body expression 4Lq^2/[L(c0^2+4q^2)+4c0]. Hence the omitted dephased g2 contribution is between zero and the omitted probability, apart from numerical roundoff. We do not renormalize a truncated probability sum.

For L=2, initial m=0, c0=1, the initial g2 is 0.3626585433 and the formal perfect-target endpoint is 0.9352851632:

| C | P_target | P_bound | Other gas | Conditional dephased endpoint g2 |
|---:|---:|---:|---:|---:|
| 1 | 0.02103418 | 0.97765371 | 0.00131211 | 0.37551921 |
| 3 | 0.19279773 | 0.79980442 | 0.00739785 | 0.47765884 |
| 10 | 0.82763277 | 0.15218082 | 0.02018641 | 0.84913495 |
| 30 | 0.98084481 | 0.00937411 | 0.00978107 | 0.93041311 |
| 100 | 0.99828325 | 0.00029677 | 0.00141997 | 0.93518939 |

These use 256 gas states; other-gas values are partial sums. For these m=0 cases the omitted probability ranges from 2.94e-10 to 7.52e-9. The absolute energy truncation errors range from 0.001146 to 0.029328 in the stated units. In particular, C=100 still has energy error about 0.02933 despite probability deficit about 7.52e-9. Convergence tables at 64,128,256 states for both m=0 and m=1 are retained in jump_results.json. Probabilities are scale invariant under (C,L)->(C/a,aL); that identity is tested independently.

## Justified finite-N extension

Yonezawa, Tanaka and Cheon (2013), equations 15–16, already derive the ideal cycle map for ordered free momenta. For general L, with integer free momentum numbers n_j and a_j=j-(N+1)/2 (j starts at 1), it is

    n'_j = n_j + 2a_j;     k_j(0)=2pi n_j/L.

On the positive-c branches in this checkpoint's convention, I_j=n_j+a_j. The corresponding ideal transported branch labels obey

    I'_j = I_j + 2a_j.

Starting from the repulsive ground branch I=a, W ideal cycles therefore give I=(2W+1)a. This is a conditional ideal-cycle endpoint selection using an existing result. We do not generalize the two-body finite-jump probabilities to N>2: many-body bound strings and overlaps require a separate calculation.

Static repulsive Bethe/Gaudin results at N=L, c=gamma=1:

| N | W=0 g2 | W=1 g2 | W=2 g2 |
|---:|---:|---:|---:|
| 2 | 0.36265854 | 0.93528516 | 0.98180504 |
| 3 | 0.43697984 | 1.22373978 | 1.30179508 |
| 6 | 0.47721288 | 1.46213921 | 1.60362758 |
| 12 | 0.48647433 | 1.52219931 | 1.72244057 |
| 24 | 0.48875119 | 1.52822279 | 1.74963011 |

These are numerical observations for selected eigenstates, not a thermodynamic extrapolation or proof of fractional-sea criticality. The inequality g2<1 used for the two-body tail bound does not apply to general N. The Gaudin positive-definiteness proof, fixed-I Hellmann–Feynman normalization, and boost/scaling identities remain those in the October 21 checkpoint. Each new case checks total momentum zero and minimum Gaudin eigenvalue L; residuals and conditioning are recorded. No attractive finite-N solver is introduced.

## Reproduce and executed checks

In this folder, Python with NumPy 2.5.2 and SciPy 1.18.1:

    python -m unittest -v test_response test_cycle
    python jump.py

The four baseline Python files are copied unchanged from the public checkpoint, so the new session is self-contained. jump.py validates itself before writing its results. It checks gas and bound overlaps against independent adaptive quadrature for C=0.1,1,10,100 and m=0,1,2; bound normalization; gas/gas and gas/bound orthogonality; the boundary overlap identity; probability completeness; cutoff convergence of the energy identity; and scaling. Existing nine test groups pass, including independent two-body normalization, finite-difference Gaudin response, spectral seams, weak/strong limits, and invalid inputs. These are double-precision checks, not interval-certified proofs. jump_results.json records interpreter/library versions and SHA-256 hashes of the executed Python sources.

Executed with Python 3.14.7. The final baseline test run passed nine groups in 3.954 seconds. Maximum new finite-N Bethe residual: 1.9895196601282805e-13; maximum response residual: 7.105427357601002e-15; largest Gaudin condition number: 2.372858854782198. Maximum independent overlap integration discrepancy: 2.220446049250313e-16. Across all m and all cutoffs, the largest missing probability is 4.102913087056237e-6 (the coarse cutoff is retained rather than silently normalized away). The script completed successfully after adding its independent boundary-identity check.

## Implications and open work

1. Local pair correlation is transported and is not a cycle invariant in this benchmark. Finite seam strength materially changes state populations and conditional correlation endpoints.
2. A complete one-body reduced density operator still cannot determine arbitrary pair correlations, as the prior checkpoint's explicit two-mode counterexample shows. A proposed single-entity encoding needs additional state information or a stated restricted family.
3. Nothing here selects geometry, particle number, interaction, or an observable algebra from an unstructured starting point. A noncircular emergence claim needs a specified primitive structure and equivalence relation, followed by derived locality/dimension, operational entity criteria, and interactions. Merely defining a correlation distance would impose an observable/metric choice and would not establish a physical spacetime.
4. Next bounded calculation: choose actual ramp functions and durations, evolve the coherent two-body state, resolve the bound sector, and converge time and spectral cutoffs against these seam identities. Only then consider N=3 overlaps, rather than assuming products of two-body probabilities. The many-body static data above are a baseline for that future work.

## Literature and attribution

- Lieb and Liniger, 1963, foundational model: https://doi.org/10.1103/PhysRev.130.1605
- Yonezawa, Tanaka and Cheon, Quantum holonomy in Lieb–Liniger model, 2013, v2: https://arxiv.org/html/1304.5041 . Inspected this session, especially equations 10–16; ideal many-body cycle map is existing work, not a project discovery. Their Hamiltonian differs by an overall factor of two from ours, with g=c.
- Tanaka, Yonezawa and Cheon, two-body holonomy, 2013: https://arxiv.org/abs/1305.1693 . Prior-checkpoint citation; not independently re-audited here.
- Bastianello et al., 2026 v1: https://arxiv.org/html/2602.17656v1 . Inspected this session for the distinction between cyclic GHD/GGE preparation and static microstates. No nonlocal critical exponent or fractional-filling phase is reproduced here.
- Public predecessor: https://github.com/JasonSEFIDEFI/PhD/tree/a6d1e35a07551c7a07ff2b33c8508de17a038254/10_DISSERTATION/lieb_liniger_2026_10_21

Signed overlaps, the bound-state sector, and the energy form identity are derived explicitly above as standard spectral calculations; implementation and numerical tables are the contribution of this session. Literature coverage is targeted, not exhaustive.
