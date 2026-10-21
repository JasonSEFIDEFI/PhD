"""Finite-N repulsive periodic Lieb-Liniger response; hbar=2m=1."""
import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import root


def quantum_numbers(n, spacing=1):
    if n < 1 or int(n) != n or spacing < 1 or int(spacing) != spacing:
        raise ValueError("N and spacing must be positive integers")
    if n % 2 == 0 and spacing % 2 == 0:
        raise ValueError("Centered even-N states require odd spacing")
    return spacing * (np.arange(n) - (n - 1) / 2)


def validate(c, length, numbers):
    q = np.asarray(numbers, dtype=float)
    if not np.isfinite(c) or not np.isfinite(length) or c <= 0 or length <= 0:
        raise ValueError("Require finite c>0 and L>0")
    if q.ndim != 1 or not len(q) or not np.all(np.isfinite(q)):
        raise ValueError("Require a nonempty finite vector of quantum numbers")
    target = 0 if len(q) % 2 else 0.5
    if not np.allclose(q - target, np.round(q - target), atol=1e-12, rtol=0):
        raise ValueError("Wrong periodic-boson quantum-number parity")
    if np.any(np.diff(q) <= 0):
        raise ValueError("Quantum numbers must be strictly increasing")
    return q


def residual(k, c, length, numbers):
    d = k[:, None] - k[None, :]
    return length * k + np.sum(2 * np.arctan(d / c), axis=1) - 2 * np.pi * numbers


def gaudin(k, c, length):
    d = k[:, None] - k[None, :]
    kernel = 2 * c / (c*c + d*d)
    np.fill_diagonal(kernel, 0)
    return np.diag(length + kernel.sum(axis=1)) - kernel


def solve(c, length, numbers):
    q = validate(c, length, numbers)
    # Continue from a well-conditioned strong-coupling solution.
    start = max(c, 100 * (1 + np.max(np.abs(2*np.pi*q/length))))
    k = 2*np.pi*q/length
    for coupling in np.geomspace(start, c, max(2, int(np.log(start/c)*8)+2)):
        result = root(residual, k, args=(coupling, length, q),
                      jac=lambda roots, cc, ll, qq: gaudin(roots, cc, ll), tol=1e-11)
        k = result.x
        error = np.max(np.abs(residual(k, coupling, length, q)))
        if not np.all(np.isfinite(k)) or error > 1e-9:
            raise RuntimeError(f"Bethe solve failed: residual={error}: {result.message}")
    if len(k) > 1 and np.any(np.diff(k) <= 0):
        raise RuntimeError("Unordered roots")
    return k


def observables(c, length, numbers):
    numbers = validate(c, length, numbers)
    k = solve(c, length, numbers)
    g = gaudin(k, c, length)
    d = k[:, None] - k[None, :]
    den = c*c + d*d
    b = np.sum(2*d/den, axis=1)
    u = np.linalg.solve(g, b)
    w = u[:, None] - u[None, :]
    r = np.sum((-4*c*d*w*w + 4*(d*d-c*c)*w + 4*c*d)/den**2, axis=1)
    v = np.linalg.solve(g, -r)
    ep = float(2*k@u)
    epp = float(2*(u@u + k@v))
    n = len(k)
    return dict(k=k.tolist(), dk_dc=u.tolist(), d2k_dc2=v.tolist(),
                energy=float(k@k), dE_dc=ep, d2E_dc2=epp,
                g2=length*ep/n**2, contact_integrated=c*c*ep,
                contact_density=c*c*ep/length,
                bethe_residual=float(np.max(np.abs(residual(k, c, length, numbers)))),
                response_residual=float(np.max(np.abs(g@u-b))),
                gaudin_min_eigenvalue=float(np.linalg.eigvalsh(g)[0]),
                gaudin_condition=float(np.linalg.cond(g)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('results.json'))
    args = parser.parse_args()
    cases = []
    for n in (2, 3, 6, 12):
        for spacing in (1, 3):
            for gamma in (0.1, 1., 10., 100.):
                length = float(n)  # density=1, hence c=gamma
                q = quantum_numbers(n, spacing)
                cases.append(dict(N=n, L=length, c=gamma, spacing=spacing,
                                  quantum_numbers=q.tolist(), **observables(gamma, length, q)))
    payload = dict(conventions='hbar=2m=1; fixed N,L,I coupling derivatives',
                   python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__, cases=cases)
    args.output.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    print(f'Wrote {len(cases)} cases to {args.output}')


if __name__ == '__main__':
    main()
