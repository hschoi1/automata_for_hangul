import ply.yacc as yacc
import eNFA_to_mDFA
# Get the token map from the lexer.  This is required.
from lex1 import tokens

def p_expression_union(p):
    'expression : expression UNION expression'
    p[0]=('union',p[1],p[3])
    
def p_expression_expr(p):
    'expression : LPAREN expression RPAREN'
    p[0]=p[2]
    
def p_expression_concat(p):
    'expression : expression CONCAT expression'
    p[0]=('concatenation',p[1],p[3])
    
def p_expression_closure(p):
    'expression : expression CLOSURE'
    p[0]=('closure',p[1])
    
def p_expression_term(p):
    'expression : term'
    p[0]=('term',p[1])
def p_term_sym(p):
    'term : SYMBOL'
    p[0]=p[1]

precedence = (
    ('left', 'UNION'),
    ('left', 'CONCAT'),
    ('left','CLOSURE'),
)
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

inputsym=[]
s = input('regular expression: ')
alphabets='abcdefghijklmnopqrstuvwxyz'
for i in s:
    if i not in inputsym and i in alphabets:
        inputsym.append(i)

empty=False
if s=='':
    empty=True
   
if not empty:
    processed_s=s[0]
    for i in range(1,len(s)):
        if ((s[i-1] in [')','*'] or s[i-1] in 'abcdefghijklmnopqrstuvwxyz') and (s[i] =='(' or s[i] in 'abcdefghijklmnopqrstuvwxyz')):
            processed_s=processed_s+' '
            processed_s=processed_s+s[i]
        else:
            processed_s=processed_s+s[i]
    result = parser.parse(processed_s)
