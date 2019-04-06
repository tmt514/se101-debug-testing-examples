import unittest
import logging


class TestComputeTwoNorm(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger('simpleLogger')
        self.logger.info('Set up a test!')
        pass

    def tearDown(self):
        self.logger.info('Tear down a test.')
        pass

    def test_vector_one(self):
        from lib.twonorm import compute_two_norm
        self.logger.debug('Start a test.')
        self.vector = [1, 2, 3, 4, 5]
        norm_value = compute_two_norm(self.vector)
        
        self.assertEqual(norm_value, 7.4161984871)  # 這邊有問題？
        
        self.logger.debug('The calculated norm value = {}'.format(norm_value))
        self.logger.debug('Ends a test.')
        pass
