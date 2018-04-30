from ast import *
import re

# Based on the recursive descent parser tutorial here:
# http://blog.erezsh.com/how-to-write-a-calculator-in-70-python-lines-by-writing-a-recursive-descent-parser/

Token = namedtuple("Token", ["name", "val"])
TOKEN_MAP = {
    '+': "ADD",
    '-': "ADD",
    '*': "MULT",
    '/': "MULT",
    '(': "LPAREN",
    ')': "RPAREN"
}

# Tokenize the expression.
# Parameters:
#   e - str, the expression to tokenize
def tokenize(e):
    # Split into list of tokens
    split_e = re.findall("[\\d\\.]+|[{}]".format("\\" + "\\".join(TOKEN_MAP)), e)
    # Convert to token objects
    return [Token(TOKEN_MAP.get(tok, "N"), tok) for tok in split_e]

# BNF Grammar for our calculator:
# add:  add ADD mul | mul
# mul:  mul MULT atom | atom
# atom: NUM | '(' add ')' | neg
# neg:  '-' atom
# rule_map = {
#     'add' : ['mul ADD add', 'mul'],
#     'mul' : ['atom MUL mul', 'atom'],
#     'atom': ['NUM', 'LPAR add RPAR', 'neg'],
#     'neg' : ['ADD atom'],
# }