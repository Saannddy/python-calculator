import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_addfunc(self):
        self.assertEqual(self.calc.add(-1,-2),-3)
        self.assertEqual(self.calc.add(-1,1),0)

    def test_subtractfunc(self):
        self.assertEqual(self.calc.subtract(-1,-2),1)
        self.assertEqual(self.calc.subtract(-1,-1),0)

    def test_multiplyfunc(self):
        self.assertEqual(self.calc.multiply(2,10),20)
        self.assertEqual(self.calc.multiply(-2,-3),6)
        self.assertEqual(self.calc.multiply(-2,3),-6)
    
    def test_dividefunc(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(-10,3),-3)
        self.assertEqual(self.calc.divide(-10,-2),5)

    def test_modulofunc(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)         
        self.assertEqual(self.calc.modulo(-10, 3), -1)   
        self.assertEqual(self.calc.modulo(5, 10), 5) 

if __name__ == '__main__':
    unittest.main(verbosity=2)