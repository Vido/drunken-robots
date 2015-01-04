# -*- coding: utf-8 -*-

import unittest

from VaR import CreditExposure
from VaR import monte_carlo_method

class MonteCarloVaR(unittest.TestCase):
    def setUp(self):
        """
            Portfolio from:
                CREDIT SUISSE | FIRST BOSTON
                CreditRisk+
                A Credit Risk Management Framework
            www.csfb.com/institutional/research/assets/creditrisk.pdf
                Appendix B
        """
        # EAD and PD come from the paper,  LGD is made up.
        self.exposure = [
            CreditExposure(358475.0,   0.30,  1.0),
            CreditExposure(1089819.0,  0.30,  1.0),
            CreditExposure(1799710.0,  0.10,  1.0),
            CreditExposure(1933116.0,  0.15,  1.0),
            CreditExposure(2317327.0,  0.15,  1.0),
            CreditExposure(2410929.0,  0.15,  1.0),
            CreditExposure(2652184.0,  0.30,  1.0),
            CreditExposure(2957685.0,  0.15,  1.0),
            CreditExposure(3137989.0,  0.05,  1.0),
            CreditExposure(3204044.0,  0.05,  1.0),
            CreditExposure(4727724.0,  0.015, 1.0),
            CreditExposure(4830517.0,  0.05,  1.0),
            CreditExposure(4912097.0,  0.05,  1.0),
            CreditExposure(4928989.0,  0.30,  1.0),
            CreditExposure(5042312.0,  0.10,  1.0),
            CreditExposure(5320364.0,  0.075, 1.0),
            CreditExposure(5435457.0,  0.05,  1.0),
            CreditExposure(5517586.0,  0.03,  1.0),
            CreditExposure(5764596.0,  0.075, 1.0),
            CreditExposure(5847845.0,  0.03,  1.0),
            CreditExposure(6466533.0,  0.30,  1.0),
            CreditExposure(6480322.0,  0.30,  1.0),
            CreditExposure(7727651.0,  0.016, 1.0),
            CreditExposure(15410906.0, 0.10,  0.5),
            CreditExposure(20238895.0, 0.075, 0.5),
        ]

    def test_var(self):
        VaR = monte_carlo_method(self.exposure)
        VaR = monte_carlo_method(self.exposure, alpha=0.99)
        VaR = monte_carlo_method(self.exposure, simulations=1000)
        VaR = monte_carlo_method(self.exposure, simulations=1000, alpha=0.99)

    def test_very_high_alpha(self):
        with self.assertRaises(Exception) as context:
            monte_carlo_method(self.exposure, simulations=1000, alpha=0.9999)
        mesg = 'Alpha is too big for given simulations.'
        self.assertEqual(context.exception.message, mesg)

    def test_sloppy_output(self):
        """
            VaR must be larger the the Expected Loss
            VaR must be less than the Aggregate Exposure
            This VaR must be less then CreditRisk+'s VaR,
                because it does not uses PD volatilities.

            99th Percentile: 55,311,503
            Aggregate Exposure: 130,513,072
            Expected Loss: 14,221,863
        """
        VaR = monte_carlo_method(self.exposure, simulations=100000)
        print "Var: ", VaR
        self.assertGreater(VaR, 14221863.0)

        VaR = monte_carlo_method(self.exposure, simulations=100000)
        print "Var: ", VaR
        self.assertLess(VaR, 55311503.0)

        VaR = monte_carlo_method(self.exposure, simulations=100000)
        print "Var: ", VaR
        self.assertLess(VaR, 130513503.0)


if __name__ == '__main__':
    unittest.main()

