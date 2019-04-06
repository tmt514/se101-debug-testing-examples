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
        vector = [3, 4]
        norm_value = compute_two_norm(vector)
        self.assertEqual(norm_value, 5)
        self.logger.debug('The calculated norm value = {}'.format(norm_value))
        self.logger.debug('Ends a test.')
        pass
