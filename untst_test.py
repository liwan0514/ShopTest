import unittest
from oose import Caa
class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("setup")
    def tearDown(self):
        print("teardown")
    def test_add(self):
        c = Caa(1,2)
        result = c.add()
        self.assertEqual(result,2)
if __name__ == '__main__':
    # unittest.main
    suit = unittest.TestCase()
    suit.addTest(TestCalculator("test_add"))
    runner = unittest.TextTestRunner()
    runner.run(suit)