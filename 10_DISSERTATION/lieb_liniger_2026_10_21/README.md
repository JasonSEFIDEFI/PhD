# Finite-N Lieb–Liniger response and local two-body contact

Research checkpoint, 21 October 2026. Status: standard-model derivations and reproducible numerical checks for author review. No novelty claim or SEFI invariant is asserted.

## Provenance and scope

This checkpoint follows “Relate Quantum Order to SEFI” (conversation identifier `6ad83ea9-1bd4-83e9-a79a-5fb5242a9c0e`). Initially only a short preview was available. The author subsequently supplied the full pasted conversation; its derivations and intended next step have now been audited in [RECOVERED_CONTEXT.md](RECOVERED_CONTEXT.md). The finite-N baseline below agrees with the recovered response formulas. The next intended calculation is the two-body interaction-cycle branch map, developed in [TWO_BODY_CYCLE.md](TWO_BODY_CYCLE.md). The author selected the PhD repository. Its initial main-branch baseline was `ea632a09693f5fba23ebe4cf189ca39bbe2282de`.

The model here is the homogeneous periodic, repulsive, one-component Bose gas. Fix particle number N, circumference L>0, c>0, and distinct ordered Bethe quantum numbers I. Integers apply for odd N and half-integers for even N. Work in hbar=2m=1 units:

$$H=-\sum_j\partial_{x_j}^2+2c\sum_{i<j}\delta(x_i-x_j),\qquad E=\sum_j k_j^2.$$

In physical units, H_phys=(hbar²/2m)H and g_1D=hbar²c/m. All derivatives below hold N,L,I fixed. They are not derivatives along a thermal ensemble, a changing occupation distribution, or an interaction cycle across attractive coupling.

## Exact results within this model

### Bethe equations and invertible Gaudin response

Use the continuous real arctangent branch for positive c:

$$F_j=Lk_j+\sum_{\ell\ne j}2\arctan[(k_j-k_\ell)/c]-2\pi I_j=0.$$

Set d_jl=k_j-k_l, D_jl=c²+d_jl² and K_jl=2c/D_jl for j≠l. The Jacobian is

$$G_{jj}=L+\sum_{\ell\ne j}K_{j\ell},\qquad G_{j\ell}=-K_{j\ell}\quad(j\ne\ell).$$

For real x,

$$x^TGx=L\sum_jx_j^2+\sum_{j<\ell}K_{j\ell}(x_j-x_\ell)^2\ge L\|x\|^2.$$

Thus G is symmetric positive definite, its smallest eigenvalue is L (G1=L1), and the implicit function theorem supplies a smooth local fixed-I response at every c>0 real solution. This positivity argument is restricted to repulsion. It does not prove stability of a different field theory or control continuation through c=0.

Partial differentiation gives F_c,j=−sum_l 2d_jl/D_jl. Consequently, with u_j=dk_j/dc,

$$Gu=b,\qquad b_j=\sum_{\ell\ne j}\frac{2d_{j\ell}}{D_{j\ell}},\qquad E'=2k^Tu.$$

The sign of b is fixed by differentiating arctan(d/c) at fixed d; changing this sign would reverse the physical energy response. Solve this linear system instead of explicitly inverting G.

Summing the Bethe equations cancels pair phases: sum k_j=2π sum I_j/L. Therefore sum u_j=0. An integer shift I→I+q shifts every k by 2πq/L without changing d, u, or the local pair correlation. A boundary twist phi, in the convention F−phi=0, gives dk/dphi=1/L exactly on a fixed branch; this is a standard Galilean response, not a new identity-space invariant.

### Second coupling derivative

For w_jl=u_j−u_l, twice differentiating F gives Gv=−r, v=d²k/dc², with

$$r_j=\sum_{\ell\ne j}\frac{-4cd_{j\ell}w_{j\ell}^2+4(d_{j\ell}^2-c^2)w_{j\ell}+4cd_{j\ell}}{D_{j\ell}^2},$$

$$E''=2u^Tu+2k^Tv.$$

This follows from theta_dd=−4cd/D², theta_dc=2(d²−c²)/D² and theta_cc=4cd/D² for theta=2 arctan(d/c). The code checks the second derivative against independently re-solved energies. Ground-state energy is concave in c by the variational principle, but no blanket concavity claim for excited branches is used.

### Pair density and contact conventions

Second quantization gives H_int=c∫dx ψ†²ψ². For a normalized differentiable Bethe eigenstate, Hellmann–Feynman yields

$$E'=\int_0^L dx\,\langle\psi^{\dagger2}\psi^2\rangle=L n^2 g^{(2)}(0),\qquad n=N/L,$$

$$\boxed{g^{(2)}(0)=\frac{L}{N^2}\,2k^TG^{-1}b.}$$

This uses the ordered-pair field operator: E'=2∑_{i<j}⟨δ(x_i−x_j)⟩. It avoids a common factor-of-two error. Translation invariance of a momentum eigenstate makes the local pair density uniform. It is not the full separated correlation g²(x), nor a one-body coherence exponent.

Define integrated contact C=c²E' and contact per length C/L=c²n²g²(0). The Fourier convention is n(k)=∫dx dy exp[ik(x−y)]⟨ψ†(x)ψ(y)⟩, with ∫dk n(k)/(2π)=N on the line; its short-distance cusp gives n(k)~C/k⁴. On the ring the corresponding discrete occupation n_q has ∑_q n_q=N and n_q~C/(Lk_q⁴). Other conventions absorb factors of 2π or L. C has dimension length⁻³ and C/L length⁻⁴. The code evaluates the Hellmann–Feynman contact, not the momentum tail itself. Its derivative is C'=2cE'+c²E''.

At fixed I the exact scaling k(c/a,aL)=k(c,L)/a implies E→E/a², E'→E'/a, C→C/a³ and invariant g²(0). This supplies a dimensional check independent of finite differences.

### Independent two-particle check

For N=2, I=(−1/2,1/2), roots (−k,k) obey

$$kL+2\arctan(2k/c)=\pi,\qquad c=2k\tan(kL/2),\quad0<k<\pi/L.$$

The relative wavefunction is proportional to cos[k(r−L/2)] on 0≤r≤L. Its squared normalization integral is A=L/2+sin(kL)/(2k). Hence

$$E'=\frac{2\cos^2(kL/2)}{A}=\frac{4k}{2\tan(kL/2)+kL\sec^2(kL/2)},\qquad g^{(2)}(0)=LE'/4.$$

This scalar quantization and direct wavefunction normalization test both the Bethe solution and contact normalization without using the Gaudin derivative. For the finite-N ground state, c→0+ gives g²(0)→1−1/N; replacing it by 1 would silently take a thermodynamic limit.

For a centered fixed-I branch as c→∞, E_inf=∑(2πI_j/L)² and C→4NE_inf/L, while g²(0)→0. For nonzero total momentum use the relative energy E_inf−P²/N in this last contact expression. Vanishing pair density therefore does not imply vanishing limiting contact.

## Conditional link to fractional Fermi seas

The example family I_j=s[j−(N−1)/2], s=1 or 3, is a set of legitimate finite-N eigenstates for the parity choices used here. Spacing three leaves two holes between occupied quantum numbers. In a coarse-grained large-N sequence this motivates a filling of one third inside its support. At finite N each quantum number is either occupied or empty; no particle has fractional probability merely because we chose a sparse sequence. Rapidity filling also differs from the physical bosonic momentum distribution.

The 2026 Bastianello et al. paper studies fractional Fermi seas produced by interaction cycles through attractive and repulsive regimes, with GHD and generalized Gibbs ensembles. This checkpoint computes static repulsive branches. Identifying a sparse branch with a prepared cycle endpoint requires a justified state-selection/continuation rule. Reproducing the paper's critical correlations requires nonlocal correlators and thermodynamic analysis, which are not performed here. These finite-N derivatives cannot establish the reported correlation phase or its exponents.

## Open questions and the next defensible contribution

1. Recovered: the prior derivations agree with this baseline, with qualifications documented in RECOVERED_CONTEXT.md. The new two-body continuation calculation starts from the intended stopping point.
2. Derive the precise finite-N state map for the specified cycle; decide which attractive real-root branch and bound-state sectors are included. The present solver deliberately rejects c≤0.
3. Compare multiple microstate sequences with the same proposed coarse filling at fixed density and gamma=c/n, with systematic N scaling and uncertainty. Regularly spaced quantum numbers alone do not settle the correlation structure.
4. Compute the thermodynamic dressed response and compare its pair contact with these finite-N calculations, then analyze nonlocal correlations if criticality is the question.
5. To test SEFI/GWFM/DEFI, specify an explicit map from those variables or an action to these Bethe observables, derive an independent quantitative prediction, and compare it with this established baseline. No such map or additional conserved invariant is assumed here.

The restored research direction is cyclic correlation transport. TWO_BODY_CYCLE.md now supplies the conditional two-body spectral map and its contact change. The next step is comparison with a fully specified finite-time protocol, followed by justified larger-N extensions. This is not yet evidence of a novel law. Literature review and an actual discrepancy, theorem, or new controlled prediction would be needed for that assessment.

## Reproduce

Use Python with `pip install -r requirements.txt`, then, from this directory:

```sh
python -m unittest -v test_response
python response.py --output results.json
```

The pinned versions record the execution environment, not minimum compatible versions. The deterministic 32-case table covers N=2,3,6,12, spacings 1,3 and gamma=0.1,1,10,100 at n=1. The code continues from strong coupling, uses the analytic Jacobian, rejects residuals above 1e−9, and reports residuals and conditioning. These are floating-point checks, not interval-certified roots. Small c and large N require further precision and conditioning studies. The tests cover finite differences, two-body wavefunction normalization, single-particle contact, weak/strong limits, boost invariance, scaling, momentum response, and invalid inputs. See VALIDATION.md for the actual executed outcome.

## Sources and attribution

- [Lieb and Liniger, Exact Analysis of an Interacting Bose Gas. I (1963)](https://doi.org/10.1103/PhysRev.130.1605): foundational model and Bethe solution; cited for provenance.
- [Bucciantini, Stationary State After a Quench to the Lieb–Liniger from Rotating BECs (2016)](https://doi.org/10.1007/s10955-016-1535-7), section 2, equations 1, 6 and Gaudin norm discussion: checked Hamiltonian and logarithmic Bethe conventions.
- [Bastianello et al., Exotic critical states as fractional Fermi seas in the one-dimensional Bose gas, arXiv:2602.17656v1 (2026)](https://arxiv.org/html/2602.17656v1): checked the distinction between finite eigenstates, fractional rapidity filling, and cyclic GHD preparation. This is existing research, not a SEFI result.

The response and normalization formulas above are derived explicitly from the stated equations; they are not presented as new formulas. Numerical agreement supplies implementation evidence only.
