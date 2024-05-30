# POPL_Parser_project


Group Name: Parser Puzzlers

Programing Language: Python3

GitHub: https://github.com/cscranton5/POPL_Parser_project 

Group Members:

1. Carter Scranton (cscranton5)

2. Allan Jones Jr (allanjones24)

3. Shakthivel Gnanasekaran (sgckm on branch)

5. Clayton Wiemann (claytonwiemann)

6. Atul Krishnadas (yugi957)


Helpfull Resources:

Antlr Mega Tutorial:
https://tomassetti.me/antlr-mega-tutorial/#chapter23

To run the project:

Ensure you have the proper libraries installed (Antlr4, pip install antlr4-python3-runtime AND antlr4-tools)
This library is an open-source library made by Yuval Shavit for ready-made counter for indent/dedent.

1. Generate Python files from g4:
1.   a) inside "Project" directory, run antlr4 -Dlanguage=Python3 Python.g4
2. Run the parser:
2.   a) same directory, run python Parse.py

Using the script we've created, "tokens.py", you can display the tokens and their corresponding identifiers that the lexer identifies. This was very useful for debugging.

For both tokens.py and parse.py, the file you would like to parse is editable through modifying the file assigned in the code.
For parse.py, we did implement command line argument handling for files.

After running, this will bring up the parsing tree gui as well as print a flat text format

The image we've included in the resources directory has a transparent background. If you open it in a browser (We confirmed in Firefox) then it will have a white background where you can zoom in and look through the tree. The tree is also scrollable after simply running the script



