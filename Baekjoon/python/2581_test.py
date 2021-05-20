import unittest
from prime_sum import f_2581

class SimpleTest(unittest.TestCase):
    def testResult1(self):
        self.assertEqual(f_2581(60, 100), (620, 61))

if __name__ == '__main__':
    unittest.main()
