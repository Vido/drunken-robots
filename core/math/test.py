# -*- coding: utf-8 -*-

import unittest

from statistics import ordinary_least_squares
from statistics import alt_ordinary_least_squares

class OLS(unittest.TestCase):
    def setUp(self):
        # http://en.wikipedia.org/wiki/Simple_linear_regression
        self.height = [
            1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70,
            1.73, 1.75, 1.78, 1.80, 1.83,
        ]
        self.weight = [
            52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11,
            64.47, 66.28, 68.10, 69.92, 72.19, 74.46,
        ]

        self.beta = 61.272
        self.alpha = -39.062

    def test_alpha_beta(self):
        alpha, beta = ordinary_least_squares(self.height, self.weight)
        self.assertAlmostEqual(alpha, self.alpha, places=2)
        self.assertAlmostEqual(beta, self.beta, places=2)

    @unittest.skip("the 'alt' method is not right")
    def test_alt_alpha_beta(self):
        alpha, beta = alt_ordinary_least_squares(self.height, self.weight)
        self.assertAlmostEqual(alpha, self.alpha, places=2)
        self.assertAlmostEqual(beta, self.beta, places=2)


if __name__ == '__main__':
    unittest.main()

