# -*- coding: utf-8 -*-

import unittest

from core.finance.volatility.sigma import blind_rr_log

class TestSigma(unittest.TestCase):

    def setUp(self):
        self.array = []
        with open('table.csv', 'r') as fp:
            for line in fp:
                try:
                    close_p = float(line.split(',')[4])
                    assert close_p > 0.0
                    self.array.append(close_p)
                except:
                    continue

    def test_blind_rr_log(self):
        sigma = blind_rr_log(self.array)
        # TODO: Check the correct value
        self.assertEqual(sigma, 0)


if __name__ == '__main__':
    unittest.main()
