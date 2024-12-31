import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.qu = Queue(2)

    def test_is_empty(self):
        self.assertEqual(self.qu.is_empty(), True)
        self.qu.add_queue(10)
        self.assertEqual(self.qu.is_empty(), False)

    def test_is_full(self):
        self.assertEqual(self.qu.is_full(), False)
        self.qu.add_queue(10)
        self.qu.add_queue(11)
        self.assertEqual(self.qu.is_full(), True)