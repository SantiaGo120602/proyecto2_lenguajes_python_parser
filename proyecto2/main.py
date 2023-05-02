__author__ = 'jszheng'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from python_grammarLexer import python_grammarLexer
from python_grammarParser import python_grammarParser
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class MyErrorStrategy(BailErrorStrategy):
    def recover(self, recognizer:Parser, e:RecognitionException):
        recognizer._errHandler.reportError(recognizer,e)
        super().recover(recognizer,e)

class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        symbol = str(offendingSymbol)
        errorsymbol = ""
        comas = 0
        for c in symbol:
            if c == "'":
                errorsymbol+=c
                comas+=1
            if comas ==1 and c!="'":
                errorsymbol+=c

        symbol = str(msg)
        añadir = False
        correcSymbol = ""
        for i in range(len(symbol)):
            if añadir:
                correcSymbol+=symbol[i]
            if symbol[i] == " " and symbol[i-1] == "g":
                añadir = True

        print(f'<{line},{column}> Error sintáctico: Se encontró: {errorsymbol}. Se esperaba: {correcSymbol}')

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

if __name__ == '__main__':
    

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    if len(sys.argv) > 1:
            input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = python_grammarLexer(input_stream)
    lexer.removeErrorListeners()
    lexer._listeners = [ MyErrorListener() ]
    token_stream = CommonTokenStream(lexer)
    parser = python_grammarParser(token_stream)
    parser._listeners = [ MyErrorListener() ]
    parser._errHandler = MyErrorStrategy()
    try:
        tree = parser.parse()
        print("El análisis sintáctico ha finalizado exitosamente.")
    except ParseCancellationException:
        pass

