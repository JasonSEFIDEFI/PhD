import unittest
import numpy as np
from response import observables
from two_body_cycle import branch


class CycleTests(unittest.TestCase):
    def test_repulsive_matches_gaudin(self):
        for m in (0, 1, 2):
            for c in (.1, 1., 10.):
                a = branch(c, m=m)
                b = observables(c, 2., [-m-.5, m+.5])
                np.testing.assert_allclose(a['energy'], b['energy'], rtol=1e-10)
                np.testing.assert_allclose(a['g2'], b['g2'], rtol=1e-10)

    def test_attractive_wavefunction_and_derivative(self):
        for m in (0, 1, 2):
            for c in (-.1, -1., -10., -100.):
                a = branch(c, m=m)
                q = a['q']
                # Integral of squared relative wavefunction on [0,L], L=2.
                norm = 1+np.sin(2*q)/(2*q)
                direct = np.cos(q)**2/norm  # g2=L E'/4, E'=2 cos²/A
                np.testing.assert_allclose(a['g2'], direct, rtol=1e-9, atol=1e-12)
                h = abs(c)*1e-4
                fd = (branch(c+h,m=m)['q']-branch(c-h,m=m)['q'])/(2*h)
                np.testing.assert_allclose(a['dq_dc'], fd, rtol=2e-6)

    def test_branch_seams_and_free_contact(self):
        for m in (0, 1, 2):
            tg = (2*m+1)*np.pi/2
            np.testing.assert_allclose(branch(1e8,m=m)['q'], tg, rtol=3e-8)
            np.testing.assert_allclose(branch(-1e8,m=m)['q'], tg, rtol=3e-8)
            free = (m+1)*np.pi
            np.testing.assert_allclose(branch(-1e-7,m=m)['q'], free, rtol=1e-8)
            np.testing.assert_allclose(branch(1e-7,m=m+1)['q'], free, rtol=1e-8)
        self.assertAlmostEqual(branch(1e-7,m=0)['g2'], .5, delta=1e-7)
        self.assertAlmostEqual(branch(1e-7,m=1)['g2'], 1., delta=1e-7)

    def test_invalid(self):
        for c, length, m in ((0,2,0),(1,0,0),(1,2,-1),(1,2,.5)):
            with self.assertRaises(ValueError):
                branch(c,length,m)


if __name__ == '__main__':
    unittest.main(verbosity=2)
