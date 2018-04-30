import unittest
from ast import *
from eval import evaluate
import math
from custom_parser import parse

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
		self.assertTrue(math.isnan(evaluate(Binary(Div, N(50), N(0)))))

	def test_neg(self):
		self.assertEqual(evaluate(Unary(Neg, N(15))), -15)
	
	def test_recurse(self):
		self.assertEqual(evaluate(Binary(Plus, Binary(Times, N(2), N(3)), N(4))), 10)
		self.assertEqual(evaluate(Binary(Plus, N(2), Binary(Times,N(3), N(4)))), 14)
	
class ParseTest(unittest.TestCase):
	def setUp(self):
		pass

	def test_atom(self):
		self.assertEqual(parse("2"), N(2))
	
	def test_mult(self):
		self.assertEqual(parse("1*3"), Binary(Times, N(1), N(3)))
		self.assertEqual(parse("1/3"), Binary(Div, N(1), N(3)))
	
	def test_add(self):
		self.assertEqual(parse("1+3"), Binary(Plus, N(1), N(3)))
		self.assertEqual(parse("1-3"), Binary(Minus, N(1), N(3)))
	
	def test_operator_precedence(self):
		self.assertEqual(parse("2+1*3"), Binary(Plus, N(2), Binary(Times, N(1), N(3))))
	
	def test_parentheses(self):
		self.assertEqual(parse("(2+1)*3"), Binary(Times, Binary(Plus, N(2), N(1)), N(3)))
	
	def test_failure_add(self):
		with self.assertRaises(Exception):
			parse("2+")
	
	def test_failure_mult(self):
		with self.assertRaises(Exception):
			parse("2*")
	
	def test_failure_atom(self):
		with self.assertRaises(Exception):
			parse("idk")
	
	def test_failure_parentheses(self):
		with self.assertRaises(Exception):
			parse("2+(3*5")

if __name__ == '__main__':
	unittest.main()

