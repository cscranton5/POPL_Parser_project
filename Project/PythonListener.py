# Generated from Python.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#prog.
    def enterProg(self, ctx:PythonParser.ProgContext):
        pass

    # Exit a parse tree produced by PythonParser#prog.
    def exitProg(self, ctx:PythonParser.ProgContext):
        pass


    # Enter a parse tree produced by PythonParser#statement.
    def enterStatement(self, ctx:PythonParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParser#statement.
    def exitStatement(self, ctx:PythonParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonParser#Float.
    def enterFloat(self, ctx:PythonParser.FloatContext):
        pass

    # Exit a parse tree produced by PythonParser#Float.
    def exitFloat(self, ctx:PythonParser.FloatContext):
        pass


    # Enter a parse tree produced by PythonParser#Mod.
    def enterMod(self, ctx:PythonParser.ModContext):
        pass

    # Exit a parse tree produced by PythonParser#Mod.
    def exitMod(self, ctx:PythonParser.ModContext):
        pass


    # Enter a parse tree produced by PythonParser#MulDiv.
    def enterMulDiv(self, ctx:PythonParser.MulDivContext):
        pass

    # Exit a parse tree produced by PythonParser#MulDiv.
    def exitMulDiv(self, ctx:PythonParser.MulDivContext):
        pass


    # Enter a parse tree produced by PythonParser#AddSub.
    def enterAddSub(self, ctx:PythonParser.AddSubContext):
        pass

    # Exit a parse tree produced by PythonParser#AddSub.
    def exitAddSub(self, ctx:PythonParser.AddSubContext):
        pass


    # Enter a parse tree produced by PythonParser#Parens.
    def enterParens(self, ctx:PythonParser.ParensContext):
        pass

    # Exit a parse tree produced by PythonParser#Parens.
    def exitParens(self, ctx:PythonParser.ParensContext):
        pass


    # Enter a parse tree produced by PythonParser#VarExpr.
    def enterVarExpr(self, ctx:PythonParser.VarExprContext):
        pass

    # Exit a parse tree produced by PythonParser#VarExpr.
    def exitVarExpr(self, ctx:PythonParser.VarExprContext):
        pass


    # Enter a parse tree produced by PythonParser#List.
    def enterList(self, ctx:PythonParser.ListContext):
        pass

    # Exit a parse tree produced by PythonParser#List.
    def exitList(self, ctx:PythonParser.ListContext):
        pass


    # Enter a parse tree produced by PythonParser#String.
    def enterString(self, ctx:PythonParser.StringContext):
        pass

    # Exit a parse tree produced by PythonParser#String.
    def exitString(self, ctx:PythonParser.StringContext):
        pass


    # Enter a parse tree produced by PythonParser#Int.
    def enterInt(self, ctx:PythonParser.IntContext):
        pass

    # Exit a parse tree produced by PythonParser#Int.
    def exitInt(self, ctx:PythonParser.IntContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment.
    def enterAssignment(self, ctx:PythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment.
    def exitAssignment(self, ctx:PythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment_operator.
    def enterAssignment_operator(self, ctx:PythonParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment_operator.
    def exitAssignment_operator(self, ctx:PythonParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by PythonParser#list_expr.
    def enterList_expr(self, ctx:PythonParser.List_exprContext):
        pass

    # Exit a parse tree produced by PythonParser#list_expr.
    def exitList_expr(self, ctx:PythonParser.List_exprContext):
        pass


    # Enter a parse tree produced by PythonParser#elements.
    def enterElements(self, ctx:PythonParser.ElementsContext):
        pass

    # Exit a parse tree produced by PythonParser#elements.
    def exitElements(self, ctx:PythonParser.ElementsContext):
        pass


    # Enter a parse tree produced by PythonParser#variable.
    def enterVariable(self, ctx:PythonParser.VariableContext):
        pass

    # Exit a parse tree produced by PythonParser#variable.
    def exitVariable(self, ctx:PythonParser.VariableContext):
        pass



del PythonParser