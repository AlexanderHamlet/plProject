import unittest
from ast import *
from eval import evaluate

class EvalTest(unittest.TestCase):

	def setUP(self):
		pass

	def test_plus(self):
		self.assertEqual(evaluate(Binary(Plus, N(5), N(10))), 15)

	def test_minus(self):
		self.assertEqual(evaluate(Binary(Minus, N(20), N(5))), 15)

	def test_times(self):
		self.assertEqual(evaluate(Binary(Times, N(5), N(3))), 15)

	def test_div(self):
		self.assertEqual(evaluate(Binary(Div, N(60), N(4))), 15)
		self.assertEqual(evaluate(Binary(Div, N(50), N(0))), 0)

	def test_neg(self):
		self.assertEqual(evaluate(Unary(Neg, N(15))), -15)

if __name__ == '__main__':
	unittest.main()

