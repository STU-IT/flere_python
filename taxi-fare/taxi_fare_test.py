import unittest

import taxi_fare

class TaxiFareTests(unittest.TestCase):
    def test_gode_positive_stræninger(self):
        self.assertEqual(taxi_fare.taxi_fare(1), 5.785714285714286)
        self.assertEqual(taxi_fare.taxi_fare(10), 21.857142857142854)
        self.assertEqual(taxi_fare.taxi_fare(3.36), 10)
        
        
    def test_grænse_strækninger(self):
        self.assertEqual(taxi_fare.taxi_fare(0), 4)
        self.assertEqual(taxi_fare.taxi_fare(0.01), 4.017857142857143)

    def test_negative_strækninger(self):
        self.assertEqual(taxi_fare.taxi_fare(-0), 4)
        self.assertEqual(taxi_fare.taxi_fare(-1), 4)
        self.assertEqual(taxi_fare.taxi_fare(-10), 4)
        self.assertEqual(taxi_fare.taxi_fare(-3.36), 4)
        self.assertEqual(taxi_fare.taxi_fare(-0.01), 4)

if __name__ == '__main__':
    unittest.main()
