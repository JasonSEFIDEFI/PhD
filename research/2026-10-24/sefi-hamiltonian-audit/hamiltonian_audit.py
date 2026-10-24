"""Allowed curvature-only SEFI realization: symbolic audit and local dynamics.

Units c=1. No empirical predictions or full-theory rejection are inferred.
"""
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import sympy as sp


def symbolic_check():
    v,a,S,w,P,pS,p,m,h,k,mu=sp.symbols('v a S w P pS p m h k mu', real=True)
    g=(1-v*v)**sp.Rational(-1,2)
    L=-m/g+h*g*w*w/2-k*S*S/(2*g)-mu*S*g**5*a*a
    av=-P/(2*mu*S*g**5)
    wv=pS/(h*g)
    H=p*v-P*P/(4*mu*S*g**5)+pS*pS/(2*h*g)+m/g+k*S*S/(2*g)
    identities={
        'highest_derivative_hessian':sp.diff(L,a,2)+2*mu*S*g**5,
        'momentum_P':sp.diff(L,a)+2*mu*S*g**5*a,
        'momentum_pS':sp.diff(L,w)-h*g*w,
        'Legendre_transform':(p*v+P*a+pS*w-L).subs({a:av,w:wv})-H,
        'velocity_inverse':sp.diff(H,P)-av,
        'identity_velocity_inverse':sp.diff(H,pS)-wv,
        'P_evolution':-sp.diff(H,v)-(-p-5*P*P*v/(4*mu*S*g**3)+(pS*pS/(2*h)+m+k*S*S/2)*g*v),
        'pS_evolution':-sp.diff(H,S)-(-P*P/(4*mu*S*S*g**5)-k*S/g),
    }
    results={name:str(sp.simplify(expr)) for name,expr in identities.items()}
    assert set(results.values())=={'0'}, results
    # Check the parametrized theory's reparametrization constraints explicitly.
    u0,u1,b0,b1,j=sp.symbols('u0 u1 b0 b1 j',real=True)
    n=sp.sqrt(u0*u0-u1*u1)
    D=u0*b1-u1*b0
    Lpar=-m*n+h*w*w/(2*n)-k*S*S*n/2-mu*S*D*D/n**5
    subs={u0:1,u1:v,b0:0,b1:a}
    Pi0=sp.diff(Lpar,b0).subs(subs)
    Pi1=sp.diff(Lpar,b1).subs(subs)
    dt=lambda f:sp.diff(f,v)*a+sp.diff(f,a)*j+sp.diff(f,S)*w
    px=sp.diff(Lpar,u1).subs(subs)-dt(Pi1)
    pt=sp.diff(Lpar,u0).subs(subs)-dt(Pi0)
    residuals={
        'parametrized_acceleration_Hessian_determinant':sp.hessian(Lpar,(b0,b1)).det(),
        'primary_reparametrization_constraint':Pi0+v*Pi1,
        'secondary_constraint_fixes_pt':pt+px*v+Pi1*a+h*g*w*w-L,
        'px_jerk_coefficient':sp.diff(px,j)-2*mu*S*g**5,
    }
    extra={name:str(sp.simplify(expr)) for name,expr in residuals.items()}
    assert set(extra.values())=={'0'},extra
    results.update(extra)
    return results


def energy(z, mu=1.,m=1.,h=1.,k=1.):
    x,v,S,p,P,pS=np.asarray(z)
    g=1/np.sqrt(1-v*v)
    return p*v-P*P/(4*mu*S*g**5)+pS*pS/(2*h*g)+m/g+k*S*S/(2*g)


def flow(t,z,mu=1.,m=1.,h=1.,k=1.):
    x,v,S,p,P,pS=z
    g=1/np.sqrt(1-v*v)
    return np.array([v,-P/(2*mu*S*g**5),pS/(h*g),0.,
                     -p-5*P*P*v/(4*mu*S*g**3)+(pS*pS/(2*h)+m+k*S*S/2)*g*v,
                     -P*P/(4*mu*S*S*g**5)-k*S/g])


def run_local():
    # All starts are timelike, nonzero curvature, and away from S=0.
    rows=[]
    for S0 in (1.,-1.):
        z0=np.array([0.,.2,S0,0.3,.2,.1])
        sol=[]
        for rtol in (1e-8,1e-10,1e-12):
            r=solve_ivp(flow,(0.,.3),z0,method='DOP853',rtol=rtol,atol=rtol*.01,
                        t_eval=np.linspace(0.,.3,101),max_step=.03)
            assert r.success, r.message
            assert np.max(np.abs(r.y[1]))<.95 and np.min(np.abs(r.y[2]))>.5
            assert np.min(np.abs(r.y[4]))>.01
            err=float(np.max(np.abs(energy(r.y)-energy(z0))))
            assert err<1e-7
            sol.append(r.y[:,-1])
            rows.append(dict(S0=S0,rtol=rtol,energy_initial=float(energy(z0)),
                             energy_drift=err,max_speed=float(np.max(np.abs(r.y[1]))),
                             min_abs_S=float(np.min(np.abs(r.y[2]))),
                             final=r.y[:,-1].tolist()))
        assert np.max(np.abs(sol[-1]-sol[-2]))<1e-8
    return rows


def finite_difference_checks():
    rng=np.random.default_rng(24102026)
    maximum=0.
    for _ in range(100):
        z=rng.normal(size=6)
        z[1]=rng.uniform(-.7,.7)
        z[2]=rng.choice([-1,1])*rng.uniform(.5,2.)
        eps=1e-6
        grad=np.array([(energy(z+eps*np.eye(6)[i])-energy(z-eps*np.eye(6)[i]))/(2*eps) for i in range(6)])
        expected=np.r_[grad[3:],-grad[:3]]
        err=np.max(np.abs(flow(0,z)-expected))
        maximum=max(maximum,float(err))
        assert err<1e-7
        # Independent identity E-L equation in proper time.
        dz=flow(0,z); v,S,P,pS=z[1],z[2],z[4],z[5]
        g=1/np.sqrt(1-v*v)
        a,w=dz[1],dz[2]
        wdot=dz[5]/g-pS*g*v*a
        proper_second=g*g*wdot+g**4*v*a*w
        assert abs(proper_second+S+g**6*a*a)<1e-10
    return dict(seed=24102026,cases=100,max_Hamilton_gradient_error=maximum)


def witnesses():
    rows=[]
    # Fixed finite curvature and all other physical jets through second order;
    # change p, which corresponds to the otherwise free third derivative.
    for sign in (1.,-1.):
        for magnitude in (1.,10.,100.,1000.):
            z=np.array([0.,.2,sign,-magnitude,.2,.1])
            rows.append(dict(S=sign,p=-magnitude,H=float(energy(z)),
                             speed=z[1],proper_curvature=float(abs(flow(0,z)[1])/(1-z[1]**2)**1.5)))
    assert rows[3]['H']<rows[2]['H']<rows[1]['H']<rows[0]['H']
    assert rows[7]['H']<rows[6]['H']<rows[5]['H']<rows[4]['H']
    return rows


def old_claims():
    # Exact counterexamples, reported as rational/symbolic identities.
    t=sp.symbols('t',real=True)
    O=sp.sin(t)
    acceleration=sp.diff(O,t,2).subs(t,0)
    jerk=sp.diff(O,t,3).subs(t,0)
    assert acceleration==0 and jerk==-1
    lam,K,S=sp.symbols('lambda K S',real=True)
    frozen=sp.diff(lam*K*K*S,K)
    assert frozen==2*lam*K*S
    return dict(acceleration_zero_at_crossing=str(acceleration),jerk_at_crossing=str(jerk),
                frozen_identity_geometric_coupling=str(frozen),
                status='Older DEFI implications fail; newer foundations already acknowledges both')


def main():
    result=dict(scope='Curvature-only allowed parameter subfamily, local timelike regular domain',
                units='c=1; numerical m=h=k=mu=1',python=platform.python_version(),
                numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,
                symbolic_identities=symbolic_check(),finite_difference_checks=finite_difference_checks(),
                local_integrations=run_local(),unbounded_energy_witnesses=witnesses(),
                older_claim_counterexamples=old_claims(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path('hamiltonian_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
