# Generated from python_grammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .python_grammarParser import python_grammarParser
else:
    from python_grammarParser import python_grammarParser

# This class defines a complete listener for a parse tree produced by python_grammarParser.
class python_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by python_grammarParser#parse.
    def enterParse(self, ctx:python_grammarParser.ParseContext):
        pass

    # Exit a parse tree produced by python_grammarParser#parse.
    def exitParse(self, ctx:python_grammarParser.ParseContext):
        pass


    # Enter a parse tree produced by python_grammarParser#from_input.
    def enterFrom_input(self, ctx:python_grammarParser.From_inputContext):
        pass

    # Exit a parse tree produced by python_grammarParser#from_input.
    def exitFrom_input(self, ctx:python_grammarParser.From_inputContext):
        pass


    # Enter a parse tree produced by python_grammarParser#from_file.
    def enterFrom_file(self, ctx:python_grammarParser.From_fileContext):
        pass

    # Exit a parse tree produced by python_grammarParser#from_file.
    def exitFrom_file(self, ctx:python_grammarParser.From_fileContext):
        pass


    # Enter a parse tree produced by python_grammarParser#stat.
    def enterStat(self, ctx:python_grammarParser.StatContext):
        pass

    # Exit a parse tree produced by python_grammarParser#stat.
    def exitStat(self, ctx:python_grammarParser.StatContext):
        pass


    # Enter a parse tree produced by python_grammarParser#compound_stat.
    def enterCompound_stat(self, ctx:python_grammarParser.Compound_statContext):
        pass

    # Exit a parse tree produced by python_grammarParser#compound_stat.
    def exitCompound_stat(self, ctx:python_grammarParser.Compound_statContext):
        pass


    # Enter a parse tree produced by python_grammarParser#simple_stat.
    def enterSimple_stat(self, ctx:python_grammarParser.Simple_statContext):
        pass

    # Exit a parse tree produced by python_grammarParser#simple_stat.
    def exitSimple_stat(self, ctx:python_grammarParser.Simple_statContext):
        pass


    # Enter a parse tree produced by python_grammarParser#assignment.
    def enterAssignment(self, ctx:python_grammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by python_grammarParser#assignment.
    def exitAssignment(self, ctx:python_grammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by python_grammarParser#if_stat.
    def enterIf_stat(self, ctx:python_grammarParser.If_statContext):
        pass

    # Exit a parse tree produced by python_grammarParser#if_stat.
    def exitIf_stat(self, ctx:python_grammarParser.If_statContext):
        pass


    # Enter a parse tree produced by python_grammarParser#while_stat.
    def enterWhile_stat(self, ctx:python_grammarParser.While_statContext):
        pass

    # Exit a parse tree produced by python_grammarParser#while_stat.
    def exitWhile_stat(self, ctx:python_grammarParser.While_statContext):
        pass


    # Enter a parse tree produced by python_grammarParser#for_stat.
    def enterFor_stat(self, ctx:python_grammarParser.For_statContext):
        pass

    # Exit a parse tree produced by python_grammarParser#for_stat.
    def exitFor_stat(self, ctx:python_grammarParser.For_statContext):
        pass


    # Enter a parse tree produced by python_grammarParser#log.
    def enterLog(self, ctx:python_grammarParser.LogContext):
        pass

    # Exit a parse tree produced by python_grammarParser#log.
    def exitLog(self, ctx:python_grammarParser.LogContext):
        pass


    # Enter a parse tree produced by python_grammarParser#funcion.
    def enterFuncion(self, ctx:python_grammarParser.FuncionContext):
        pass

    # Exit a parse tree produced by python_grammarParser#funcion.
    def exitFuncion(self, ctx:python_grammarParser.FuncionContext):
        pass


    # Enter a parse tree produced by python_grammarParser#importar.
    def enterImportar(self, ctx:python_grammarParser.ImportarContext):
        pass

    # Exit a parse tree produced by python_grammarParser#importar.
    def exitImportar(self, ctx:python_grammarParser.ImportarContext):
        pass


    # Enter a parse tree produced by python_grammarParser#call_function.
    def enterCall_function(self, ctx:python_grammarParser.Call_functionContext):
        pass

    # Exit a parse tree produced by python_grammarParser#call_function.
    def exitCall_function(self, ctx:python_grammarParser.Call_functionContext):
        pass


    # Enter a parse tree produced by python_grammarParser#retornar.
    def enterRetornar(self, ctx:python_grammarParser.RetornarContext):
        pass

    # Exit a parse tree produced by python_grammarParser#retornar.
    def exitRetornar(self, ctx:python_grammarParser.RetornarContext):
        pass


    # Enter a parse tree produced by python_grammarParser#condition_block.
    def enterCondition_block(self, ctx:python_grammarParser.Condition_blockContext):
        pass

    # Exit a parse tree produced by python_grammarParser#condition_block.
    def exitCondition_block(self, ctx:python_grammarParser.Condition_blockContext):
        pass


    # Enter a parse tree produced by python_grammarParser#stat_block.
    def enterStat_block(self, ctx:python_grammarParser.Stat_blockContext):
        pass

    # Exit a parse tree produced by python_grammarParser#stat_block.
    def exitStat_block(self, ctx:python_grammarParser.Stat_blockContext):
        pass


    # Enter a parse tree produced by python_grammarParser#array.
    def enterArray(self, ctx:python_grammarParser.ArrayContext):
        pass

    # Exit a parse tree produced by python_grammarParser#array.
    def exitArray(self, ctx:python_grammarParser.ArrayContext):
        pass


    # Enter a parse tree produced by python_grammarParser#tuple.
    def enterTuple(self, ctx:python_grammarParser.TupleContext):
        pass

    # Exit a parse tree produced by python_grammarParser#tuple.
    def exitTuple(self, ctx:python_grammarParser.TupleContext):
        pass


    # Enter a parse tree produced by python_grammarParser#accessarray.
    def enterAccessarray(self, ctx:python_grammarParser.AccessarrayContext):
        pass

    # Exit a parse tree produced by python_grammarParser#accessarray.
    def exitAccessarray(self, ctx:python_grammarParser.AccessarrayContext):
        pass


    # Enter a parse tree produced by python_grammarParser#type_anotation.
    def enterType_anotation(self, ctx:python_grammarParser.Type_anotationContext):
        pass

    # Exit a parse tree produced by python_grammarParser#type_anotation.
    def exitType_anotation(self, ctx:python_grammarParser.Type_anotationContext):
        pass


    # Enter a parse tree produced by python_grammarParser#variable.
    def enterVariable(self, ctx:python_grammarParser.VariableContext):
        pass

    # Exit a parse tree produced by python_grammarParser#variable.
    def exitVariable(self, ctx:python_grammarParser.VariableContext):
        pass


    # Enter a parse tree produced by python_grammarParser#parametro.
    def enterParametro(self, ctx:python_grammarParser.ParametroContext):
        pass

    # Exit a parse tree produced by python_grammarParser#parametro.
    def exitParametro(self, ctx:python_grammarParser.ParametroContext):
        pass


    # Enter a parse tree produced by python_grammarParser#parExpr.
    def enterParExpr(self, ctx:python_grammarParser.ParExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#parExpr.
    def exitParExpr(self, ctx:python_grammarParser.ParExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#notExpr.
    def enterNotExpr(self, ctx:python_grammarParser.NotExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#notExpr.
    def exitNotExpr(self, ctx:python_grammarParser.NotExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:python_grammarParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:python_grammarParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:python_grammarParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:python_grammarParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#atomExpr.
    def enterAtomExpr(self, ctx:python_grammarParser.AtomExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#atomExpr.
    def exitAtomExpr(self, ctx:python_grammarParser.AtomExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#orExpr.
    def enterOrExpr(self, ctx:python_grammarParser.OrExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#orExpr.
    def exitOrExpr(self, ctx:python_grammarParser.OrExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:python_grammarParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:python_grammarParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#powExpr.
    def enterPowExpr(self, ctx:python_grammarParser.PowExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#powExpr.
    def exitPowExpr(self, ctx:python_grammarParser.PowExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#relationalExpr.
    def enterRelationalExpr(self, ctx:python_grammarParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#relationalExpr.
    def exitRelationalExpr(self, ctx:python_grammarParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#equalityExpr.
    def enterEqualityExpr(self, ctx:python_grammarParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#equalityExpr.
    def exitEqualityExpr(self, ctx:python_grammarParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#andExpr.
    def enterAndExpr(self, ctx:python_grammarParser.AndExprContext):
        pass

    # Exit a parse tree produced by python_grammarParser#andExpr.
    def exitAndExpr(self, ctx:python_grammarParser.AndExprContext):
        pass


    # Enter a parse tree produced by python_grammarParser#callAtom.
    def enterCallAtom(self, ctx:python_grammarParser.CallAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#callAtom.
    def exitCallAtom(self, ctx:python_grammarParser.CallAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#booleanAtom.
    def enterBooleanAtom(self, ctx:python_grammarParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#booleanAtom.
    def exitBooleanAtom(self, ctx:python_grammarParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#stringAtom.
    def enterStringAtom(self, ctx:python_grammarParser.StringAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#stringAtom.
    def exitStringAtom(self, ctx:python_grammarParser.StringAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#arrayAtom.
    def enterArrayAtom(self, ctx:python_grammarParser.ArrayAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#arrayAtom.
    def exitArrayAtom(self, ctx:python_grammarParser.ArrayAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#tupleAtom.
    def enterTupleAtom(self, ctx:python_grammarParser.TupleAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#tupleAtom.
    def exitTupleAtom(self, ctx:python_grammarParser.TupleAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#objetoAtom.
    def enterObjetoAtom(self, ctx:python_grammarParser.ObjetoAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#objetoAtom.
    def exitObjetoAtom(self, ctx:python_grammarParser.ObjetoAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#accessToarray.
    def enterAccessToarray(self, ctx:python_grammarParser.AccessToarrayContext):
        pass

    # Exit a parse tree produced by python_grammarParser#accessToarray.
    def exitAccessToarray(self, ctx:python_grammarParser.AccessToarrayContext):
        pass


    # Enter a parse tree produced by python_grammarParser#accessVariable.
    def enterAccessVariable(self, ctx:python_grammarParser.AccessVariableContext):
        pass

    # Exit a parse tree produced by python_grammarParser#accessVariable.
    def exitAccessVariable(self, ctx:python_grammarParser.AccessVariableContext):
        pass


    # Enter a parse tree produced by python_grammarParser#NULLAtom.
    def enterNULLAtom(self, ctx:python_grammarParser.NULLAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#NULLAtom.
    def exitNULLAtom(self, ctx:python_grammarParser.NULLAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#numberAtom.
    def enterNumberAtom(self, ctx:python_grammarParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#numberAtom.
    def exitNumberAtom(self, ctx:python_grammarParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#lambdaAtom.
    def enterLambdaAtom(self, ctx:python_grammarParser.LambdaAtomContext):
        pass

    # Exit a parse tree produced by python_grammarParser#lambdaAtom.
    def exitLambdaAtom(self, ctx:python_grammarParser.LambdaAtomContext):
        pass


    # Enter a parse tree produced by python_grammarParser#lambda_func.
    def enterLambda_func(self, ctx:python_grammarParser.Lambda_funcContext):
        pass

    # Exit a parse tree produced by python_grammarParser#lambda_func.
    def exitLambda_func(self, ctx:python_grammarParser.Lambda_funcContext):
        pass


    # Enter a parse tree produced by python_grammarParser#objeto.
    def enterObjeto(self, ctx:python_grammarParser.ObjetoContext):
        pass

    # Exit a parse tree produced by python_grammarParser#objeto.
    def exitObjeto(self, ctx:python_grammarParser.ObjetoContext):
        pass


    # Enter a parse tree produced by python_grammarParser#keyvalue.
    def enterKeyvalue(self, ctx:python_grammarParser.KeyvalueContext):
        pass

    # Exit a parse tree produced by python_grammarParser#keyvalue.
    def exitKeyvalue(self, ctx:python_grammarParser.KeyvalueContext):
        pass



del python_grammarParser