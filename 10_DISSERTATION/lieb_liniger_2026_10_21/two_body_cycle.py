"""Static real-root branch continuation, not a finite-time cycle simulation."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq


def branch(c, length=2., m=0):
    """m labels the positive-c branch; retain it on the negative-c gas branch."""
    if not np.isfinite(c) or c == 0 or not np.isfinite(length) or length <= 0:
        raise ValueError('Require finite nonzero c and finite L>0')
    if int(m) != m or m < 0:
        raise ValueError('m must be a nonnegative integer')
    target = (2*m+1)*np.pi
    # Dimensionless x=qL brackets avoid tangent poles.
    if c > 0:
        lo, hi = 2*m*np.pi, target
    else:
        lo, hi = target, (2*m+2)*np.pi
    x = brentq(lambda x: x+2*np.arctan(2*x/(c*length))-target,
               lo, hi, xtol=1e-13)
    q = x/length
    denominator = length*(c*c+4*q*q)+4*c
    qp = 4*q/denominator
    return dict(c=float(c), L=float(length), m=int(m), q=float(q),
                energy=float(2*q*q), dq_dc=float(qp),
                g2=float(4*length*q*q/denominator),
                residual=float(x+2*np.arctan(2*x/(c*length))-target))


if __name__ == '__main__':
    rows = []
    for c in (.1, 1., 10., 100.):
        initial, final = branch(c, m=0), branch(c, m=1)
        rows.append(dict(c=c, initial=initial, final=final,
                         delta_g2=final['g2']-initial['g2']))
    Path('cycle_results.json').write_text(json.dumps(dict(
        status='Formal branch endpoints only; cycle transport is conditional',
        units='hbar=2m_atom=1; N=L=2', cases=rows), indent=2)+'\n', encoding='utf-8')
    print('Wrote 4 endpoint comparisons to cycle_results.json')
