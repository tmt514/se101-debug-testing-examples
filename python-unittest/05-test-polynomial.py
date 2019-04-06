import unittest
import logging


class TestPolynomial(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger('simpleLogger')
        self.logger.info('Set up a test!')
        pass

    def tearDown(self):
        self.logger.info('Tear down a test.')
        pass

    def test_polynomial_evaluation(self):
        from lib.polynomial import Polynomial
        self.logger.debug('Start a test.')
        f = Polynomial(3, 2, 1) # x^2 + 2x + 3
        f0 = f(0)
        f1 = f(1)
        self.assertEqual(f0, 3)
        self.assertEqual(f1, 6)
        
        self.logger.debug('f(0) = {}, f(1) = {}'.format(f0, f1))
        self.logger.debug('Ends a test.')
        