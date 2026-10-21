# Executed validation — 21 October 2026

## Recovered-context continuation

After the full conversation was supplied, `python -m unittest -v test_response test_cycle` passed all nine test groups in 7.810 seconds. The four new groups cover nine repulsive endpoint comparisons against the Gaudin solver; twelve attractive real-root checks against wavefunction normalization and finite-difference root derivatives; matching limits at both spectral seams; free-limit contact; and invalid inputs. `python two_body_cycle.py` generated four endpoint comparisons in cycle_results.json.

For N=L=2 and c=1, the prescribed one-loop spectral endpoints have g²(0)=0.362658543 and 0.935285163, giving Delta g²=0.572626620. This is a conditional spectral endpoint comparison, not a simulated physical cycle or experimental prediction. Full derivation and limitations are in TWO_BODY_CYCLE.md.

## Original finite-N baseline

Environment: Python 3.14.7, NumPy 2.5.2, SciPy 1.18.1 on Windows.

`python -m unittest -v test_response` passed all five test groups (2.972 seconds in the final recorded run). These include 18 fixed-I finite-difference cases for rapidity, energy and energy curvature; five independent two-particle scalar solves and wavefunction normalizations; weak- and strong-coupling limits; momentum, boost and scale identities; one-particle contact; and rejection of invalid inputs. Assertions and tolerances are visible in test_response.py.

`python response.py --output results.json` generated all 32 cases. The maximum absolute Bethe residual was 1.5276668818842154e−13, the maximum linear-response residual was 1.7763568394002505e−14, and the largest Gaudin condition number was 6.326289865435106.

Selected numerical observations at N=L=6 (density one):

| c=gamma | g²(0), spacing 1 | g²(0), spacing 3 |
|---:|---:|---:|
| 0.1 | 0.76221986 | 1.65431229 |
| 1 | 0.47721288 | 1.46213921 |
| 10 | 0.06893022 | 0.41794839 |
| 100 | 0.00120391 | 0.01071525 |

These are different explicitly selected eigenstates, not a measurement of a cycle-prepared ensemble. A spacing-three value above one is not a normalization failure: an excited Bose eigenstate may have enhanced local pair correlation. The weak ground-state limit 1−1/N is not an excited-state bound.

During implementation, the tests exposed a Jacobian callback argument mismatch and list-to-array conversion missing in residual reporting. Both were corrected before the passing run. The earlier unsuccessful runs are not counted as validation.

Limits: no attractive-branch continuation, thermodynamic convergence, momentum-tail computation, nonlocal correlations, interval certification, experiment, or validation of SEFI/GWFM/DEFI is claimed. Passing checks establish internal consistency for the named finite-N implementation and cases.
