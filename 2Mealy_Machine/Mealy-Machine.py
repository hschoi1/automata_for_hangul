def main():
    states=[]
    in_sym=[]
    out_sym=[]
    trans_fct={}
    out_fct={}
    init_state=''
    
    print("Enter Mealy-Machine info")
    
    line=input("Enter States:\nex) q0,q1,q2,q3\n")
    states.extend(line.strip().split(','))
    line=input("Enter Input symbols:\nex) 0,1\n")
    in_sym.extend(line.strip().split(','))
    line=input("Enter State transition function and type 'end' to end.\nex)\n"
               "q0,1,q1\nq0,0,q2\n,q1,0,q2\nq2,1,q3\nq3,0,q2\nq3,1,q1\nend\n")
    while line!="end":
        fct_info=line.strip().split(',')
        if (fct_info[0] not in states) or (fct_info[2] not in states):
            print("Not valid state! Enter again!")
        elif fct_info[1] not in in_sym:
            print("Not valid input symbol! Enter again!")
        else:
            trans_fct[(fct_info[0],fct_info[1])]=fct_info[2]     
        line=input()
                
    line=input("Enter Output symbols:\nex) a,b,c,d")
    out_sym.extend(line.strip().split(','))               
            
    line=input("Enter Output function and type 'end' to end.\nex)\n"
               "q0,1,a\nq0,0,b\nq1,0,c\nq2,1,d\nq3,0,a\nq3,1,c\nend\n")
    while line!="end":
        fct_info=line.strip().split(',')
        if (fct_info[0] not in states) or (fct_info[2] not in out_sym):
            print("Not valid state! Enter again!")
        elif fct_info[1] not in in_sym:
            print("Not valid input symbol! Enter again!")
        else:
            out_fct[(fct_info[0],fct_info[1])]=fct_info[2]     
        line=input()
            
    line=input("Enter Initial state:\nex) q0\n")
    temp_init=line.strip()
    while temp_init not in states:
        temp_init=input("Not valid state! Enter again!\n")
    init_state=temp_init
    
    print("\nType 'end' to end the program\n")
    line=input("Enter a string or end\nex) 1011010\n")
    while line!="end":
        output,visited=Mealy(states,line,trans_fct,out_fct,init_state)
        print("visited states: "+visited)
        print("output string: "+output)
        print("\n")
        line=input()

def Mealy(states,input_vocab,trans_function,output_function,initial):
    outputvocab=""
    visited=initial
    i=0
    q=initial
    while (i<len(input_vocab)):
        if (q,input_vocab[i]) in trans_function.keys():    #check if the next move is available
            temp_q=trans_function[(q,input_vocab[i])]
            outputvocab=outputvocab+output_function[(q,input_vocab[i])]
            q=temp_q
            visited=visited+" "+q
            i=i+1            
        else: return ("No path exists!",visited)     #if there is no state to move to, then return "No path exists"
        
    return (outputvocab,visited)
        
if __name__ == "__main__":
    main()
        
        
