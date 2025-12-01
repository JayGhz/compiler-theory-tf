# Generated from Quantum.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QuantumParser import QuantumParser
else:
    from QuantumParser import QuantumParser

# This class defines a complete listener for a parse tree produced by QuantumParser.
class QuantumListener(ParseTreeListener):

    # Enter a parse tree produced by QuantumParser#prog.
    def enterProg(self, ctx:QuantumParser.ProgContext):
        pass

    # Exit a parse tree produced by QuantumParser#prog.
    def exitProg(self, ctx:QuantumParser.ProgContext):
        pass


    # Enter a parse tree produced by QuantumParser#stmtDeclareQubit.
    def enterStmtDeclareQubit(self, ctx:QuantumParser.StmtDeclareQubitContext):
        pass

    # Exit a parse tree produced by QuantumParser#stmtDeclareQubit.
    def exitStmtDeclareQubit(self, ctx:QuantumParser.StmtDeclareQubitContext):
        pass


    # Enter a parse tree produced by QuantumParser#stmtUpdateSymbol.
    def enterStmtUpdateSymbol(self, ctx:QuantumParser.StmtUpdateSymbolContext):
        pass

    # Exit a parse tree produced by QuantumParser#stmtUpdateSymbol.
    def exitStmtUpdateSymbol(self, ctx:QuantumParser.StmtUpdateSymbolContext):
        pass


    # Enter a parse tree produced by QuantumParser#stmtApplyGate.
    def enterStmtApplyGate(self, ctx:QuantumParser.StmtApplyGateContext):
        pass

    # Exit a parse tree produced by QuantumParser#stmtApplyGate.
    def exitStmtApplyGate(self, ctx:QuantumParser.StmtApplyGateContext):
        pass


    # Enter a parse tree produced by QuantumParser#stmtMeasure.
    def enterStmtMeasure(self, ctx:QuantumParser.StmtMeasureContext):
        pass

    # Exit a parse tree produced by QuantumParser#stmtMeasure.
    def exitStmtMeasure(self, ctx:QuantumParser.StmtMeasureContext):
        pass


    # Enter a parse tree produced by QuantumParser#stmtGrover.
    def enterStmtGrover(self, ctx:QuantumParser.StmtGroverContext):
        pass

    # Exit a parse tree produced by QuantumParser#stmtGrover.
    def exitStmtGrover(self, ctx:QuantumParser.StmtGroverContext):
        pass


    # Enter a parse tree produced by QuantumParser#stmtExpr.
    def enterStmtExpr(self, ctx:QuantumParser.StmtExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#stmtExpr.
    def exitStmtExpr(self, ctx:QuantumParser.StmtExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#qubitDecl.
    def enterQubitDecl(self, ctx:QuantumParser.QubitDeclContext):
        pass

    # Exit a parse tree produced by QuantumParser#qubitDecl.
    def exitQubitDecl(self, ctx:QuantumParser.QubitDeclContext):
        pass


    # Enter a parse tree produced by QuantumParser#applyGate.
    def enterApplyGate(self, ctx:QuantumParser.ApplyGateContext):
        pass

    # Exit a parse tree produced by QuantumParser#applyGate.
    def exitApplyGate(self, ctx:QuantumParser.ApplyGateContext):
        pass


    # Enter a parse tree produced by QuantumParser#applyGateStmt.
    def enterApplyGateStmt(self, ctx:QuantumParser.ApplyGateStmtContext):
        pass

    # Exit a parse tree produced by QuantumParser#applyGateStmt.
    def exitApplyGateStmt(self, ctx:QuantumParser.ApplyGateStmtContext):
        pass


    # Enter a parse tree produced by QuantumParser#measureStmt.
    def enterMeasureStmt(self, ctx:QuantumParser.MeasureStmtContext):
        pass

    # Exit a parse tree produced by QuantumParser#measureStmt.
    def exitMeasureStmt(self, ctx:QuantumParser.MeasureStmtContext):
        pass


    # Enter a parse tree produced by QuantumParser#groverBlock.
    def enterGroverBlock(self, ctx:QuantumParser.GroverBlockContext):
        pass

    # Exit a parse tree produced by QuantumParser#groverBlock.
    def exitGroverBlock(self, ctx:QuantumParser.GroverBlockContext):
        pass


    # Enter a parse tree produced by QuantumParser#block.
    def enterBlock(self, ctx:QuantumParser.BlockContext):
        pass

    # Exit a parse tree produced by QuantumParser#block.
    def exitBlock(self, ctx:QuantumParser.BlockContext):
        pass


    # Enter a parse tree produced by QuantumParser#type.
    def enterType(self, ctx:QuantumParser.TypeContext):
        pass

    # Exit a parse tree produced by QuantumParser#type.
    def exitType(self, ctx:QuantumParser.TypeContext):
        pass


    # Enter a parse tree produced by QuantumParser#intDivExpr.
    def enterIntDivExpr(self, ctx:QuantumParser.IntDivExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#intDivExpr.
    def exitIntDivExpr(self, ctx:QuantumParser.IntDivExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:QuantumParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:QuantumParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#modExpr.
    def enterModExpr(self, ctx:QuantumParser.ModExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#modExpr.
    def exitModExpr(self, ctx:QuantumParser.ModExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#addExpr.
    def enterAddExpr(self, ctx:QuantumParser.AddExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#addExpr.
    def exitAddExpr(self, ctx:QuantumParser.AddExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#numberExpr.
    def enterNumberExpr(self, ctx:QuantumParser.NumberExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#numberExpr.
    def exitNumberExpr(self, ctx:QuantumParser.NumberExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#functionCallExpr.
    def enterFunctionCallExpr(self, ctx:QuantumParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#functionCallExpr.
    def exitFunctionCallExpr(self, ctx:QuantumParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#mulExpr.
    def enterMulExpr(self, ctx:QuantumParser.MulExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#mulExpr.
    def exitMulExpr(self, ctx:QuantumParser.MulExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#divExpr.
    def enterDivExpr(self, ctx:QuantumParser.DivExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#divExpr.
    def exitDivExpr(self, ctx:QuantumParser.DivExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#powExpr.
    def enterPowExpr(self, ctx:QuantumParser.PowExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#powExpr.
    def exitPowExpr(self, ctx:QuantumParser.PowExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#subExpr.
    def enterSubExpr(self, ctx:QuantumParser.SubExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#subExpr.
    def exitSubExpr(self, ctx:QuantumParser.SubExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#parenExpr.
    def enterParenExpr(self, ctx:QuantumParser.ParenExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#parenExpr.
    def exitParenExpr(self, ctx:QuantumParser.ParenExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#idExpr.
    def enterIdExpr(self, ctx:QuantumParser.IdExprContext):
        pass

    # Exit a parse tree produced by QuantumParser#idExpr.
    def exitIdExpr(self, ctx:QuantumParser.IdExprContext):
        pass


    # Enter a parse tree produced by QuantumParser#functionCall.
    def enterFunctionCall(self, ctx:QuantumParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by QuantumParser#functionCall.
    def exitFunctionCall(self, ctx:QuantumParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by QuantumParser#arg.
    def enterArg(self, ctx:QuantumParser.ArgContext):
        pass

    # Exit a parse tree produced by QuantumParser#arg.
    def exitArg(self, ctx:QuantumParser.ArgContext):
        pass


    # Enter a parse tree produced by QuantumParser#argList.
    def enterArgList(self, ctx:QuantumParser.ArgListContext):
        pass

    # Exit a parse tree produced by QuantumParser#argList.
    def exitArgList(self, ctx:QuantumParser.ArgListContext):
        pass


    # Enter a parse tree produced by QuantumParser#idList.
    def enterIdList(self, ctx:QuantumParser.IdListContext):
        pass

    # Exit a parse tree produced by QuantumParser#idList.
    def exitIdList(self, ctx:QuantumParser.IdListContext):
        pass


    # Enter a parse tree produced by QuantumParser#gate.
    def enterGate(self, ctx:QuantumParser.GateContext):
        pass

    # Exit a parse tree produced by QuantumParser#gate.
    def exitGate(self, ctx:QuantumParser.GateContext):
        pass



del QuantumParser