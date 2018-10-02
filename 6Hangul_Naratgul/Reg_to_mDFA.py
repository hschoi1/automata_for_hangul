# -*- coding: utf-8 -*-
import yacc1
import eNFA_to_mDFA
eNFA_trans_fct={}
eNFA_states=[]
count=0

def Make_mDFA(inputreg,insymlist):
    
    #print(initial)
    eNFA=makeTree(inputreg)
    #print(eNFA)
    #print(eNFA_trans_fct)
    DFA=eNFA_to_mDFA.eNFA_to_DFA(eNFA[0],insymlist,eNFA_trans_fct,eNFA[1],[eNFA[2]])
    #print("states :")
    #print(DFA[0])
    #print("transition function: ")
    #print(DFA[2])
    #print("initial state")
    #print(DFA[3])
    #print("final states")
    #print(DFA[4])    
    
    m_DFA=eNFA_to_mDFA.DFA_to_mDFA(DFA[0],insymlist,DFA[2],DFA[3],DFA[4])    
    return m_DFA
    #print("states :")
    #print(m_DFA[0])
    #print("transition function: ")
    #for key in sorted(m_DFA[1]):
    #    print("%s: %s" % (key, m_DFA[1][key]))    
    #print("initial state")
    #print(m_DFA[2])
    #print("final states")
    #print(m_DFA[3])
    
def makeTree(tree):
    operation=tree[0]
    if operation=='concatenation':
        leftsub=makeTree(tree[1])
        rightsub=makeTree(tree[2])
        return concat(leftsub,rightsub)
    elif operation=='union':
        leftsub=makeTree(tree[1])
        rightsub=makeTree(tree[2])  
        return union(leftsub,rightsub)
    elif operation=='closure':
        sub=makeTree(tree[1])       
        return closure(sub)
    elif operation=='term':
        sub=symbol(tree[1])
        return sub
    
           
            
def symbol(sym):
    states=[]
    global count
    initial='q'+str(count)
    final='q'+str(count+1)
    eNFA_trans_fct[(initial,sym)]=final
    eNFA_states.append(initial)
    eNFA_states.append(final)
    states.append(initial)
    states.append(final)
    count=count+2
    return [states, initial, final]

def union(A,B):
    states=[]
    global count
    initial='q'+str(count)
    final='q'+str(count+1)
    A_states=A[0]
    A_initial=A[1]
    A_final=A[2]
    B_states=B[0]
    B_initial=B[1]
    B_final=B[2] 
    eNFA_states.append(initial)
    eNFA_states.append(final)
    states.append(initial)
    states.append(final)
    states.extend(A_states)
    states.extend(B_states)    
    count=count+2
    eNFA_trans_fct[(A_final,'e')]=final
    eNFA_trans_fct[(B_final,'e')]=final
    eNFA_trans_fct[(initial,'e')]=[A_initial,B_initial]
    return [states,initial,final]
def concat(A,B):
    states=[]
    global count

    A_states=A[0]
    A_initial=A[1]
    A_final=A[2]
    B_states=B[0]
    B_initial=B[1]
    B_final=B[2] 

    states.extend(A_states)
    states.extend(B_states)
    eNFA_trans_fct[(A_final,'e')]=B_initial
    return [states,A_initial,B_final]

def closure(A):
    states=[]
    global count
    initial='q'+str(count)
    final='q'+str(count+1)
    A_states=A[0]
    A_initial=A[1]
    A_final=A[2]

    eNFA_states.append(initial)
    eNFA_states.append(final)    
    states.append(initial)
    states.append(final)
    states.extend(A_states)
    count=count+2
    eNFA_trans_fct[(A_final,'e')]=[final,A_initial]
    eNFA_trans_fct[(initial,'e')]=[final,A_initial]   
    return [states,initial,final]    

