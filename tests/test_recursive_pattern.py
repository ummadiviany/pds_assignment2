import sys
sys.path.append('..')

import unittest
from tasks.recursive_pattern import print_pattern
from get_func_output import return_func_output

class TestRecursivePattern(unittest.TestCase):
    def test_pattern1_return(self):
        self.assertEqual(print_pattern(2,2), 4)
    
    def test_pattern1_print(self):
        self.assertEqual(return_func_output(print_pattern, 2, 2), "y^2*-z^2*-b^2*-a^3*-b^2*-z^2*-y^2\nx^4*-y^4*-z^4*-c^4*-b^4*-a^5*-b^4*-c^4*-z^4*-y^4*-x^4")
        
    def test_pattern2_return(self):
        self.assertEqual(print_pattern(3,3), 27)
    
    def test_pattern2_print(self):
        self.assertEqual(return_func_output(print_pattern, 3, 3), "y^3*-z^3*-b^3*-a^4*-b^3*-z^3*-y^3\nx^9*-y^9*-z^9*-c^9*-b^9*-a^10*-b^9*-c^9*-z^9*-y^9*-x^9\nw^27*-x^27*-y^27*-z^27*-d^27*-c^27*-b^27*-a^28*-b^27*-c^27*-d^27*-z^27*-y^27*-x^27*-w^27")
        
        

if __name__ == "__main__":
    unittest.main()