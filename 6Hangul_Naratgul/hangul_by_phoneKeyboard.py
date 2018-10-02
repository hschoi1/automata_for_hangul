# -*- coding: utf-8 -*-
from __future__ import print_function
import ply.yacc as yacc
from yacc1 import*
import os
import ply.lex as lex
from lex1 import tokens
from Reg_to_mDFA import*
NRG_to_Hangul={'1':'ㄱ','2':'ㄴ','3':'ㅏ','q':'ㄹ','w':'ㅁ','e':'ㅗ','a':'ㅅ','s':'ㅇ','d':'ㅣ','z':'획','x':'ㅡ','c':'쌍'}
NRGcons={'ㄱ':'ㄱ','ㄱ획':'ㅋ','ㄴ':'ㄴ','ㄴ획':'ㄷ','ㄴ획획':'ㅌ','ㄹ':'ㄹ','ㅁ':'ㅁ','ㅁ획':'ㅂ','ㅁ획획':'ㅍ','ㅅ':'ㅅ','ㅅ획':'ㅈ','ㅅ획획':'ㅊ','ㅇ':'ㅇ','ㅇ획':'ㅎ','ㄱ쌍':'ㄲ','ㄴ획쌍':'ㄸ','ㅁ획쌍':'ㅃ','ㅅ쌍':'ㅆ','ㅅ획쌍':'ㅉ'}
NRGvow={'ㅏ':'ㅏ','ㅏㅣ':'ㅐ','ㅏ획':'ㅑ','ㅏ획ㅣ':'ㅒ','ㅏㅏ':'ㅓ','ㅏㅏㅣ':'ㅔ','ㅏㅏ획':'ㅕ','ㅏㅏ획ㅣ':'ㅖ','ㅗ':'ㅗ','ㅗ획':'ㅛ','ㅗㅗ':'ㅜ','ㅗㅗ획':'ㅠ','ㅗㅏ':'ㅘ','ㅗㅏㅣ':'ㅙ','ㅗㅣ':'ㅚ','ㅗㅗㅏ':'ㅝ','ㅗㅗㅏㅣ':'ㅞ','ㅜㅣ':'ㅟ','ㅡ':'ㅡ','ㅡㅣ':'ㅢ','ㅣ':'ㅣ'}
NRGlowcons={'ㄱ':'ㄱ','ㄱ획':'ㅋ','ㄴ':'ㄴ','ㄴ획':'ㄷ','ㄴ획획':'ㅌ','ㄹ':'ㄹ','ㅁ':'ㅁ','ㅁ획':'ㅂ','ㅁ획획':'ㅍ','ㅅ':'ㅅ','ㅅ획':'ㅈ','ㅅ획획':'ㅊ','ㅇ':'ㅇ','ㅇ획':'ㅎ','ㄱ쌍':'ㄲ','ㅅ쌍':'ㅆ','ㄱㅅ':'ㄳ','ㄴㅅ획':'ㄵ','ㄴㅇ획':'ㄶ','ㄹㄱ':'ㄺ','ㄹㅁ':'ㄻ','ㄹㅁ획':'ㄼ','ㄹㅅ':'ㄽ','ㄹㄴ획획':'ㄾ',
              'ㄹㅁ획획':'ㄿ','ㄹㅇ획':'ㅀ','ㅁ획ㅅ':'ㅄ'}
v=['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅐ','ㅒ','ㅔ','ㅖ']
trans_fct={('q0', 'ㄱ'): 'q2', ('q0', 'ㄴ'): 'q15', ('q0', 'ㅏ'): 'q12', ('q0', 'ㄹ'): 'q3', ('q0', 'ㅁ'): 'q16', ('q0', 'ㅗ'): 'q10', ('q0', 'ㅅ'): 'q8', ('q0', 'ㅇ'): 'q17', ('q0', 'ㅣ'): 'q9', ('q0', 'ㅡ'): 'q5', ('q0', '획'): 'q9', ('q0', '쌍'): 'q5', ('q1', 'ㄱ'): 'q5', ('q1', 'ㄴ'): 'q5', ('q1', 'ㅏ'): 'q7', ('q1', 'ㄹ'): 'q5', ('q1', 'ㅁ'): 'q5', ('q1', 'ㅗ'): 'q0', ('q1', 'ㅅ'): 'q5', ('q1', 'ㅇ'): 'q5', ('q1', 'ㅣ'): 'q9', ('q1', 'ㅡ'): 'q12', ('q1', '획'): 'q13', ('q1', '쌍'): 'q5', ('q2', 'ㄱ'): 'q27', ('q2', 'ㄴ'): 'q21', ('q2', 'ㅏ'): 'q7', ('q2', 'ㄹ'): 'q19', ('q2', 'ㅁ'): 'q21', ('q2', 'ㅗ'): 'q0', ('q2', 'ㅅ'): 'q20', ('q2', 'ㅇ'): 'q26', ('q2', 'ㅣ'): 'q9', ('q2', 'ㅡ'): 'q12', ('q2', '획'): 'q13', ('q2', '쌍'): 'q13', ('q3', 'ㄱ'): 'q25', ('q3', 'ㄴ'): 'q11', ('q3', 'ㅏ'): 'q7', ('q3', 'ㄹ'): 'q19', ('q3', 'ㅁ'): 'q18', ('q3', 'ㅗ'): 'q0', ('q3', 'ㅅ'): 'q20', ('q3', 'ㅇ'): 'q1', ('q3', 'ㅣ'): 'q9', ('q3', 'ㅡ'): 'q12', ('q3', '획'): 'q5', ('q3', '쌍'): 'q5', ('q4', 'ㄱ'): 'q2', ('q4', 'ㄴ'): 'q15', ('q4', 'ㅏ'): 'q5', ('q4', 'ㄹ'): 'q3', ('q4', 'ㅁ'): 'q16', ('q4', 'ㅗ'): 'q5', ('q4', 'ㅅ'): 'q8', ('q4', 'ㅇ'): 'q17', ('q4', 'ㅣ'): 'q9', ('q4', 'ㅡ'): 'q5', ('q4', '획'): 'q12', ('q4', '쌍'): 'q5', ('q5', 'ㄱ'): 'q5', ('q5', 'ㄴ'): 'q5', ('q5', 'ㅏ'): 'q5', ('q5', 'ㄹ'): 'q5', ('q5', 'ㅁ'): 'q5', ('q5', 'ㅗ'): 'q5', ('q5', 'ㅅ'): 'q5', ('q5', 'ㅇ'): 'q5', ('q5', 'ㅣ'): 'q5', ('q5', 'ㅡ'): 'q5', ('q5', '획'): 'q5', ('q5', '쌍'): 'q5', ('q6', 'ㄱ'): 'q27', ('q6', 'ㄴ'): 'q21', ('q6', 'ㅏ'): 'q5', ('q6', 'ㄹ'): 'q19', ('q6', 'ㅁ'): 'q21', ('q6', 'ㅗ'): 'q5', ('q6', 'ㅅ'): 'q24', ('q6', 'ㅇ'): 'q26', ('q6', 'ㅣ'): 'q5', ('q6', 'ㅡ'): 'q5', ('q6', '획'): 'q5', ('q6', '쌍'): 'q5', ('q7', 'ㄱ'): 'q2', ('q7', 'ㄴ'): 'q15', ('q7', 'ㅏ'): 'q4', ('q7', 'ㄹ'): 'q3', ('q7', 'ㅁ'): 'q16', ('q7', 'ㅗ'): 'q5', ('q7', 'ㅅ'): 'q8', ('q7', 'ㅇ'): 'q17', ('q7', 'ㅣ'): 'q9', ('q7', 'ㅡ'): 'q5', ('q7', '획'): 'q12', ('q7', '쌍'): 'q5', ('q8', 'ㄱ'): 'q27', ('q8', 'ㄴ'): 'q21', ('q8', 'ㅏ'): 'q7', ('q8', 'ㄹ'): 'q19', ('q8', 'ㅁ'): 'q21', ('q8', 'ㅗ'): 'q0', ('q8', 'ㅅ'): 'q24', ('q8', 'ㅇ'): 'q26', ('q8', 'ㅣ'): 'q9', ('q8', 'ㅡ'): 'q12', ('q8', '획'): 'q23', ('q8', '쌍'): 'q13', ('q9', 'ㄱ'): 'q2', ('q9', 'ㄴ'): 'q15', ('q9', 'ㅏ'): 'q5', ('q9', 'ㄹ'): 'q3', ('q9', 'ㅁ'): 'q16', ('q9', 'ㅗ'): 'q5', ('q9', 'ㅅ'): 'q8', ('q9', 'ㅇ'): 'q17', ('q9', 'ㅣ'): 'q5', ('q9', 'ㅡ'): 'q5', ('q9', '획'): 'q5', ('q9', '쌍'): 'q5', ('q10', 'ㄱ'): 'q2', ('q10', 'ㄴ'): 'q15', ('q10', 'ㅏ'): 'q12', ('q10', 'ㄹ'): 'q3', ('q10', 'ㅁ'): 'q16', ('q10', 'ㅗ'): 'q5', ('q10', 'ㅅ'): 'q8', ('q10', 'ㅇ'): 'q17', ('q10', 'ㅣ'): 'q5', ('q10', 'ㅡ'): 'q5', ('q10', '획'): 'q9', ('q10', '쌍'): 'q5', ('q11', 'ㄱ'): 'q5', ('q11', 'ㄴ'): 'q5', ('q11', 'ㅏ'): 'q7', ('q11', 'ㄹ'): 'q5', ('q11', 'ㅁ'): 'q5', ('q11', 'ㅗ'): 'q0', ('q11', 'ㅅ'): 'q5', ('q11', 'ㅇ'): 'q5', ('q11', 'ㅣ'): 'q9', ('q11', 'ㅡ'): 'q12', ('q11', '획'): 'q28', ('q11', '쌍'): 'q5', ('q12', 'ㄱ'): 'q2', ('q12', 'ㄴ'): 'q15', ('q12', 'ㅏ'): 'q5', ('q12', 'ㄹ'): 'q3', ('q12', 'ㅁ'): 'q16', ('q12', 'ㅗ'): 'q5', ('q12', 'ㅅ'): 'q8', ('q12', 'ㅇ'): 'q17', ('q12', 'ㅣ'): 'q9', ('q12', 'ㅡ'): 'q5', ('q12', '획'): 'q5', ('q12', '쌍'): 'q5', ('q13', 'ㄱ'): 'q27', ('q13', 'ㄴ'): 'q21', ('q13', 'ㅏ'): 'q7', ('q13', 'ㄹ'): 'q19', ('q13', 'ㅁ'): 'q21', ('q13', 'ㅗ'): 'q0', ('q13', 'ㅅ'): 'q24', ('q13', 'ㅇ'): 'q26', ('q13', 'ㅣ'): 'q9', ('q13', 'ㅡ'): 'q12', ('q13', '획'): 'q5', ('q13', '쌍'): 'q5', ('q14', 'ㄱ'): 'q27', ('q14', 'ㄴ'): 'q21', ('q14', 'ㅏ'): 'q7', ('q14', 'ㄹ'): 'q19', ('q14', 'ㅁ'): 'q21', ('q14', 'ㅗ'): 'q0', ('q14', 'ㅅ'): 'q20', ('q14', 'ㅇ'): 'q26', ('q14', 'ㅣ'): 'q9', ('q14', 'ㅡ'): 'q12', ('q14', '획'): 'q13', ('q14', '쌍'): 'q19', ('q15', 'ㄱ'): 'q27', ('q15', 'ㄴ'): 'q21', ('q15', 'ㅏ'): 'q7', ('q15', 'ㄹ'): 'q19', ('q15', 'ㅁ'): 'q21', ('q15', 'ㅗ'): 'q0', ('q15', 'ㅅ'): 'q22', ('q15', 'ㅇ'): 'q1', ('q15', 'ㅣ'): 'q9', ('q15', 'ㅡ'): 'q12', ('q15', '획'): 'q23', ('q15', '쌍'): 'q5', ('q16', 'ㄱ'): 'q27', ('q16', 'ㄴ'): 'q21', ('q16', 'ㅏ'): 'q7', ('q16', 'ㄹ'): 'q19', ('q16', 'ㅁ'): 'q21', ('q16', 'ㅗ'): 'q0', ('q16', 'ㅅ'): 'q24', ('q16', 'ㅇ'): 'q26', ('q16', 'ㅣ'): 'q9', ('q16', 'ㅡ'): 'q12', ('q16', '획'): 'q14', ('q16', '쌍'): 'q5', ('q17', 'ㄱ'): 'q27', ('q17', 'ㄴ'): 'q21', ('q17', 'ㅏ'): 'q7', ('q17', 'ㄹ'): 'q19', ('q17', 'ㅁ'): 'q21', ('q17', 'ㅗ'): 'q0', ('q17', 'ㅅ'): 'q24', ('q17', 'ㅇ'): 'q26', ('q17', 'ㅣ'): 'q9', ('q17', 'ㅡ'): 'q12', ('q17', '획'): 'q13', ('q17', '쌍'): 'q5', ('q18', 'ㄱ'): 'q27', ('q18', 'ㄴ'): 'q21', ('q18', 'ㅏ'): 'q7', ('q18', 'ㄹ'): 'q19', ('q18', 'ㅁ'): 'q21', ('q18', 'ㅗ'): 'q0', ('q18', 'ㅅ'): 'q24', ('q18', 'ㅇ'): 'q26', ('q18', 'ㅣ'): 'q9', ('q18', 'ㅡ'): 'q12', ('q18', '획'): 'q23', ('q18', '쌍'): 'q5', ('q19', 'ㄱ'): 'q5', ('q19', 'ㄴ'): 'q5', ('q19', 'ㅏ'): 'q7', ('q19', 'ㄹ'): 'q5', ('q19', 'ㅁ'): 'q5', ('q19', 'ㅗ'): 'q0', ('q19', 'ㅅ'): 'q5', ('q19', 'ㅇ'): 'q5', ('q19', 'ㅣ'): 'q9', ('q19', 'ㅡ'): 'q12', ('q19', '획'): 'q5', ('q19', '쌍'): 'q5', ('q20', 'ㄱ'): 'q27', ('q20', 'ㄴ'): 'q21', ('q20', 'ㅏ'): 'q7', ('q20', 'ㄹ'): 'q19', ('q20', 'ㅁ'): 'q21', ('q20', 'ㅗ'): 'q0', ('q20', 'ㅅ'): 'q24', ('q20', 'ㅇ'): 'q26', ('q20', 'ㅣ'): 'q9', ('q20', 'ㅡ'): 'q12', ('q20', '획'): 'q27', ('q20', '쌍'): 'q19', ('q21', 'ㄱ'): 'q5', ('q21', 'ㄴ'): 'q5', ('q21', 'ㅏ'): 'q7', ('q21', 'ㄹ'): 'q5', ('q21', 'ㅁ'): 'q5', ('q21', 'ㅗ'): 'q0', ('q21', 'ㅅ'): 'q5', ('q21', 'ㅇ'): 'q5', ('q21', 'ㅣ'): 'q9', ('q21', 'ㅡ'): 'q12', ('q21', '획'): 'q27', ('q21', '쌍'): 'q5', ('q22', 'ㄱ'): 'q5', ('q22', 'ㄴ'): 'q5', ('q22', 'ㅏ'): 'q7', ('q22', 'ㄹ'): 'q5', ('q22', 'ㅁ'): 'q5', ('q22', 'ㅗ'): 'q0', ('q22', 'ㅅ'): 'q5', ('q22', 'ㅇ'): 'q5', ('q22', 'ㅣ'): 'q9', ('q22', 'ㅡ'): 'q12', ('q22', '획'): 'q25', ('q22', '쌍'): 'q19', ('q23', 'ㄱ'): 'q27', ('q23', 'ㄴ'): 'q21', ('q23', 'ㅏ'): 'q7', ('q23', 'ㄹ'): 'q19', ('q23', 'ㅁ'): 'q21', ('q23', 'ㅗ'): 'q0', ('q23', 'ㅅ'): 'q24', ('q23', 'ㅇ'): 'q26', ('q23', 'ㅣ'): 'q9', ('q23', 'ㅡ'): 'q12', ('q23', '획'): 'q13', ('q23', '쌍'): 'q19', ('q24', 'ㄱ'): 'q5', ('q24', 'ㄴ'): 'q5', ('q24', 'ㅏ'): 'q7', ('q24', 'ㄹ'): 'q5', ('q24', 'ㅁ'): 'q5', ('q24', 'ㅗ'): 'q0', ('q24', 'ㅅ'): 'q5', ('q24', 'ㅇ'): 'q5', ('q24', 'ㅣ'): 'q9', ('q24', 'ㅡ'): 'q12', ('q24', '획'): 'q27', ('q24', '쌍'): 'q19', ('q25', 'ㄱ'): 'q27', ('q25', 'ㄴ'): 'q21', ('q25', 'ㅏ'): 'q7', ('q25', 'ㄹ'): 'q19', ('q25', 'ㅁ'): 'q21', ('q25', 'ㅗ'): 'q0', ('q25', 'ㅅ'): 'q24', ('q25', 'ㅇ'): 'q26', ('q25', 'ㅣ'): 'q9', ('q25', 'ㅡ'): 'q12', ('q25', '획'): 'q19', ('q25', '쌍'): 'q19', ('q26', 'ㄱ'): 'q5', ('q26', 'ㄴ'): 'q5', ('q26', 'ㅏ'): 'q7', ('q26', 'ㄹ'): 'q5', ('q26', 'ㅁ'): 'q5', ('q26', 'ㅗ'): 'q0', ('q26', 'ㅅ'): 'q5', ('q26', 'ㅇ'): 'q5', ('q26', 'ㅣ'): 'q9', ('q26', 'ㅡ'): 'q12', ('q26', '획'): 'q19', ('q26', '쌍'): 'q5', ('q27', 'ㄱ'): 'q5', ('q27', 'ㄴ'): 'q5', ('q27', 'ㅏ'): 'q7', ('q27', 'ㄹ'): 'q5', ('q27', 'ㅁ'): 'q5', ('q27', 'ㅗ'): 'q0', ('q27', 'ㅅ'): 'q5', ('q27', 'ㅇ'): 'q5', ('q27', 'ㅣ'): 'q9', ('q27', 'ㅡ'): 'q12', ('q27', '획'): 'q19', ('q27', '쌍'): 'q19', ('q28', 'ㄱ'): 'q5', ('q28', 'ㄴ'): 'q5', ('q28', 'ㅏ'): 'q7', ('q28', 'ㄹ'): 'q5', ('q28', 'ㅁ'): 'q5', ('q28', 'ㅗ'): 'q0', ('q28', 'ㅅ'): 'q5', ('q28', 'ㅇ'): 'q5', ('q28', 'ㅣ'): 'q9', ('q28', 'ㅡ'): 'q12', ('q28', '획'): 'q13', ('q28', '쌍'): 'q19'}

cons={'ㄱ':0,'ㄲ':1,'ㄴ':2,'ㄷ':3,'ㄸ':4,'ㄹ':5,'ㅁ':6,'ㅂ':7,'ㅃ':8,'ㅅ':9,'ㅆ':10,'ㅇ':11,'ㅈ':12,'ㅉ':13,
      'ㅊ':14,'ㅋ':15,'ㅌ':16,'ㅍ':17,'ㅎ':18}
vowels={'ㅏ':0,'ㅐ':1,'ㅑ':2,'ㅒ':3,'ㅓ':4,'ㅔ':5,'ㅕ':6,'ㅖ':7,'ㅗ':8,'ㅘ':9,'ㅙ':10,'ㅚ':11,'ㅛ':12,'ㅜ':13,
        'ㅝ':14,'ㅞ':15,'ㅟ':16,'ㅠ':17,'ㅡ':18,'ㅢ':19,'ㅣ':20}
bottom={'e':0,'ㄱ':1,'ㄲ':2,'ㄳ':3,'ㄴ':4,'ㄵ':5,'ㄶ':6,'ㄷ':7,'ㄹ':8,'ㄺ':9,'ㄻ':10,'ㄼ':11,'ㄽ':12,'ㄾ':13,
        'ㄿ':14,'ㅀ':15,'ㅁ':16,'ㅂ':17,'ㅄ':18,'ㅅ':19,'ㅆ':20,'ㅇ':21,'ㅈ':22,'ㅊ':23,'ㅋ':24,'ㅌ':25,'ㅍ':26,'ㅎ':27}

NRG=['ㄱ','ㄴ','ㅏ','ㄹ','ㅁ','ㅗ','ㅅ','ㅇ','ㅣ','ㅡ','획','쌍']
def main():
    parser = yacc.yacc()
    
    nolower=''
    s='('
    for i in range(len(NRGcons)):
        for j in range(len(list(NRGcons.keys())[i])):
            s=s+list(NRGcons.keys())[i][j]+' '
        s= s[:-1]
        s = s+'+'
    s=s[:-1]
    s=s+') ('
    for i in range(len(NRGvow)):
        for j in range(len(list(NRGvow.keys())[i])):
            s=s+list(NRGvow.keys())[i][j]+' '
        s= s[:-1]        
        s = s+'+'
    s=s[:-1]
    nolower=s+')'
    s=s+') ('
    for i in range(len(NRGlowcons)):
        for j in range(len(list(NRGlowcons.keys())[i])):
            s = s+list(NRGlowcons.keys())[i][j]+' '
        s=s[:-1]
        s= s+'+'
    s=s[:-1]
    s=s+')' 
    s=s+'+'+nolower
    s='('+s+')*'                   #form the Hangul Regular Expression
    

   
    result = parser.parse(s)

    m_DFA=Make_mDFA(result,NRG)  #convert Regular-Expression to m-DFA


    global trans_fct
    trans_fct=m_DFA[1]
    init_state=m_DFA[2]
    final_states=m_DFA[3]


    uorb=input("Upper Consonant First: u, Bottom Consonant First: b\n")
    Mealy(init_state,final_states,uorb)
    


def Mealy(initial,final,uorb):      #assemble symbols into Hangul syllables
    os.system('cls')
    q=initial
    final_states=final
    visited=[q]
    inputstring=""
    keyboardstring=""

    while True:

        newin=input() 

        if newin=='<':    #deletion
            inputstring=inputstring[:-1]
            keyboardstring=keyboardstring[:-1]
            visited.pop()
            q=visited[-1]

        elif newin=='b' or newin=='u':
            uorb=newin
        else:
            hanin=NRG_to_Hangul[newin]
            inputstring = inputstring+hanin
            keyboardstring = keyboardstring+newin
            q=trans_fct[(q,hanin)]

            visited.append(q)


        processed_string = inputstring

        index=0
        for k in range(len(visited)-1):    # if final_states -> non_final_states, insert e to divide btw syllables
            if visited[k]!=initial and ((visited[k] in final_states) and (visited[k+1] not in final_states)):
                endconindex = k+1+index
                startingconindex = k+index
                while processed_string[startingconindex:endconindex] not in list(NRGcons.keys()):
                    startingconindex = startingconindex - 1

                processed_string = processed_string[:startingconindex] + 'e' + processed_string[startingconindex:]
                index = index + 1


        tokens=processed_string.split('e')


        complete=False

        for l in range(len(tokens[0])):   # check if the token is incomplete yet
            if tokens[0][l] in v:
                complete=True
                break

        i=0
        while complete and i<len(tokens):   # divide the tokens into syllables
            complete=False
            for l in range(len(tokens[i])):
                if tokens[i][l] in v:
                    complete = True
                    break
            j=0

            while j < len(tokens[i]):
                if tokens[i][j] in v:
                    endconindex=j
                    startingconindex=j-1
                    while tokens[i][startingconindex:endconindex] not in list(NRGcons.keys()):
                        startingconindex=startingconindex-1
                    tokens[i]=tokens[i][:startingconindex]+'e'+tokens[i][startingconindex:]
                    j=j+1
                    while j<len(tokens[i]) and ((tokens[i][j] in v) or (tokens[i][j] == '획')):
                        j=j+1
                else:
                    j=j+1
            i=i+1


        complete=''
        if uorb=='b':   # bottom consonant first

            firstToken=tokens[0]
            if firstToken[0] == 'e':
                complete = complete + firstToken[1:]
            elif 'e' not in firstToken:
                complete = complete + 'e' + firstToken     # the token contains upper consonant only

            for i in range(1,len(tokens)):
                if tokens[i][0] == 'e':
                   complete=complete+tokens[i]
                elif 'e' not in tokens[i]:          # the token contains upper consonant only
                    complete=complete+'e'+tokens[i]

        elif uorb=='u':    # upper consonant first

            for i in range(0, len(tokens)-1):
                if tokens[i][0] == 'e':
                    complete = complete + tokens[i]
                elif 'e' not in tokens[i]:  # the token contains upper consonant only
                    complete = complete + 'e' + tokens[i]

            lastToken = tokens[len(tokens) - 1]
            endlowerindex=len(lastToken)
            startlowerindex=len(lastToken)-1
            nolowercon=False
            if lastToken[0] == 'e':
               while lastToken[startlowerindex:endlowerindex] not in list(NRGcons.keys()):
                   if lastToken[startlowerindex] in v:
                       nolowercon=True
                       break
                   startlowerindex = startlowerindex - 1
               if nolowercon:    # if the syllable does not have a bottom consonant
                   complete=complete+lastToken
               else:    # if the syllable has a bottom consonant
                   complete = complete+lastToken[:startlowerindex]+'e'+lastToken[startlowerindex:]


            elif 'e' not in lastToken:  # the token contains upper consonant only
                complete = complete + 'e' + lastToken


        os.system('cls')
        printSyllables(complete)
        print("\ninput so far: "+keyboardstring,sep=' ',end="")



def printSyllables(input_string):  #print a series of syllables
    outputvocab=''
    syllables=input_string.split('e')
    for syllable in syllables:    
        if syllable != '':
            outputsymbol=Syllable(syllable)           
            outputvocab=outputvocab+outputsymbol        
    print(outputvocab)


def Syllable(syllable):        #print a syllable
    uppercons=''
    lowercons='e'
    vowel=''  
    tempvowel=''
    vowel_index=0
    cons_only=True
    for i in range(len(syllable)):
        if syllable[i] in v:
            cons_only=False
    if cons_only:
        return NRGcons[syllable]

    if not cons_only:
        for i in range(len(syllable)):
            if syllable[i] in v:
                vowel_index=i
                break

        uppercons=NRGcons[syllable[:vowel_index]]

        while (syllable[vowel_index] in v or syllable[vowel_index] == '쌍' or syllable[vowel_index] ==  '획'):
            tempvowel=tempvowel+syllable[vowel_index]
            if vowel_index>=len(syllable)-1:
                vowel_index=vowel_index+1
                break
            vowel_index=vowel_index+1

        vowel=NRGvow[tempvowel]

        if syllable[vowel_index:]!='':
            lowercons=NRGlowcons[syllable[vowel_index:]]

    return chr(44032+((cons[uppercons]*21)+vowels[vowel])*28+bottom[lowercons])


if __name__ == "__main__":
    main()


