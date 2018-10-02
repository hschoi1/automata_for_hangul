
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftUNIONleftCONCATleftCLOSURESYMBOL UNION CLOSURE CONCAT LPAREN RPARENexpression : expression UNION expressionexpression : LPAREN expression RPARENexpression : expression CONCAT expressionexpression : expression CLOSUREexpression : termterm : SYMBOL'
    
_lr_action_items = {'UNION':([1,3,4,6,8,9,10,11,],[5,-5,-6,-4,5,-1,-3,-2,]),'LPAREN':([0,2,5,7,],[2,2,2,2,]),'$end':([1,3,4,6,9,10,11,],[0,-5,-6,-4,-1,-3,-2,]),'SYMBOL':([0,2,5,7,],[4,4,4,4,]),'CONCAT':([1,3,4,6,8,9,10,11,],[7,-5,-6,-4,7,7,-3,-2,]),'CLOSURE':([1,3,4,6,8,9,10,11,],[6,-5,-6,-4,6,6,6,-2,]),'RPAREN':([3,4,6,8,9,10,11,],[-5,-6,-4,11,-1,-3,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,5,7,],[1,8,9,10,]),'term':([0,2,5,7,],[3,3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression UNION expression','expression',3,'p_expression_union','yacc1.py',7),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_expr','yacc1.py',11),
  ('expression -> expression CONCAT expression','expression',3,'p_expression_concat','yacc1.py',15),
  ('expression -> expression CLOSURE','expression',2,'p_expression_closure','yacc1.py',19),
  ('expression -> term','expression',1,'p_expression_term','yacc1.py',23),
  ('term -> SYMBOL','term',1,'p_term_sym','yacc1.py',26),
]
