import unittest
import logging


class TestVectorSumAndTwoNorm(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger('simpleLogger')
        self.logger.info('Set up a test!')
        pass

    def tearDown(self):
        self.logger.info('Tear down a test.')
        pass

    def test_vector_one(self):
        from lib.twonorm import compute_two_norm
        from lib.vector_v0 import Vector
        self.logger.debug('Start a test.')
        self.vector = Vector(1, 2, 3, 4, 5)
        norm_value = compute_two_norm(self.vector)
        
        self.assertAlmostEqual(norm_value, 7.4161984871)  # 這也有問題？
        
        self.logger.debug('The calculated norm value = {}'.format(norm_value))
        self.logger.debug('Ends a test.')
        
        
    def test_vector_two(self):
        from lib.twonorm import compute_two_norm
        from lib.vector_v0 import Vector
        self.logger.debug('Start a test.')
        u = Vector(5, 4, 3, 2, 1)
        v = Vector(1, 2, 3, 4, 5)
        self.assertEqual(u + v, Vector(6, 6, 6, 6, 6))  # 這 Line 有問題？
        self.logger.debug('Ends a test.')
        pass
