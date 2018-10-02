
def main():
    eNFA_states=[]
    in_sym=[]
    eNFA_trans_fct={}
    eNFA_init_state=''
    eNFA_final_states=[]
    
    print("Enter e-NFA_info")
    
    line=input("Enter States:\nex) A,B,C,D,E,F,G,H\n")
    eNFA_states.extend(line.strip().split(','))
    line=input("Enter Input symbols:\nex) 0,1\n")
    in_sym.extend(line.strip().split(','))
    line=input("Enter State transition function and type 'end' to end.\nex)\n"
               "A,0,B\nA,1,F\nB,0,G\nB,1,C\nC,0,A\nC,1,C\nC,e,C\nD,0,C\nD,1,G\n"
               "E,0,H\nE,1,F\nF,0,C\nF,1,G\nG,0,G\nG,1,E\nH,0,G\nH,1,C\nend\n")
    while line!="end":
        fct_info=line.strip().split(',')
        if (fct_info[0],fct_info[1]) in eNFA_trans_fct.keys(): # for when delta(q,a)=[q0,q1]
            if isinstance( eNFA_trans_fct[(fct_info[0],fct_info[1])],list):
                eNFA_trans_fct[(fct_info[0],fct_info[1])].append(fct_info[2])
            else:
                state=[eNFA_trans_fct[(fct_info[0],fct_info[1])],fct_info[2]]
                eNFA_trans_fct[(fct_info[0],fct_info[1])]=state
           
        else:
            eNFA_trans_fct[(fct_info[0],fct_info[1])]=fct_info[2]     
        line=input()
        
    line=input("Enter Initial state:\nex) A\n")
    temp_init=line.strip()
    eNFA_init_state=temp_init
    
    line=input("Enter Final states:\nex) C\n")
    temp_final=line.strip().split(',')
    for i in range(len(temp_final)):
        eNFA_final_states.append(temp_final[i])
    DFA=eNFA_to_DFA(eNFA_states,in_sym,eNFA_trans_fct,eNFA_init_state,eNFA_final_states)

    m_DFA=DFA_to_mDFA(DFA[0],in_sym,DFA[2],DFA[3],DFA[4])
    print('\nm-DFA states: ')
    print(sorted(m_DFA[0]))
    print('\nm-DFA transition functions: ')
    for key in sorted(m_DFA[1]):
        print("%s: %s" % (key, m_DFA[1][key]))
    print('\nm-DFA initial state: ')
    print(m_DFA[2])
    print('\nm-DFA final states: ')
    print(m_DFA[3])
    end=input("\nPress enter to exit")


        
def eClosure(vertex,eNFA_trans_fct):
    visited=[]
    stack=[]
    temp_keys=list(eNFA_trans_fct.keys())
    stack.append(vertex)
    while len(stack)!=0:
        v=stack.pop()
        if not isinstance(v,list):
            v=[v]
        for state in v:
            if state not in visited:
                visited.append(state)
                for i in range(len(temp_keys)):
                    pair=temp_keys[i]
                    if pair==(state,'e'):
                        stack.append(eNFA_trans_fct[(pair[0],pair[1])])
                   
    return visited
                   
                   
def matchState(DFA_state,dic):   # helper function for eNFA_to_DFA 
    for i in dic:
        if dic[i]==DFA_state:
            return i             # return the renamed state. eg. {q0,q1,q3} -> q1 
        
def eNFA_to_DFA(eNFA_states,in_sym,eNFA_trans_function,eNFA_initial,eNFA_finals):
    DFA_initial=eClosure(eNFA_initial,eNFA_trans_function)  # get DFA initial state
    DFA_initial.sort()
    DFA_trans_fct={}
    DFA_states_sofar=[DFA_initial]  #collects all transformed DFA states
    
    renamed_states={'q0':DFA_initial}   #used to rename transfomred DFA states
    count=1
    stack=[DFA_initial]    # states to be transformed 
    
    while len(stack)!=0:  # get DFA_states  
        
        
        state=stack.pop()
       
        renamed=matchState(state,renamed_states) 
        for a in in_sym:    
            states=[]
            for i in range(len(state)):  # find e-closure of the delta(q,a)
                if (state[i],a) in eNFA_trans_function.keys():
                    nextstates=eNFA_trans_function[(state[i],a)]
                    
                    if isinstance(nextstates,list):
                        for j in nextstates:
                            if (j,a) in eNFA_trans_function.keys():
                                states=list(set(states+eClosure(j,eNFA_trans_function)))
                            
                    else:
                        states=list(set(states+eClosure(nextstates,eNFA_trans_function)))
            states.sort()
            #print(state,a,states)
            if (states not in DFA_states_sofar):    # if delta(q,a) is first encountered, create a new state and give a new name and add it to trans_fct
                stack.append(states)
                DFA_states_sofar.append(states)
                renamed_states['q'+str(count)]=states
                DFA_trans_fct[(renamed,a)]='q'+str(count)
                count=count+1
            else:          #if delta(q,a) is already encountered, find its name and add it to trans_fct
                renamed2=matchState(states,renamed_states)
                DFA_trans_fct[(renamed,a)]=renamed2
                
    DFA_finals=[]      

    for state in DFA_states_sofar:   # get DFA_final

        if len(set(eNFA_finals).intersection(set(state)))!=0 :
            DFA_finals.append(matchState(state,renamed_states))
    
    return list(renamed_states.keys()),in_sym,DFA_trans_fct,'q0',DFA_finals





def whichState(subset,dic):    #helper function for DFA_to_mDFA
    for i in dic:
        if set(subset).issubset(set(dic[i])):
            return i

def DFA_to_mDFA(DFA_states,in_sym,DFA_trans_function,DFA_initial,DFA_final_states):
    mDFA_trans_fct={}
    count=0
    mDFA_initial=''
    renamed_states={}
    non_final=[vertex for vertex in DFA_states if vertex not in DFA_final_states]
    if len(non_final)==0:
        partition=[DFA_final_states]
    else:
        partition=[DFA_final_states,non_final]
    mDFA_finals=[]
    W=[DFA_final_states]
    while len(W)!=0:
        A=W.pop()
        for c in in_sym:
            X=[]
            for state in DFA_states:
                if DFA_trans_function[(state,c)] in A:
                    X.append(state)
        
            for Y in partition:
                intersection=[vertex for vertex in Y if vertex in X]
                YsubX=[vertex for vertex in Y if vertex not in X]
                if (len(intersection)!=0) and (len(YsubX)!=0):
  
                    partition[partition.index(Y)]=intersection
                    partition.append(YsubX)
                    if Y in W:
                        W[W.index(Y)]=intersection
                        W.append(YsubX)
                    else:
                        if len(intersection)<=len(YsubX):
                            W.append(intersection)
                        else:
                            W.append(YsubX)
    for state in partition:
        renamed_states['q'+str(count)]=state
        count=count+1
        
    for state in partition:
        renamed_state=whichState(state,renamed_states)  #renamed state
        
        if DFA_initial in state:
            mDFA_initial=renamed_state       #get mDFA_initial

        if len(set(DFA_final_states).intersection(set(state)))!=0:
            mDFA_finals.append(renamed_state)        #get mDFA_final
                
        for a in in_sym:  
            states=[]
            
            if isinstance(state,list):
                for j in state:
                    if (j,a) in DFA_trans_function.keys():
                        states.append(DFA_trans_function[(j,a)])  # get [ detal(q,a) ] for all q in its equivalent class
                    
            else:
                states.append(DFA_trans_function[(state,a)])           
             
            mDFA_trans_fct[(renamed_state,a)]=whichState(states,renamed_states)
        
    return list(renamed_states.keys()),mDFA_trans_fct,mDFA_initial,mDFA_finals
    


if __name__ == "__main__":
    main()
        
        
