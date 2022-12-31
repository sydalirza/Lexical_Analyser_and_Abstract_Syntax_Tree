# Lexical_Analyser_and_Abstract_Syntax_Tree
Imported Modules
The code imports the following modules:
1.	re: The re (Regular Expression) module provides functions for working with regular expressions in Python.
2.	string: The string module provides constants and functions for working with string data in Python.
3.	ast: The ast (Abstract Syntax Tree) module provides functions for parsing and manipulating Python code in the form of abstract syntax trees.
4.	pprint: The pprint (Pretty Print) module provides functions for pretty-printing data structures in Python.

Class Definition
The lexical_analyzer class represents a lexical analyzer that can tokenize a string of code and classify the tokens. It has the following attributes:
1.	expression: The input string to be tokenized.
2.	tokenized: A list of the tokenized form of the input string.
3.	whitespace: A list of characters that represent whitespace (i.e., spaces, tabs, and newlines).
4.	constants: A list of characters that represent constants (i.e., digits).
5.	operators: A list of characters that represent operators (i.e., +, -, *, and /).
6.	sp_characters: A list of characters that represent special characters (i.e., & and %).
7.	puncuators: A list of characters that represent punctuators (i.e., ;, :, ,, (, ), {, }, [, and ]).

Method Definitions
The lexical_analyzer class has two methods:
•	tokenize: This method uses a regular expression to split the input string into tokens and stores the resulting list of tokens in the tokenized attribute.
•	type_of_token: This method iterates over the list of tokens in the tokenized attribute and prints the type of each token.

Main Function
•	In the main function, the user is prompted to enter an expression, and the input is stored in the input_string variable. An instance of the lexical_analyzer class, obj1, is created with the input_string as its argument.
•	The tokenize method of obj1 is then called to tokenize the input string, and the type_of_token method is called to classify the tokens.
•	Next, the ast.parse function is used to parse the input_string into an abstract syntax tree (AST). The AST is then pretty-printed using the pprint function and printed using the ast.dump function. Finally, the compile and exec functions are used to execute the code represented by the AST.
