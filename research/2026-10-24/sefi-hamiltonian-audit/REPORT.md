# SEFI geometric dynamics: a reduced Hamiltonian obstruction

24 October 2026. Mathematical research checkpoint. No experimental validation or full-framework falsification is claimed.

## Result and exact scope

**The curvature-coupled minimal action displayed in the newer foundations draft admits a regular timelike planar sector whose physical coordinate-time Hamiltonian is unbounded below whenever the curvature coefficient mu_1(A) I_S is nonzero.** This is stronger than the draft's earlier completion-of-squares observation: the proper-time measure is retained, the time-reparametrization redundancy is handled, and the physical Hamiltonian is derived explicitly. The obstruction does not depend on sending curvature to infinity.

This rules out an unconditional claim of globally lower-bounded energy for the stated unrestricted classical realization. It does not prove that every trajectory grows, every restricted effective model is unacceptable, or every possible SEFI interpretation is false. The foundations draft itself did not claim a completed ghost-free Hamiltonian; this checkpoint resolves an explicitly open part of its analysis for the sector specified below. Its valid internal oscillator and conditional stability results survive.

The broad question of whether a minimally specified mathematical structure can generate geometry and operationally distinct entities remains unanswered. The audited model assumes Minkowski spacetime, its metric, smooth histories, four internal coordinates, positive internal metric coefficients, stiffnesses and constitutive coupling functions. Those are inputs, not emergent conclusions.

## Source versions and fairness to the newer formulation

All source files are pinned to public SEFI-Manuscripts commit `4643ee8cd2cf06d29fc606af80be8763fb6bc3fb`. `source_manifest.json` records paths, Git blob hashes and local-copy SHA-256 hashes. Six source texts were read: original SEFI, SEFI Space, DEFI, the October 17 foundations draft published in the October 18 research folder, the October 18 source-coupling note, and the October 20 unified draft.

The foundations draft explicitly corrects several earlier problems. It distinguishes scalar identity from a four-coordinate state, boundedness from attraction, internal from geometric stability, and classical occupation distributions from quantum fields. It already supplies the acceleration-zero counterexample and warns that higher-derivative constraints require analysis. Those corrections are acknowledged, rather than treated as new refutations of the revised text.

The original DEFI manuscript still claims that zero internal acceleration implies its tuple invariance, and that frozen identity removes coupling. These implications fail: I_O(s)=sin(s) has I_O''(0)=0 but I_O'''(0)=-1; and d(mu K^2 S)/dK=2 mu K S is generally nonzero with S frozen. The script checks both exact statements. The newer foundations draft already acknowledges both defects. Their repetition here is a version audit, not a novelty claim.

The source-coupling note labels its additional scalar field model as a candidate extension, supplies no calibrated laboratory source, and does not claim reactionless propulsion. It therefore cannot supply an unmentioned constraint or observation law for the present action.

## 1. Allowed model and regular solution sector

Write the foundations action as

    S_action = integral ds [-m + (1/2) sum_a h_a (D_s I_a)^2
                            - (1/2) sum_a k_a I_a^2
                            - mu_1(A) kappa^2 I_S
                            - mu_2(A) tau_1^2 I_W],

with h_a,k_a>0 and the source's smooth real coupling functions. The source has flat Minkowski signature (-+++), c=1, and kappa>0 on its torsion domain.

First take mu_1=mu!=0 constant, mu_2=0, and I_O=I_A=I_W=0 with their velocities zero. These are permitted constitutive choices and dynamically consistent internal data. Denote I_S by S, h_S by h, and k_S by k. We study planar timelike histories y=(t,x(t),0,0). Selecting a symmetry sector for analysis introduces no spatial walls or physical boundary.

Set v=dx/dt, a=dv/dt and gamma=(1-v^2)^(-1/2). Future-directed timelikeness permits t as a local parameter and requires |v|<1. Proper time and curvature are exactly

    ds=dt/gamma,     D_s S=gamma dS/dt,     kappa^2=gamma^6 a^2.

Restrict to the open regular domain S!=0, |v|<1, and a!=0. Thus the calculation does not assign torsion at zero curvature or cross a singular chart.

The gauge-fixed Lagrangian, retaining the measure, is

    L_t = -m/gamma + (h gamma/2) Sdot^2
          - k S^2/(2 gamma) - mu S gamma^5 a^2.                 (1)

Fixing coordinate time is not the illegitimate operation of imposing proper-time speed equal to one before variation. The gamma factors in (1) retain precisely that dependence.

## 2. Reparametrization constraints do not remove the obstruction

This step is essential. Higher derivatives alone would not justify applying an unconstrained theorem to the original action.

Before time gauge, let u0=t', u1=x', b0=t'', b1=x'', n=sqrt(u0^2-u1^2)>0, D=u0 b1-u1 b0, and w=S'. The parameter-space Lagrangian is

    L_lambda = -m n + h w^2/(2n) - k S^2 n/2
               - mu S D^2/n^5.                              (2)

Its acceleration Hessian has rank one, rather than rank two. With Pi0=partial L_lambda/partial b0 and Pi1=partial L_lambda/partial b1, its primary reparametrization constraint is

    Pi0 u0 + Pi1 u1 = 0.

In time gauge (u0,u1,b0,b1)=(1,v,0,a), Pi1=P and Pi0=-vP. Define p_i=partial L_lambda/partial u_i-dPi_i/dlambda and pS=partial L_lambda/partial w. The second reparametrization relation gives

    p0 + [p1 v + P a + pS Sdot - L_t] = 0.

It determines p0=-H_t; it does not set the physical H_t or p1 to zero. In the open chart t'=1 the gauge has no remaining time-reparametrization freedom. The spatial and internal Euler equations imply the time equation by the reparametrization Noether identity, since t'!=0. Thus this treatment retains the missing constraint, rather than deleting it.

The script differentiates (2) symbolically, checks the zero Hessian determinant, the primary constraint, and the displayed secondary relation as exact identities. The regular gauge-fixed highest-derivative Hessian below shows there are no further primary constraints in this curvature-only planar realization.

## 3. Exact Hamiltonian and local initial-value system

The independent Ostrogradsky coordinates are (x,v,S). Their momenta are

    P = partial L_t/partial a = -2 mu S gamma^5 a,
    pS = partial L_t/partial Sdot = h gamma Sdot,
    p = partial L_t/partial v - dP/dt.

The Hessian in (a,Sdot) is diagonal with entries -2 mu S gamma^5 and h gamma. It is nonsingular on the stated domain. Consequently

    a = -P/(2 mu S gamma^5),       Sdot = pS/(h gamma).

The physical coordinate-time Hamiltonian is

    H_t = p v - P^2/(4 mu S gamma^5)
          + pS^2/(2h gamma) + m/gamma + k S^2/(2 gamma).       (3)

Its canonical equations are

    xdot = v,
    vdot = -P/(2 mu S gamma^5),
    Sdot = pS/(h gamma),
    pdot = 0,
    Pdot = -p - 5 P^2 v/(4 mu S gamma^3)
           + [pS^2/(2h)+m+kS^2/2] gamma v,
    pSdot = -P^2/(4 mu S^2 gamma^5) - k S/gamma.             (4)

The right-hand side is smooth where |v|<1 and mu S!=0. For any initial point there with P!=0, standard local ordinary-differential-equation existence and uniqueness gives a solution that stays within the regular timelike, nonzero-curvature chart for a sufficiently short interval. This is a local result; continuation through S=0, |v|=1, or P=0 is not established.

The freedom in p is genuine initial data. In jet variables, with j=x'''(t),

    p = m gamma v + (h/2) gamma^3 v Sdot^2
        + (k/2) gamma v S^2 + 5 mu S gamma^7 v a^2
        + 2 mu Sdot gamma^5 a + 2 mu S gamma^5 j.            (5)

The coefficient of j is nonzero. Hence any real p is realized by a finite third derivative at a given regular initial point. Timelikeness constrains v, not this independent momentum. The source imposes no separate condition that its Noether four-momentum must be future timelike.

The script verifies (1)–(5), the Legendre transform, and both momentum evolution equations symbolically. It also verifies the internal equation independently in proper time:

    h D_s^2 S + k S + mu kappa^2 = 0.

## 4. Proof of unboundedness

Fix any regular values of v!=0, S!=0, P!=0 and pS, with |v|<1. Every term of (3) except p v is now fixed. Let p=-R sign(v) with R tending to positive infinity. Then

    H_t = -R |v| + constant -> -infinity.

By (5) each finite R corresponds to valid finite local jet data. The speed and curvature are the same for every member of this family. The constraints in section 2 fix p0,Pi0, not p, so they do not remove the family. This proves the stated unboundedness on regular physical coordinate-time phase space for either sign of mu S.

For m=h=k=mu=1, v=0.2, P=0.2, pS=0.1 and S=1, all witnesses have proper curvature 0.096:

| p | H_t |
|---:|---:|
| -1 | 1.2655630262 |
| -10 | -0.5344369738 |
| -100 | -18.5344369738 |
| -1000 | -198.5344369738 |

The negative-S examples show the same linear decrease. The finite table illustrates the exact proof; it is not the proof by itself.

The mechanism is the standard nondegenerate higher-derivative energy obstruction, not a newly discovered instability principle. See Woodard, The Theorem of Ostrogradsky, sections 2.2 and 5, https://arxiv.org/html/1506.02210 . What is supplied here is its explicit constrained application to the author's displayed action.

## 5. Extension within the source action, without choosing constant couplings

The same obstruction persists on planar histories with general smooth mu_1(A), at points where mu_1(A)S!=0. Keep all internal coordinates and momenta. The time-gauge Hamiltonian becomes

    H_t = p v - P^2/[4 mu_1(A) S gamma^5]
          + sum_a p_a^2/(2h_a gamma)
          + [m+(1/2)sum_a k_a I_a^2]/gamma.                 (6)

The highest-derivative Hessian is still nonsingular: its acceleration entry is -2 mu_1(A)S gamma^5 and its internal-velocity entries are h_a gamma>0. The momentum p is again unconstrained and linear. Varying A adds an equation, not a condition removing p.

A nonzero torsion coupling does not change this planar-sector conclusion. On a regular timelike history in a fixed timelike two-plane, tau_1=0 and b=D_s N-kappa T=0. Since tau_1^2=eta(b,b), its first variation is zero when b=0, including transverse variations. Therefore the entire first variation of mu_2(A) tau_1^2 I_W vanishes on such a history. Reflection symmetry of the remaining terms also makes their transverse first variations zero. Planar solutions of the reduced curvature problem embed as full stationary histories of the source action. This argument concerns the torsion square, which the source defines at b=0 for kappa>0; it does not divide by tau_1.

Thus for the displayed unrestricted realization, any mu_1 which is nonzero somewhere admits this obstruction, regardless of mu_2. The exact symbolic and numerical implementation tests the constant-coupling subcase; equation (6) and the torsion-square argument are analytic extensions, not simulated torsion dynamics. They do not classify a purely torsion-coupled model with mu_1 identically zero.

## 6. What the result does and does not disprove

| Statement | Finding |
|---|---|
| Positive internal oscillator coefficients alone guarantee a globally positive total energy | Disproved for nonzero curvature coupling in the displayed unrestricted realization. |
| The newer foundations model already supplied a ghost-free Hamiltonian | It explicitly did not claim this. The present result resolves an open sector adversely. |
| All trajectories are runaway | Not proved and not implied merely by unbounded energy. The numerical checks include well-behaved local solutions. |
| The decoupled Origin energy is conserved | Still proved under its stated decoupling assumptions. |
| The constant-geometry positive-Hessian internal equilibrium is Lyapunov stable | Not contradicted. Prescribing geometry removes the dynamical sector responsible for (3). |
| Every SEFI proposal is mathematically inconsistent | Not established. SEFI denotes several formulations and an interpretation with unspecified observation laws. |
| Geometry and multiple physical entities have been derived | Not established by the inspected formulations or the Lieb–Liniger benchmark. |
| The audited model is a complete successful electron/quantum theory | Not established; state preparation, quantum state space, statistics, measurement and observable maps remain incomplete. |

A lower energy bound is a clear conventional requirement for a fundamental stable-ground-state interpretation. If that requirement is retained, this unrestricted curvature realization needs modification or a justified additional constraint. Interpreting it as an effective derivative expansion could be different, but requires an explicit cutoff and reduction prescription. Imposing a bound on speed or curvature alone does not eliminate the fixed-curvature witness family above. Adding only an internal potential or simply naming a conserved Origin charge does not remove p v. A proposed repair must be analyzed as a new or restricted model, with proof that its constraints are preserved by evolution.

## 7. Reproducibility and limitations of numerical evidence

From this directory:

    python -m pip install -r requirements.txt
    python hamiltonian_audit.py

The calculation uses Python 3.14.7, NumPy 2.5.2, SciPy 1.18.1 and SymPy 1.14.0. It records twelve zero symbolic identities, 100 deterministic finite-difference Hamilton-gradient comparisons, six local integrations (two signs of S, three tolerances), eight energy witnesses, and two older-claim counterexamples. The source SHA-256 is recorded in the results file.

Numerical integrations use coordinate time [0,0.3], DOP853, maximum step 0.03, and relative tolerances 1e-8,1e-10,1e-12. Independent gradient and proper-time identity checks are used to catch sign and measure errors. The short trajectories are implementation checks on a smooth chart, not a long-time instability experiment. Global existence, a quantum vacuum-decay rate, observational exclusion bounds, a purely torsion theory, and arbitrary curved backgrounds are not computed.

## 8. Implications for continuing the mathematical program

The finite classical question above is settled within its stated assumptions. It identifies a property of a displayed realization, rather than deciding the value of the entire research program. The author has directed subsequent work toward following the mathematics from the existing models, rather than seeking a broad proof or disproof of SEFI.

For this worldline realization, a productive next question is whether it can arise as a controlled effective description of the separately studied two-field dynamics. That would require deriving collective coordinates, coefficients and an approximation regime, then checking the resulting constraints and conservation laws. It would not justify silently adding terms to obtain a desired stability result. The fundamental and effective readings of a higher-derivative action must be kept distinct.

Mathematical work can continue on explicitly defined submodels now. Experimental claims additionally need operational variables, a normalized observation law and calibrated predictions. The companion research-priorities review evaluates which existing submodel offers the clearest next step. These requirements guide the work; they are not a reason to abandon every defined calculation.

## Public provenance and continuity

The user requested that research remain pushed and renamed the public PhD repository to Research during this session. Repository ID 1379291375 and the prior research commit were verified unchanged by the rename. Existing local checkout remote was updated; its staged predecessor work was left untouched. The prior Lieb–Liniger session remains at commit 6e77ff32c13e3a7bf8b7a22b317dd3f708713851 in this same repository. Its exact seam probabilities are a standard-model benchmark and supply no missing SEFI constitutive law.

This checkpoint contains derived mathematical results and reproducible numerical checks, with no novelty or peer-review claim. Source interpretations and the broader physical conclusions remain subject to independent review.
