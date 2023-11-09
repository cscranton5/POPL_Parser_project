# Generated from Python.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,4,0,23,8,0,11,0,12,0,24,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,46,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        57,8,2,10,2,12,2,60,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,3,5,70,8,
        5,1,5,1,5,1,6,1,6,1,6,5,6,77,8,6,10,6,12,6,80,9,6,1,7,1,7,1,7,0,
        1,4,8,0,2,4,6,8,10,12,14,0,3,1,0,11,12,1,0,13,14,1,0,3,7,90,0,22,
        1,0,0,0,2,33,1,0,0,0,4,45,1,0,0,0,6,61,1,0,0,0,8,65,1,0,0,0,10,67,
        1,0,0,0,12,73,1,0,0,0,14,81,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,
        18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,23,1,0,0,0,21,23,5,
        19,0,0,22,17,1,0,0,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,0,0,0,24,
        25,1,0,0,0,25,1,1,0,0,0,26,27,3,4,2,0,27,28,5,19,0,0,28,34,1,0,0,
        0,29,30,3,6,3,0,30,31,5,19,0,0,31,34,1,0,0,0,32,34,5,19,0,0,33,26,
        1,0,0,0,33,29,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,6,2,-1,0,
        36,46,5,16,0,0,37,46,5,18,0,0,38,46,5,17,0,0,39,46,3,10,5,0,40,46,
        3,14,7,0,41,42,5,1,0,0,42,43,3,4,2,0,43,44,5,2,0,0,44,46,1,0,0,0,
        45,35,1,0,0,0,45,37,1,0,0,0,45,38,1,0,0,0,45,39,1,0,0,0,45,40,1,
        0,0,0,45,41,1,0,0,0,46,58,1,0,0,0,47,48,10,9,0,0,48,49,7,0,0,0,49,
        57,3,4,2,10,50,51,10,8,0,0,51,52,7,1,0,0,52,57,3,4,2,9,53,54,10,
        7,0,0,54,55,5,15,0,0,55,57,3,4,2,8,56,47,1,0,0,0,56,50,1,0,0,0,56,
        53,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,5,1,0,0,
        0,60,58,1,0,0,0,61,62,3,14,7,0,62,63,3,8,4,0,63,64,3,4,2,0,64,7,
        1,0,0,0,65,66,7,2,0,0,66,9,1,0,0,0,67,69,5,8,0,0,68,70,3,12,6,0,
        69,68,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,5,9,0,0,72,11,1,
        0,0,0,73,78,3,4,2,0,74,75,5,10,0,0,75,77,3,4,2,0,76,74,1,0,0,0,77,
        80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,13,1,0,0,0,80,78,1,0,0,
        0,81,82,5,20,0,0,82,15,1,0,0,0,9,19,22,24,33,45,56,58,69,78
    ]

class PythonParser ( Parser ):

    grammarFileName = "Python.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "'+='", "'-='", "'*='", 
                     "'/='", "'['", "']'", "','", "'*'", "'/'", "'+'", "'-'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MULT", "DIV", 
                      "ADD", "SUB", "MOD", "INT", "STRING", "FLOAT", "NEWLINE", 
                      "VAR", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_assignment = 3
    RULE_assignment_operator = 4
    RULE_list_expr = 5
    RULE_elements = 6
    RULE_variable = 7

    ruleNames =  [ "prog", "statement", "expr", "assignment", "assignment_operator", 
                   "list_expr", "elements", "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    MULT=11
    DIV=12
    ADD=13
    SUB=14
    MOD=15
    INT=16
    STRING=17
    FLOAT=18
    NEWLINE=19
    VAR=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParser.NEWLINE)
            else:
                return self.getToken(PythonParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(PythonParser.StatementContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = PythonParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 17 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 16
                            self.statement()

                        else:
                            raise NoViableAltException(self)
                        self.state = 19 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                    pass

                elif la_ == 2:
                    self.state = 21
                    self.match(PythonParser.NEWLINE)
                    pass


                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2031874) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(PythonParser.NEWLINE, 0)

        def assignment(self):
            return self.getTypedRuleContext(PythonParser.AssignmentContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(PythonParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.assignment()
                self.state = 30
                self.match(PythonParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(PythonParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(PythonParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class ModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)

        def MOD(self):
            return self.getToken(PythonParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)

        def MULT(self):
            return self.getToken(PythonParser.MULT, 0)
        def DIV(self):
            return self.getToken(PythonParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)

        def ADD(self):
            return self.getToken(PythonParser.ADD, 0)
        def SUB(self):
            return self.getToken(PythonParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(PythonParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_expr(self):
            return self.getTypedRuleContext(PythonParser.List_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PythonParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PythonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PythonParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = PythonParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.match(PythonParser.INT)
                pass
            elif token in [18]:
                localctx = PythonParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(PythonParser.FLOAT)
                pass
            elif token in [17]:
                localctx = PythonParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(PythonParser.STRING)
                pass
            elif token in [8]:
                localctx = PythonParser.ListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.list_expr()
                pass
            elif token in [20]:
                localctx = PythonParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.variable()
                pass
            elif token in [1]:
                localctx = PythonParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(PythonParser.T__0)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(PythonParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 56
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = PythonParser.MulDivContext(self, PythonParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 48
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = PythonParser.AddSubContext(self, PythonParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 51
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = PythonParser.ModContext(self, PythonParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 54
                        self.match(PythonParser.MOD)
                        self.state = 55
                        self.expr(8)
                        pass

             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(PythonParser.VariableContext,0)


        def assignment_operator(self):
            return self.getTypedRuleContext(PythonParser.Assignment_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PythonParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.variable()
            self.state = 62
            self.assignment_operator()
            self.state = 63
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = PythonParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 248) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(PythonParser.ElementsContext,0)


        def getRuleIndex(self):
            return PythonParser.RULE_list_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_expr" ):
                listener.enterList_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_expr" ):
                listener.exitList_expr(self)




    def list_expr(self):

        localctx = PythonParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(PythonParser.T__7)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1507586) != 0):
                self.state = 68
                self.elements()


            self.state = 71
            self.match(PythonParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)




    def elements(self):

        localctx = PythonParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.expr(0)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 74
                self.match(PythonParser.T__9)
                self.state = 75
                self.expr(0)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(PythonParser.VAR, 0)

        def getRuleIndex(self):
            return PythonParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = PythonParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(PythonParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




