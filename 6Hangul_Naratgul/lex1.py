# -*- coding: utf-8 -*-
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'SYMBOL',
   'UNION',
   'CLOSURE',
   'CONCAT',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_UNION   = r'\+'
t_CLOSURE = r'\*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_SYMBOL(t):
    r'[^\s\+\*\)\(]' 
    return t

def t_CONCAT(t):
    r'(?<=.)\s(?=.)'
    return t
    
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# A string containing ignored characters (spaces and tabs)
#t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

