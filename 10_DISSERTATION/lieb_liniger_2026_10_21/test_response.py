"""Independent identities and finite-difference checks, not physical validation."""
import unittest
import numpy as np
from scipy.optimize import brentq
from response import gaudin, observables, quantum_numbers, solve


class ResponseTests(unittest.TestCase):
    def test_response_by_resolving(self):
        for n in (2, 3, 6):
            for spacing in (1, 3):
                q = quantum_numbers(n, spacing)
                for c in (0.1, 1., 10.):
                    with self.subTest(n=n, spacing=spacing, c=c):
                        h = c*1e-4
                        a = observables(c, float(n), q)
                        kp = solve(c+h, float(n), q)
                        km = solve(c-h, float(n), q)
                        np.testing.assert_allclose(a['dk_dc'], (kp-km)/(2*h), rtol=2e-6, atol=2e-9)
                        np.testing.assert_allclose(a['dE_dc'], (kp@kp-km@km)/(2*h), rtol=2e-6, atol=2e-8)
                        np.testing.assert_allclose(a['d2E_dc2'], (kp@kp-2*a['energy']+km@km)/h**2,
                                                   rtol=3e-3, atol=2e-4)

    def test_two_particle_wavefunction(self):
        length = 2.
        for c in (0.01, .1, 1., 10., 100.):
            k = brentq(lambda k: 2*k*np.tan(k*length/2)-c, 1e-12, np.pi/length-1e-12)
            # Independent normalization of cos(k(r-L/2)) on r in [0,L].
            ep = 2*np.cos(k*length/2)**2/(length/2+np.sin(k*length)/(2*k))
            a = observables(c, length, [-.5, .5])
            np.testing.assert_allclose(a['energy'], 2*k*k, rtol=1e-9)
            np.testing.assert_allclose(a['dE_dc'], ep, rtol=1e-9)

    def test_symmetry_boost_scaling(self):
        q = quantum_numbers(6, 3)
        c, length = 1.7, 6.
        a = observables(c, length, q)
        k = np.array(a['k'])
        g = gaudin(k, c, length)
        np.testing.assert_allclose(g@np.ones(6), length*np.ones(6), atol=1e-12)
        self.assertGreaterEqual(np.linalg.eigvalsh(g)[0], length-1e-12)
        self.assertAlmostEqual(sum(a['dk_dc']), 0., places=11)
        boost = 2*np.pi*2/length
        shifted = observables(c, length, q+2)
        np.testing.assert_allclose(shifted['k'], k+boost, atol=1e-11)
        self.assertAlmostEqual(shifted['g2'], a['g2'], places=10)
        scaled = observables(c/3, length*3, q)
        np.testing.assert_allclose(scaled['energy'], a['energy']/9, rtol=1e-10)
        np.testing.assert_allclose(scaled['contact_integrated'], a['contact_integrated']/27, rtol=1e-10)
        self.assertAlmostEqual(scaled['g2'], a['g2'], places=10)

    def test_limits(self):
        for n in (2, 3, 6):
            q = quantum_numbers(n)
            weak = observables(1e-5, float(n), q)
            self.assertAlmostEqual(weak['g2'], 1-1/n, delta=2e-5)
            for spacing in (1, 3):
                q = quantum_numbers(n, spacing)
                strong = observables(1e6, float(n), q)
                e_inf = float(np.sum((2*np.pi*q/n)**2))
                np.testing.assert_allclose(strong['energy'], e_inf, rtol=5e-6)
                # c^2 E' -> 4 N E_inf/L for centered fixed-I states.
                np.testing.assert_allclose(strong['contact_integrated'], 4*e_inf, rtol=2e-5)

    def test_single_particle_and_invalid_inputs(self):
        a = observables(1., 2., [1.])
        self.assertEqual(a['g2'], 0.)
        for c, length, q in ((0, 2, [-.5,.5]), (-1,2,[-.5,.5]),
                             (1,0,[-.5,.5]), (1,2,[0,1]), (1,2,[.5,.5])):
            with self.assertRaises(ValueError):
                solve(c, length, q)


if __name__ == '__main__':
    unittest.main(verbosity=2)
