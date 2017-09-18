import unittest
import math

import hypotenuse

class HypotenuseTests(unittest.TestCase):
    def test_pytagoraeiske_talsaet(self):
        self.assertEqual(hypotenuse.hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse.hypotenuse(5, 12), 13)

    def test_negative_kateter(self):
        self.assertEqual(hypotenuse.hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse.hypotenuse(5, -12), 13)
        self.assertEqual(hypotenuse.hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse.hypotenuse(-5, -12), 13)

    def test_irrationelle_hypertenuser(self):
        self.assertEqual(hypotenuse.hypotenuse(2, 3), math.sqrt(13))
        self.assertEqual(hypotenuse.hypotenuse(1, 1), math.sqrt(2))

if __name__ == '__main__':
    unittest.main()
