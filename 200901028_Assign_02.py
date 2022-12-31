#Syed Ali Raza 200901028 CS-01-B

import re
import string
import ast
from pprint import pprint

#Module 1
class lexical_analyzer:
    def __init__(self, string):
        self.expression = string
        self.tokenized = []
        self.whitespace = [' ','\t','\n']
        self.constants = ['1','2','3','4','5','6','7','8','9','0']
        self.operators = ['+','-','*','/']
        self.sp_characters = ['&', '%']
        self.puncuators = [';' , ':', ',', '(',')','{','}','[',']']

    def tokenize(self):
        self.tokenized = re.findall(r'\b\d+\b|\b[a-zA-Z]+\b|[+-/*&%;:,(){}\[\]\s]', self.expression)
        self.tokenized = [token for token in self.tokenized if token not in self.whitespace]
        print("Tokenized String: ")
        print(self.tokenized)

    def type_of_token(self):
        print("Characterization of tokens: ")
        for char in self.tokenized:
            if char in string.ascii_letters:
                print(char + " Identifier")
            elif char in self.constants:
                print(char + " Constant")
            elif char in self.operators:
                print(char + " Operator")
            elif char in self.sp_characters:
                print(char + " Special Character")
            elif char in self.puncuators:
                print(char + " Punctuator")

if __name__ == "__main__":
    input_string = input("Enter the expression: ")
    obj1 = lexical_analyzer(input_string)
    print('Inputted String: ' + input_string)
    obj1.tokenize()
    obj1.type_of_token()
    
    #Module 2
    print("Printing AST")    
    code = ast.parse(input_string)
    pprint(code)
    print(ast.dump(code))
    exec(compile(code, filename="", mode="exec"))
