# Where the mathematics points next

Research priorities for Jason D. Dutton, 24 October 2026.

**Recommendation: make localized charged structures in the existing two-field model the main research line. Derive their persistence, characteristic scales and interactions, while building an explicit variational bridge to the identity/worldline model. Keep exact Lieb–Liniger calculations as a bounded comparison project.**

This recommendation follows the author's instruction to start from his models and follow their mathematical consequences. It does not require a preferred verdict on SEFI or agreement with a particular particle interpretation. A negative result, a different selected geometry, or an equivalence to an established model can all be useful findings.

## Scope of this review

The review covers the major publicly documented research tracks across Research (formerly PhD), SEFI-PY, SEFI-Manuscripts, SEFI_QEC_Stack, SEFI-Voxel, waveform-observed-entity and sefi-double-slit-simulator. It also uses the October 11 and 22 mathematical audits and the exact calculations executed in this chat. Repository snapshots and inspected paths are recorded in the accompanying source manifest.

This is a research-program assessment, not a claim to have rerun every historical simulation, reread every archive, independently audited every figure or binary, or established novelty. Recent summaries were read alongside the variational derivations and the spherical solver source. Reported historical numerical results remain attributed to their recorded runs. Arithmetic of the binding comparison was independently checked in this review. The new Hamiltonian analysis has its own symbolic and numerical checks, but has not received independent peer review.

I prioritize work by its connection to the central question, explicitness of equations, quality of existing evidence, cost of resolving the next uncertainty, and dependence on unselected assumptions. The rankings are research judgments, not numerical probabilities of success.

## The central sequence

The closest workable version of the central question is:

> Within a stated field model, can localized structures select their own size and shape, persist under disturbances, and generate reproducible interactions without inserting separate particles or prescribed particle surfaces?

That is already a substantial question. The two-field model assumes spacetime and its wave operator. Deriving a localized profile within it would demonstrate emergent spatial organization in an assumed background, not the emergence of spacetime itself. The latter remains a later, different problem.

The logical order is:

    defined field dynamics
        -> localized persistent structures
        -> dynamically distinguishable states and collective coordinates
        -> interactions and scattering
        -> effective motion and response to a changing background
        -> test whether a common effective geometry exists

Each arrow needs a calculation. The four identity-layer names do not establish the arrows, but they can motivate precise questions about persistence, transformation and state information.

## Priority 1 — Map the localized vacuum branch already found

The most promising existing calculation is the spherical, fixed-Phi-charge branch in the two-complex-field potential family at lambda=12. Its action, vacuum, charge, energy and profile equations are stated explicitly. At Q=100000, the reported refined value E/Q=1.377367898368 is below the free-Phi threshold sqrt(2)=1.414213562373: a margin of approximately 2.6054%.

The records include three spatial grids, two outer radii, residual checks, a dilation identity, constrained second variations including phase/angular sectors through l=4, and selected radial physical-time runs through T=100. This is a stronger starting point for isolated localized objects than a rendered ring or a finite-time core-survival statement alone. It is still numerical evidence for classical charged structures, not a derivation of electrons, electric charge, spin/statistics, or general nonlinear stability. See the [spherical derivation](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/847a071351ed2b1c54e240fd9a520a1cce238178/research/2026-10-19/vortex-extended/SPHERICAL_DERIVATION.md).

There is also a useful analytic separator inside the same existing potential family. At lambda=25, the exact inequality E >= sqrt(1.48)|Q_Phi| excludes below-free-threshold binding over the stated zero-charge vacuum with Q_Sigma=0. For lambda<16, the potential admits a subthreshold well; this permits, but does not by itself establish, a bound solution. Lambda=12 and 25 therefore belong to qualitatively different parts of a model family already present in the research. These are mathematical parameter studies, not coefficient fitting to a desired observed particle. See the [physical-background audit](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/847a071351ed2b1c54e240fd9a520a1cce238178/research/2026-10-19/vortex-extended/PHYSICAL_BACKGROUND.md).

**Next deliverable:** a branch map in charge Q and coupling lambda, with E(Q), omega(Q), radius, residuals, domain/grid errors and an explicit classification of bound, unbound, unresolved and failed cases. Start by continuing the existing lambda=12 solution downward and upward in Q; then approach the lambda=16 separator. Detect folds rather than treating continuation failure as nonexistence. The existing radial run helper fixes Q and lambda internally and uses a specific seed, so it needs a separate configurable continuation driver before this scan.

Test fragmentation as well as free-particle decay: E(Q)<m Q is not enough to show E(Q)<E(Q1)+E(Q-Q1). Initially test equal splits, then a resolved range of charge partitions. Compare alternative stationary profiles at the same charges. Do not assume the spherical ansatz has found the global minimizer.

**Next stability gate:** nonradial nonlinear perturbations that conserve the intended charge, with independent spatial/domain/time checks and energy/charge flux accounting. Allow generic distortions rather than only a single imposed angular symmetry. The Sigma vacuum has a phase mode; finite-box eigenvalues near zero must be separated from genuine localized modes and the continuum. Absence of negative computed eigenvalues at a finite set of grids is not a continuum theorem.

Use vacuum asymptotics and remove numerical boundaries by convergence studies. An outer numerical box is a regulator, not an assumed physical wall. Begin with the radial solution as a useful seed, then allow the dynamics to determine whether it retains, changes or loses its shape.

**Why this comes first:** it offers the shortest evidence-based route from fields to persistent structures and supplies measurable quantities for the next interaction calculation. Its relevance to the identity program still needs the bridge in priority 2.

## Priority 2 — Derive the bridge between the field realization and identity/worldline dynamics

The canonical two-field action and the four-coordinate worldline action are distinct constructions. The vortex code does not independently evolve Authorship. The repository already states this explicitly in [AUTHORSHIP_SCOPE.md](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/847a071351ed2b1c54e240fd9a520a1cce238178/research/2026-10-19/vortex-survival/AUTHORSHIP_SCOPE.md). A ring's spatial curvature is not automatically the proper acceleration of an entity's center worldline.

**Next deliverable:** derive a collective-coordinate action from a resolved localized solution of the existing field equations. Candidate coordinates include center, overall phase, charge-conjugate phase, and resolved shape/internal modes. Their number and kinetic terms should follow the solution's symmetries and perturbation modes; do not assume in advance that exactly four independent coordinates must appear.

Integrate the original field action under a documented slow-motion/mode ansatz. Derive the inertial coefficients, internal frequencies and coupling terms, estimate the discarded-mode errors, and compare effective trajectories against full-field evolution. Then ask whether particular derived quantities can consistently realize Origin, Authorship, Sovereignty or Warp. A correspondence may be exact, approximate, many-to-one, or absent.

The present chat's constrained Hamiltonian calculation matters here: the unrestricted curvature-coupled worldline realization has an energy obstruction. This does not transfer automatically to the canonical two-field action. It suggests testing whether the worldline description is a controlled effective derivative expansion, a differently constrained model, or a formulation requiring revision. Adding a potential merely to make plots stable does not establish the bridge.

The older isolated internal oscillator results remain useful: Origin energy conservation, Schur-complement stability conditions and driven-instability examples are explicit mathematics. They can benchmark an effective internal dynamics if such dynamics is derived. They do not yet identify physical observables.

**Why this ranks second:** it is the largest conceptual gap between the most developed numerical realization and the author's defining model. Progress here increases the relevance of every later simulation.

## Priority 3 — Calculate interactions of two resolved localized structures

Do this after a single-structure branch passes the required persistence and accounting checks. Construct separated initial states with specified charges, relative phase, separation and relative velocity in the same vacuum and model. First calibrate moving single structures and their energy/momentum. Then measure elastic deflection, phase-dependent forces, radiation, fusion, fragmentation and charge exchange.

Report energy, momentum and both charge budgets, including flux leaving the measurement region. Keep comparisons at matched conserved quantities. Superposing nonlinear profiles is only an initial-data prescription; measure the residual and allow its initial radiation to separate from interaction radiation.

**Next deliverable:** a small reproducible interaction map, with long-distance asymptotics where available and full-field comparisons. A negative outcome—rapid merger, dissolution or no robust interaction law—is informative. A reproducible emergent effective force would directly address the interaction part of the central question without inserting a force between pre-existing particles.

This work is more directly connected to the central question than extending a vehicle or particle animation. It is also premature to identify the measured interaction as electromagnetism or gravity.

## Priority 4 — Retain the moving-ring program as a separate branch

The N=0 traveling ring has substantial work behind it: calibrated symmetry modes, broad but finite spectral searches, finite-time survival and nonlinear selected-angular tests. The broad scan retained 2412 eigenpairs and found no accepted nonsymmetry instability within its tested scope. This is worthwhile evidence, not a full stability theorem. See the [broad spectral report](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/847a071351ed2b1c54e240fd9a520a1cce238178/SEFI-PY%20Evolution/research/physical_matter_2026_09_30/broad_scan_report.md).

Its main unresolved issue is interpretation and limits: the asymptotic field is a rotating charged medium, not the zero-charge vacuum. Domain dependence remains material for some energy/momentum/radius quantities, and fixed boundaries can exchange charge or reflect radiation. These complications make it less direct than the spherical vacuum branch for the first isolated-object study.

**Next deliverable:** one converged moving-branch result with controlled boundary flux, matched charge sector, and closed physical first-law checks. Study it as a medium-supported excitation unless the mathematics supplies a different interpretation. Keep the N=1 charged torus/Q-ring-like candidate separate; loss of an original-field zero is not preservation of a vortex.

The ring could become central again if its infinite-domain behavior and distinctive dynamics resolve cleanly. Its existing investment is a reason to preserve it, not to assume it must be the selected entity geometry.

## Priority 5 — Keep Lieb–Liniger as an exact correlation benchmark

This is the cleanest exact many-body mathematical work in the current portfolio. It has independent two-body identities, finite-N Gaudin checks and a clear separation between ideal spectral continuation and finite-jump state mixing. The latest [published checkpoint](https://github.com/JasonSEFIDEFI/Research/tree/6e77ff32c13e3a7bf8b7a22b317dd3f708713851/10_DISSERTATION/cyclic_transport_2026_10_24) includes bound-state leakage and energy truncation errors.

**Next deliverable:** a fully specified finite-duration coherent two-body cycle, converged in time and spectral cutoff against the exact seam identities. Proceed to N=3 only after that protocol is controlled. State the information required to predict pair correlations and identify what an identity description would have to retain.

Its limitation is relevance: the ring, particles, statistics and contact interaction are assumed, and interaction-cycle holonomy is existing literature. Without an explicit SEFI-to-observable map, more Bethe tables do not independently advance the author's field model. Keep the project bounded so it informs the main program rather than displacing it.

## Supporting and deferred directions

| Track | Current value | Recommended use or next condition |
|---|---|---|
| Phase dynamics and relational clocks | Precise classical identities, recurrence conditions and driven-stability distinctions | Consolidate as a carefully scoped mathematical result; reuse as a diagnostic. It does not presently derive physical time or a new clock law. |
| Quantum displacement recovery | A substantial, physically specified benchmark with unconditional entanglement fidelity and negative controls | Preserve and consider one bounded robustness study. The geometry estimator exactly matches the conventional Gaussian posterior; an improved SEFI-specific method has not been shown. |
| Calibration workbench | Reproducible inference/service workflow | Best near-term applied route if practical validation becomes the objective: obtain real calibration data and compare against a strong ordinary estimator under model drift. Tangent EWMA has not clearly beaten ordinary EWMA. |
| AI identity memory | A testable software hypothesis | Separate engineering project. Require equal-quality, equal-history baselines and an ablation of identity constraints; current results show ordinary indexing benefits. |
| Voxel/phase control and visual simulators | Communication, prototyping and visualization | Use as tools. A physical-medium choice, propagation/calibration model and measurements are needed before physical-device claims. |
| DNA/golden-ratio construction | Geometric formulas and a proposed penalty | Defer broad physical claims; a target inserted into a penalty is not a selected outcome. Needs a data/parameter and noise model before a competitive empirical study. |
| Propulsion | Explicit hypothetical scalar recoil calculation with momentum balance | Defer hardware work until the model supplies a material source coupling and calibrated response. The existing calculation is field-radiation recoil, not a demonstrated SEFI actuator. |
| Cosmology and universal emergent spacetime | Long-term motivating questions | Defer as principal projects until a defined stress-energy/field closure and controlled localized-sector response exist. Multiple infrared mode speeds currently obstruct an unqualified common-metric interpretation. |

The quantum-recovery result is particularly important for fair prioritization. At the primary noise condition the geometry estimator improves over likelihood-only ML, but agrees with an independent conventional posterior to numerical precision. Its advantage reverses under a particular unmodeled mean shift. That makes robust recovery under drift a reasonable separate engineering question; it does not justify expanding a claim of unique geometric QEC. See the [benchmark report](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/847a071351ed2b1c54e240fd9a520a1cce238178/SEFI-PY/benchmarks/displacement_recovery/BENCHMARK_REPORT.md).

## How geometry should re-enter the main program

The existing scalar model has an assumed microscopic Minkowski cone. A phase-only infrared metric describes a restricted mode. It does not automatically govern the carrier, the core or every localized excitation; the [characteristic audit](https://github.com/JasonSEFIDEFI/SEFI-PY/blob/847a071351ed2b1c54e240fd9a520a1cce238178/SEFI-PY%20Evolution/research/physical_matter_2026_09_30/three_track_derivation.md) already exhibits distinct infrared speeds in a two-condensate example.

After deriving localized collective dynamics, place a resolved structure in a slowly varying admissible background. Calculate its response directly and compare it with the proposed effective metric. Test whether different structures respond with the same coefficients after appropriate normalization. Agreement over a controlled regime would support a limited shared effective geometry; disagreement would identify the regime's limits. Neither outcome requires treating a chosen metric as fundamental from the outset of that effective calculation. It still does not remove the background geometry assumed by the underlying action.

## Recommended allocation and first checkpoint

For the next research block, allocate roughly 60% to the localized-vacuum branch map and nonradial checks, 25% to the collective-coordinate/identity bridge, and 15% to exact correlation benchmarks and consolidated provenance. These are suggested effort allocations, not measured return estimates. Do not launch all application tracks simultaneously.

**The immediate task I would start:** reproduce the lambda=12 fixed-charge profile at one reference grid and a refinement, then continue Q with a configurable solver and record E(Q), omega(Q), radius and fragmentation margins. Use the analytic lambda=16 threshold to plan the parameter map, not as proof that every lambda<16 has a stable solution. Publish failures, unresolved folds and boundary sensitivity alongside successes.

The first checkpoint should end with one of three clear findings: a controlled interval of localized candidates; a resolved loss of binding or persistence; or a diagnosed numerical/variational obstruction. Then choose the next computation from that result.

## Position relative to existing mathematics

Charged localized scalar structures and vortons are established subjects. Relevant primary comparisons include [Lennon, multi-field Q-balls](https://arxiv.org/abs/2112.14263), [Mai and Schweitzer, Q-ball stress-energy and stability](https://arxiv.org/abs/1206.2632), and [Tallarita et al., vortons and decay into Q-rings](https://arxiv.org/abs/1909.01950). Those works are context, not validation of the present numerical branch.

A useful contribution could be a controlled branch/stability classification of this specific potential family, a derived effective action and identity correspondence, or a well-resolved interaction result. None is automatically novel because it was developed in this program. The strongest direction is the one whose explicit equations continue to produce controlled results and whose comparison with known models is clear.
