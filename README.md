# automata_for_hangul
# DFA to KT Naratgul Keyboard
2017Fall CS322 Project

There are around 10,000 possible combinations of constants and vowels for a syllable in Korean.
Korean phone keyboards (non-qwerty) usually have 4x3 buttons with which it is possible to create
all of the combinations. However it clearly is not a good idea to hard-code them with thousands of ifs and elses.
There are two typing systems: Upper Consonant First and Bottom Consonant First.
Even though we use only Bottom Constant First nowadays, both systems are implemented here.


There are obviously other more efficient methods to implement a korean phone keyboard, but the point
of this project is to build upon deterministic finite automata(DFA) and extend to m-DFA step by step.


## Structure

1. DFA-simulator

* takes in DFA information.
* takes an input string.
* outputs whether the string ends in final states

2. Mealy-Machine

* takes in DFA information
* takes an input string.
* outputs an output string.

3. Hangul by QWERTY Keyboard

* takes in which system to use between Upper Consonant First and Bottom Consonant First.
* takes a consonant/vowel one at a time. (by Enter)
* shows corresponding syllables on the first line.

Too see how consonants and vowels constitute a syllable in Unicode, check out this link:
https://en.wikipedia.org/wiki/Korean_language_and_computers#Hangul_Syllables_block

If Korean characters are not displayed correctly, change the code page to 949 (for Windows)

4. eNFA to mDFA

* takes in e-NFA information
* transforms the e-NFA into the equivalent m-DFA
* shows the equivalent m-DFA information

5. RE to mDFA

* takes in a regular expression
* creates the equivalent m-DFA which accepts the R.E
* For parsing, Python Lex-Yacc is used. Copyright is stated at the bottom of this page.


6. Hangul by 4x3 KT Naratgul Phone Keyboard

* takes in which system to use between Upper Consonant First and Bottom Consonant First.
* takes a Naratgul consonant/vowel at a time(by Enter)
* shows corresponding syllables on the first line.
* KT Naratgul 4x3 keyboard = 1,2,3,q,w,e,a,s,d,z,x,c in QWERTY Keyboard
* Inside the code, epsilon e in e-NFA here is used to separate each syllable; it is used differently for the two different typing systems.


## Dependencies

### PLY

PLY (Python Lex-Yacc)                   Version 3.9

Copyright (C) 2001-2016
David M. Beazley (Dabeaz LLC)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of the David Beazley or Dabeaz LLC may be used to
  endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
