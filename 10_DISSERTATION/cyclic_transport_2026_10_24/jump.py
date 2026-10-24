"""Exact two-body sudden-jump overlaps, not a finite-duration ramp simulation."""
import json
import platform
import hashlib
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.optimize import brentq
from two_body_cycle import branch
from response import observables, quantum_numbers


def norm(q, L):
    return L/2 + L/2*np.sinc(q*L/np.pi)


def gas_overlap(q, p, L):
    integral = L/2*(np.sinc((q-p)*L/(2*np.pi)) + np.sinc((q+p)*L/(2*np.pi)))
    return integral/np.sqrt(norm(q, L)*norm(p, L))


def bound(C, L):
    if not np.isfinite(C) or C <= 0 or not np.isfinite(L) or L <= 0:
        raise ValueError('Require finite C,L>0')
    # y=kappa L/2; y*tanh(y)=CL/4.
    z = C*L/4
    y = brentq(lambda y: y*np.tanh(y)-z, 0., z+np.sqrt(z)+1, xtol=1e-13)
    kappa = 2*y/L
    # exp(-y)*cosh(kappa*(r-L/2)); stable even at strong binding.
    A = L/2*np.exp(-2*y) + (-np.expm1(-4*y))/(4*kappa)
    return kappa, A


def bound_overlap(q, C, L):
    k, A = bound(C, L)
    a = L/2
    # Exact integral of cos(q*s)*cosh(k*s), scaled by exp(-k*a).
    e = np.exp(-k*L)
    integral = (k*(1-e)*np.cos(q*a) + q*(1+e)*np.sin(q*a))/(k*k+q*q)
    return integral/np.sqrt(norm(q, L)*A)


def jump(C, L=2., m=0, cutoff=256):
    if int(cutoff) != cutoff or cutoff < m+1:
        raise ValueError('cutoff must be integer and include target branch')
    q = branch(C, L, m)['q']
    ps = np.array([branch(-C, L, j)['q'] for j in range(cutoff)])
    probs = np.array([gas_overlap(q, p, L)**2 for p in ps])
    pb = bound_overlap(q, C, L)**2
    k, _ = bound(C, L)
    total = pb + probs.sum()
    # Quadratic-form identity: H(-C)=H(+C)-4C delta(r).
    expected = 2*q*q - 4*C*np.cos(q*L/2)**2/norm(q, L)
    spectral = -2*k*k*pb + np.dot(2*ps*ps, probs)
    # Hypothetical ideal branch-following legs, followed by complete dephasing:
    # attractive gas j -> repulsive j+1; bound -> repulsive ground state.
    finals = np.array([branch(1., L, j+1)['g2'] for j in range(cutoff)])
    g2 = pb*branch(1., L, 0)['g2'] + probs@finals
    return dict(C=C,L=L,m=m,cutoff=cutoff,target_probability=float(probs[m]),
                bound_probability=float(pb),other_gas_probability=float(probs.sum()-probs[m]),
                probability_sum=float(total),missing_probability=float(1-total),
                energy_form_identity=float(expected),energy_spectral_partial=float(spectral),
                energy_error=float(spectral-expected),
                dephased_endpoint_g2_partial=float(g2),
                ideal_target_endpoint_g2=branch(1.,L,m+1)['g2'])


def validate():
    errors=[]
    for C in (0.1,1.,10.,100.):
        for m in (0,1,2):
            q=branch(C,m=m)['q']; p=branch(-C,m=m)['q']
            numeric=quad(lambda r: np.cos(q*(r-1))*np.cos(p*(r-1)),0,2,epsabs=1e-12)[0]
            errors.append(abs(gas_overlap(q,p,2)-numeric/np.sqrt(norm(q,2)*norm(p,2))))
            lhs=(2*q*q-2*p*p)*gas_overlap(q,p,2)
            rhs=4*C*np.cos(q)*np.cos(p)/np.sqrt(norm(q,2)*norm(p,2))
            assert abs(lhs-rhs)<1e-10
            k,A=bound(C,2)
            bfun=lambda r: .5*(np.exp(-k*r)+np.exp(-k*(2-r)))
            bn=quad(lambda r:bfun(r)**2,0,2,epsabs=1e-12)[0]
            assert abs(bn-A)<1e-11
            numeric=quad(lambda r:np.cos(q*(r-1))*bfun(r),0,2,epsabs=1e-12)[0]/np.sqrt(norm(q,2)*A)
            errors.append(abs(numeric-bound_overlap(q,C,2)))
            # Sturm-Liouville orthogonality at a common attractive coupling.
            assert abs(bound_overlap(p,C,2))<1e-11
            pp=branch(-C,m=m+1)['q']
            assert abs(gas_overlap(p,pp,2))<1e-11
    assert max(errors)<1e-11
    for C in (1.,10.,100.):
        a=jump(C,cutoff=128); b=jump(C,cutoff=256)
        assert -1e-12 < b['missing_probability'] < 1e-6
        assert abs(b['energy_error']) < abs(a['energy_error'])
        assert abs(b['energy_error']) < 0.6*abs(a['energy_error'])
        # Scaling C->C/a,L->aL leaves every probability invariant.
        scaled=jump(C/3,L=6,cutoff=128)
        for key in ('target_probability','bound_probability','probability_sum'):
            assert abs(a[key]-scaled[key])<1e-11
    return dict(max_overlap_quadrature_error=max(errors),status='passed')


def main():
    checks=validate()
    rows=[jump(C,m=m,cutoff=cut) for C in (1.,3.,10.,30.,100.) for m in (0,1) for cut in (64,128,256)]
    finite=[]
    for N in (2,3,6,12,24):
        a=quantum_numbers(N)
        for W in (0,1,2):
            I=(2*W+1)*a
            r=observables(1.,float(N),I)
            assert abs(sum(r['k']))<1e-9
            assert abs(r['gaudin_min_eigenvalue']-N)<1e-9
            finite.append(dict(N=N,L=N,c=1.,W=W,I=I.tolist(),**r))
    files=('jump.py','response.py','two_body_cycle.py','test_response.py','test_cycle.py')
    payload=dict(status='Exact seam overlaps; conditional dephased endpoint; finite-N static branches',
                 python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
                 checks=checks,sha256={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in files},
                 jump_cases=rows,finite_N=finite)
    Path('jump_results.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(checks=checks,selected=[r for r in rows if r['cutoff']==256 and r['m']==0],
                          finite_N=[{k:r[k] for k in ('N','W','g2')} for r in finite]),indent=2))


if __name__=='__main__':
    main()
