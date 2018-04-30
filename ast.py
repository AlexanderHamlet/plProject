from collections import namedtuple

# Named tuples give us similar functionality to case classes in Scala

# --- Literals ---
N = namedtuple("N", ["n"])

# --- Operators ---
Unary = namedtuple("Unary", ["uop", "e1"])
Binary = namedtuple("Binary", ["bop", "e1", "e2"])

# Unary operators
class Neg: pass

# Binary operators
class Plus: pass
class Minus: pass
class Times: pass
class Div: pass

# Define a value
def isValue(e):
    if type(e) == N:
        return True
    else:
        return False