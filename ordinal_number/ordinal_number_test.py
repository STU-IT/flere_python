import unittest

import ordinal_number

class TaxiFareTests(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(ordinal_number.ordinal_number(1), 'first')
        self.assertEqual(ordinal_number.ordinal_number(2), 'second')
        self.assertEqual(ordinal_number.ordinal_number(3), 'third')
        #...
        self.assertEqual(ordinal_number.ordinal_number(10), 'tenth')
        self.assertEqual(ordinal_number.ordinal_number(11), 'elleventh')
        self.assertEqual(ordinal_number.ordinal_number(12), 'twelfth')
        
        
        
        
    def test_invalid_numbers(self):
        self.assertEqual(ordinal_number.ordinal_number(0), '')
        self.assertEqual(ordinal_number.ordinal_number(1.5), '')
        self.assertEqual(ordinal_number.ordinal_number(-1), '')
        self.assertEqual(ordinal_number.ordinal_number(13), '')
        self.assertEqual(ordinal_number.ordinal_number(20), '')
        
        

if __name__ == '__main__':
    unittest.main()
