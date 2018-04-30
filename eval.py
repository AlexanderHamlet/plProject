from ast import *

# Big-step evaluation of expression e, an AST.
# Parameters:
#   e - AST node defined in ast.py
def evaluate(e):
	if type(e) == N:
		return e.n
	elif type(e) == Unary:
		if e.uop == Neg:
			return -evaluate(e.e1)
	elif type(e) == Binary:
		if e.bop == Plus:
			return evaluate(e.e1) + evaluate(e.e2)
		elif e.bop == Minus:
			return evaluate(e.e1) - evaluate(e.e2)
		elif e.bop == Times:
			return evaluate(e.e1) * evaluate(e.e2)
		elif e.bop == Div:
			e2 = evaluate(e.e2)
			if e2 == 0:
				return float('nan')
			else:
				return evaluate(e.e1) / e2