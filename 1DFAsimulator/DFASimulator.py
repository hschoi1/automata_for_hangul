def main():
    states=[]
    in_sym=[]
    trans_fct={}
    init_state=''
    final_states=[]
    
    print("Enter DFA_info")
    
    line=input("Enter States:\nex) q0,q1,q2,q3,q4\n")
    states.extend(line.strip().split(','))
    line=input("Enter Input symbols:\nex) a,b\n")
    in_sym.extend(line.strip().split(','))
    line=input("Enter State transition function and type 'end' to end.\nex)\n"
               "q0,b,q1\nq1,b,q2\nq2,a,q3\nq3,b,q4\nq4,a,q4\nq4,b,q4\nend\n")
    while line!="end":
        fct_info=line.strip().split(',')
        if (fct_info[0] not in states) or (fct_info[2] not in states):
            print("Not valid state! Enter again!")
        elif fct_info[1] not in in_sym:
            print("Not valid input symbol! Enter again!")
        else:
            trans_fct[(fct_info[0],fct_info[1])]=fct_info[2]     
        line=input()
        
    line=input("Enter Initial state:\nex) q0\n")
    temp_init=line.strip()
    while temp_init not in states:
        temp_init=input("Not valid state! Enter again!\n")
    init_state=temp_init
    
    line=input("Enter Final states:\nex) q4\n")
    temp_final=line.strip().split(',')
    if not isinstance(temp_final,list):
        temp_final=[temp_final]    
    while(not set(temp_final).issubset(set(states))):
        temp_final=input("Not valid state contained!\n").strip().split(",")
        if not isinstance(temp_final,list):
            temp_final=[temp_final]
            
    final_states.extend(temp_final)
    
    print("Type 'end' to end the program\n")
    line=input("Enter a string or end\nex) ababab\n")
    while line!="end":
        print(DFA(line,trans_fct,init_state,final_states)+"\n")
        line=input()
        
        
def DFA(input_vocab,trans_function,initial,final):
    i=0
    q=initial
    while (i<len(input_vocab)):
        if (q,input_vocab[i]) in trans_function.keys():    #check if the next move is available
            q=trans_function[(q,input_vocab[i])]
            i=i+1
        else: return "no"     #if there is no state to move to, then return "no"
          
    if q in final:
        return "yes"
    elif q not in final:
        return "no"    
        
        
if __name__ == "__main__":
    main()
        
        
