# -*- coding: utf-8 -*-
from __future__ import print_function

import os

states=['S','V','O','U','A','I','K','N','R','L','bus']
in_sym=['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ',
        'ㄸ','ㅃ','ㅆ','ㅉ','ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅐ','ㅒ','ㅔ','ㅖ']
c=['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㄸ','ㅃ','ㅆ','ㅉ']
v=['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅐ','ㅒ','ㅔ','ㅖ']
trans_fct={}
cons={'ㄱ':0,'ㄲ':1,'ㄴ':2,'ㄷ':3,'ㄸ':4,'ㄹ':5,'ㅁ':6,'ㅂ':7,'ㅃ':8,'ㅅ':9,'ㅆ':10,'ㅇ':11,'ㅈ':12,'ㅉ':13,
      'ㅊ':14,'ㅋ':15,'ㅌ':16,'ㅍ':17,'ㅎ':18}
vowels={'ㅏ':0,'ㅐ':1,'ㅑ':2,'ㅒ':3,'ㅓ':4,'ㅔ':5,'ㅕ':6,'ㅖ':7,'ㅗ':8,'ㅘ':9,'ㅙ':10,'ㅚ':11,'ㅛ':12,'ㅜ':13,
        'ㅝ':14,'ㅞ':15,'ㅟ':16,'ㅠ':17,'ㅡ':18,'ㅢ':19,'ㅣ':20}
bottom={'e':0,'ㄱ':1,'ㄲ':2,'ㄳ':3,'ㄴ':4,'ㄵ':5,'ㄶ':6,'ㄷ':7,'ㄹ':8,'ㄺ':9,'ㄻ':10,'ㄼ':11,'ㄽ':12,'ㄾ':13,
        'ㄿ':14,'ㅀ':15,'ㅁ':16,'ㅂ':17,'ㅄ':18,'ㅅ':19,'ㅆ':20,'ㅇ':21,'ㅈ':22,'ㅊ':23,'ㅋ':24,'ㅌ':25,'ㅍ':26,'ㅎ':27}
sepcons_to_b={'ㄱㅅ':'ㄳ','ㄴㅈ':'ㄵ','ㄴㅎ':'ㄶ','ㄹㄱ':'ㄺ','ㄹㅁ':'ㄻ','ㄹㅂ':'ㄼ','ㄹㅅ':'ㄽ','ㄹㅌ':'ㄾ',
              'ㄹㅍ':'ㄿ','ㄹㅎ':'ㅀ','ㅂㅅ':'ㅄ'}
sepv_to_v={'ㅗㅏ':'ㅘ','ㅗㅐ':'ㅙ','ㅗㅣ':'ㅚ','ㅜㅓ':'ㅝ','ㅜㅔ':'ㅞ','ㅜㅣ':'ㅟ','ㅡㅣ':'ㅢ'}
init_state='S'
def main():
    #define trans_fct
    trans_fct[('O','ㅏ')]='A'
    trans_fct[('O','ㅣ')]='I'
    trans_fct[('O','ㅐ')]='I'
    trans_fct[('U','ㅓ')]='A'
    trans_fct[('U','ㅔ')]='I'
    trans_fct[('U','ㅣ')]='I'
    trans_fct[('A','ㅣ')]='I'

    for consonant in c:  
        trans_fct[('S',consonant)]='V'
        trans_fct[('V',consonant)]='V'
        trans_fct[('L',consonant)]='V'

        for i in ['O','U','A','I']:
            trans_fct[(i,consonant)]='bus'


        if consonant in ['ㄱ','ㅂ']:
            trans_fct[('bus',consonant)]='K'
        elif consonant=='ㄴ':
            trans_fct[('bus',consonant)]='N'
        elif consonant=='ㄹ':
            trans_fct[('bus',consonant)]='R'
        elif consonant in ['ㄷ','ㅁ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㄲ','ㅆ']:
            trans_fct[('bus',consonant)]='L'
        elif consonant in ['ㄸ','ㅃ','ㅉ']:
            trans_fct[('bus',consonant)]='V'

        if consonant == 'ㅅ':
            trans_fct[('K',consonant)]='L'
        else:
            trans_fct[('K',consonant)]='V'

        if consonant in ['ㅈ','ㅎ']:
            trans_fct[('N',consonant)]='L'
        else:
            trans_fct[('N',consonant)]='V'

        if consonant in ['ㄱ','ㅁ','ㅂ','ㅅ','ㅌ','ㅍ','ㅎ']:
            trans_fct[('R',consonant)]='L'
        else:
            trans_fct[('R',consonant)]='V'


    for vowel in v:
        for i in ['K','N','R','L']:
            trans_fct[(i,vowel)]='bus'

        if vowel=='ㅗ':
            trans_fct[('bus',vowel)]='O'
            trans_fct[('V',vowel)]='O'
        elif vowel=='ㅜ':
            trans_fct[('bus',vowel)]='U'
            trans_fct[('V',vowel)]='U'
        elif vowel in ['ㅏ','ㅑ','ㅓ','ㅕ','ㅡ']:
            trans_fct[('bus',vowel)]='A'
            trans_fct[('V',vowel)]='A'
        elif vowel in ['ㅛ','ㅠ','ㅣ','ㅐ','ㅒ','ㅔ','ㅖ']:
            trans_fct[('bus',vowel)]='I'
            trans_fct[('V',vowel)]='I'    


    uorb=input("Upper Consonant First: u, Bottom Consonant First: b\n")
    if uorb=='u':
        UpperFirst()
    else:
        BottomFirst()



def BottomFirst():
    os.system('cls')
    q=init_state
    visited=q
    current=0
    inputstring=""
    newin=''
    while True:

        newin=input() 
        outputvocab=""  

        if newin=='<':    #deletion
            newin,inputstring,visited,q=BottomDelete(inputstring,visited,q)
            
        if newin=='u':     #change the mode to upperfirst
            UpperFirst()

        if q=='V':
            if newin in c:
                inputstring=inputstring+"e"
        elif q =='K':
            if newin in v:
                inputstring=inputstring[:-1]+"e"+inputstring[-1]
            elif newin != 'ㅅ':
                inputstring=inputstring+"e"               
        elif q =='N':
            if newin in v:
                inputstring=inputstring[:-1]+"e"+inputstring[-1]            
            elif newin not in ['ㅈ','ㅎ']:
                inputstring=inputstring+"e"    
        elif q=='R':
            if newin in v:
                inputstring=inputstring[:-1]+"e"+inputstring[-1]            
            elif newin not in ['ㄱ','ㅁ','ㅂ','ㅅ','ㅌ','ㅍ','ㅎ']:
                inputstring=inputstring+"e"                    
        elif q=='L':
            if newin in v:
                inputstring=inputstring[:-1]+"e"+inputstring[-1]            
            elif newin in c:
                inputstring=inputstring+"e"                         
        elif q in ['O','U','A','I']:                    
            if newin in ['ㄸ','ㅃ','ㅉ']:
                inputstring=inputstring+'e'

        inputstring=inputstring+newin 
        os.system('cls')        
        printSyllables(inputstring) 
        print("input so far: "+inputstring.replace('e',''),sep=' ',end="")

        q=trans_fct[(q,newin)]
        if q=="bus":
            q=trans_fct[(q,newin)]
        visited=visited+q



def UpperFirst():
    os.system('cls')
    q=init_state
    visited=q
    current=0
    inputstring=""
    newin=''

    while True:     
        print("input so far: "+inputstring.replace('e',''),sep=' ',end="")
        newin=input()
        outputvocab=""  

        if newin=='<':        # deletion
            newin,inputstring,visited,q=UpperDelete(inputstring,visited,q)
         
        if newin=='b':     #change the mode to bottomfirst
            BottomFirst()     
            print(visited)
            print(inputstring)
        if q=="S":
            inputstring=inputstring+newin
        elif q=='V':
            if newin in c:
                inputstring=inputstring+newin+"e"
            elif newin in v:
                inputstring=inputstring+newin
        elif q =='K': 
            if newin in v:
                inputstring=inputstring[:-1]+"e"+inputstring[-1]+newin
            elif newin != 'ㅅ':
                inputstring=inputstring[:-2]+inputstring[-1]+"e"+newin          
            else: inputstring=inputstring[:-2]+inputstring[-1]+'e'+newin
        elif q =='N':
            if newin in v:
                inputstring=inputstring[:-1]+"e"+inputstring[-1]+newin
            elif newin not in ['ㅈ','ㅎ']:
                inputstring=inputstring[:-2]+inputstring[-1]+"e"+newin 
            else:inputstring=inputstring[:-2]+inputstring[-1]+'e'+newin

        elif q=='R':
            if newin in v:
                inputstring=inputstring[:-1]+"e"+inputstring[-1]+newin
            elif newin not in ['ㄱ','ㅁ','ㅂ','ㅅ','ㅌ','ㅍ','ㅎ']:
                inputstring=inputstring[:-2]+inputstring[-1]+"e"+newin         
            else: 
                inputstring=inputstring[:-2]+inputstring[-1]+'e'+newin                   
        elif q=='L': 
            if newin in v:
                inputstring=inputstring[:-1]+"e"+inputstring[-1]+newin

            elif newin in c:
                inputstring=inputstring[:-2]+inputstring[-1]+"e"+newin      

        elif q in ['O','U','A','I']:    
            if newin in v:
                inputstring=inputstring+newin

            elif newin in ['ㄸ','ㅃ','ㅉ']:
                inputstring=inputstring+"e"+newin
            else:
                inputstring=inputstring+"e"+newin

        inputstring=inputstring.replace("ee","e")  
        os.system('cls') 
        printSyllables(inputstring)    
        q=trans_fct[(q,newin)]
        if q=="bus":
            q=trans_fct[(q,newin)]

        visited=visited+q  
        
def BottomDelete(inputstring,visited,q):
    newin='<'
    while newin=='<': 
        outputvocab=""
        if inputstring[-1]!='e':
            inputstring=inputstring[:-1] 
            visited=visited[:-1]
            q=visited[-1]   
            

        else:
            inputstring=inputstring[:-1]
            while len(inputstring)>=1 and inputstring[-1]!='e':
                inputstring=inputstring[:-1]
                visited=visited[:-1]
                q=visited[-1]            


        os.system('cls') 
        printSyllables(inputstring)  
        print("input so far: "+inputstring.replace('e',''),sep=' ',end="")
        newin=input()   
    return newin,inputstring,visited,q

def UpperDelete(inputstring,visited,q):
    newin='<'
    if inputstring[-1] in c:     #remove the last consonant         
        inputstring=inputstring[:-2]    
        visited=visited[:-1] 
        q=visited[-1]
        os.system('cls') 
        printSyllables(inputstring)
        print("input so far: "+inputstring.replace('e',''),sep=' ',end="")
        newin=input()
        if newin!='<':
            inputstring=inputstring[:-1]+'e'+inputstring[-1]
                        

    while inputstring[-1]!='e' and newin=='<' :   #remove the second last syllable             
        outputvocab=""
        inputstring=inputstring[:-1]
        visited=visited[:-1]
        q=visited[-1]   
        os.system('cls')          
        printSyllables(inputstring)
        print("input so far: "+inputstring.replace('e',''),sep=' ',end="")
        newin=input()
        if (newin =='<') and (inputstring[-1]=='e'):
            inputstring=inputstring[:-1]            
            break
        elif(newin!='<') and (inputstring[-1] in c):
            inputstring=inputstring[:-1]+'e'+inputstring[-1]
            break
        elif(newin!='<') and (inputstring[-1]=='e'):
            q=init_state
           
    while newin=='<':              
        outputvocab=""
        while len(inputstring)>=1 and inputstring[-1]!='e':
            inputstring=inputstring[:-1]
            visited=visited[:-1]
            q=visited[-1]
          
        os.system('cls') 
        printSyllables(inputstring)        
        print("input so far: "+inputstring.replace('e',''),sep=' ',end="")
        newin=input()
        if newin!='<':
            q=init_state
            visited=visited+q
        else:
            inputstring=inputstring[:-1]
    return newin, inputstring,visited,q


def printSyllables(input_string): 
    outputvocab=''
    syllables=input_string.split('e')

    for syllable in syllables:    
        if syllable != '':
            outputsymbol=Syllable(syllable)           
            outputvocab=outputvocab+outputsymbol        
    print(outputvocab)

def Syllable(syllable):
    uppercons=''
    lowercons='e'
    vowel=''  


    if len(syllable)==1:
        return syllable

    while len(syllable)>=1:
        if len(syllable)==1:
            uppercons=syllable
            syllable=''   
        else:        
            if syllable[-1] in c:
                if syllable[-2] in c:
                    lowercons=sepcons_to_b[syllable[-2:]]      
                    syllable=syllable[:-2]
                elif syllable[-2] in v:                              
                    lowercons=syllable[-1]
                    syllable=syllable[:-1]                     

            elif syllable[-1] in v:                   
                if syllable[-2] in v:
                    vowel=sepv_to_v[syllable[-2:]]    
                    syllable=syllable[:-2]
                elif syllable[-2] in c:
                    vowel=syllable[-1]
                    syllable=syllable[:-1]

    return chr(44032+((cons[uppercons]*21)+vowels[vowel])*28+bottom[lowercons])


if __name__ == "__main__":
    main()


