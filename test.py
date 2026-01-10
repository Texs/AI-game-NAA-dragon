import unittest
from app import sum

class TestSumFunction(unittest.TestCase):
    
    def test_positive_numbers(self):
        """Test adding positive numbers"""
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(10, 15), 25)
        
    def test_negative_numbers(self):
        """Test adding negative numbers"""
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-5, -3), -8)
        self.assertEqual(sum(-10, 5), -5)
        
    def test_zero_values(self):
        """Test adding with zero"""
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(0, 5), 5)
        self.assertEqual(sum(7, 0), 7)
        
    def test_decimal_numbers(self):
        """Test adding decimal numbers (may have precision issues)"""
        # Note: Floating point precision might cause issues here
        self.assertAlmostEqual(sum(0.1, 0.2), 0.3, places=7)
        self.assertEqual(sum(1.5, 2.5), 4.0)
        
    def test_large_numbers(self):
        """Test adding large numbers"""
        self.assertEqual(sum(1000000, 2000000), 3000000)

if __name__ == "__main__":
    # Run the tests
    unittest.main()
