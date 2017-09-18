import unittest

import valid_triangle

class TaxiFareTests(unittest.TestCase):
    def test_valid_triangles(self):
        self.assertEqual(valid_triangle.valid_triangle(3, 3, 3), True)
        self.assertEqual(valid_triangle.valid_triangle(1, 2, 3), True)
        self.assertEqual(valid_triangle.valid_triangle(1, 2, 3), True)

        self.assertEqual(valid_triangle.valid_triangle(-1, 1, 1), True)
        self.assertEqual(valid_triangle.valid_triangle(-1, 1, -1), True)
        self.assertEqual(valid_triangle.valid_triangle(-1, -1, -1), True)
        
        
    def test_invalid_triangles(self):
        self.assertEqual(valid_triangle.valid_triangle(1, 2, 6), False)
        
if __name__ == '__main__':
    unittest.main()
