from ast import *
from collections import namedtuple
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
# add:  mult ADD add | mult
# mult:  atom MULT mult | atom
# atom: NUM | '(' add ')' | ADD atom

# ParseResult Objects just like in Lab 6
Success = namedtuple("Success", ["ast", "next"])
Failure = namedtuple("Failure", ["message", "next"])

def parse(expr):
    toks = tokenize(expr)
    return parse_toks(toks)

# Here, nxt is a list of tokens
def parse_toks(nxt):
    result = add(nxt)
    if type(result) == Success and not result.next: # No more input
        return result.ast
    elif type(result) == Success:
        raise Exception("remaining input")
    else:
        raise Exception(result.message)

def add(nxt):
    result = mult(nxt)
    if type(result) == Success:
        nxt = result.next
        if not nxt:
            return Success(result.ast, result.next)
        elif nxt[0].name == "ADD":
            bop = Plus if nxt[0].val == '+' else Minus
            result2 = add(nxt[1:])
            if type(result2) == Success:
                return Success(Binary(bop, result.ast, result2.ast), result2.next) # Continue with add nodes
            else:
                return Failure("expected add", nxt)
        elif nxt[0].name == "RPAREN":
            return Success(result.ast, result.next)
        else:
            return Failure("expected add", nxt)
    else:
        return Failure(result.message, nxt)

def mult(nxt):
    result = atom(nxt)
    if type(result) == Success:
        nxt = result.next
        if not nxt:
            return Success(result.ast, result.next)
        if nxt[0].name == "MULT":
            bop = Times if nxt[0].val == '*' else Div
            result2 = mult(nxt[1:])
            if type(result2) == Success:
                return Success(Binary(bop, result.ast, result2.ast), result2.next)
            else:
                return Failure("expected mult", nxt)
        else:
            return Success(result.ast, result.next)
    else:
        return Failure(result.message, nxt)

def atom(nxt):
    if not nxt:
        return Failure("expected atom", nxt)
    else:
        if nxt[0].name == "N":
            return Success(N(float(nxt[0].val)), nxt[1:])
        elif nxt[0].name == "ADD":
            if nxt[0].val == '+':
                return atom(nxt[1:]) # Ignore plus unary ops
            else:
                result = atom(nxt[1:])
                if type(result) == Success:
                    return Success(Unary(Neg, result.ast), result.next)
                else:
                    return Failure(result.message, nxt)
        elif nxt[0].name == "LPAREN":
            if len(nxt) < 2: return Failure("expected add", nxt)
            result = add(nxt[1:])
            if type(result) == Success:
                if result.next[0].name == "RPAREN":
                    return Success(result.ast, result.next[1:])
                else:
                    return Failure("expected )", result.next)
            else:
                return Failure(result.message, nxt)
        else:
            return Failure("expected atom", nxt)

e = input("> ")
print(parse(e))