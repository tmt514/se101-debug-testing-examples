import unittest
import logging


class TestAdd(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger('simpleLogger')
        self.logger.info('Set up a test!')
        pass

    def tearDown(self):
        self.logger.info('Tear down a test.')
        pass

    def test_hello_world(self):
        self.logger.debug('Start a test.')
        a = 3
        b = 4
        self.assertEqual(a + b, 7)
        self.logger.debug('Ends a test.')
        pass
