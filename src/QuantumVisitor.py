# Generated from Quantum.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .QuantumParser import QuantumParser
else:
    from QuantumParser import QuantumParser

# This class defines a complete generic visitor for a parse tree produced by QuantumParser.

class QuantumVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QuantumParser#prog.
    def visitProg(self, ctx:QuantumParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#stmtDeclareQubit.
    def visitStmtDeclareQubit(self, ctx:QuantumParser.StmtDeclareQubitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#stmtUpdateSymbol.
    def visitStmtUpdateSymbol(self, ctx:QuantumParser.StmtUpdateSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#stmtApplyGate.
    def visitStmtApplyGate(self, ctx:QuantumParser.StmtApplyGateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#stmtMeasure.
    def visitStmtMeasure(self, ctx:QuantumParser.StmtMeasureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#stmtGrover.
    def visitStmtGrover(self, ctx:QuantumParser.StmtGroverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#stmtExpr.
    def visitStmtExpr(self, ctx:QuantumParser.StmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#qubitDecl.
    def visitQubitDecl(self, ctx:QuantumParser.QubitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#applyGate.
    def visitApplyGate(self, ctx:QuantumParser.ApplyGateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#applyGateStmt.
    def visitApplyGateStmt(self, ctx:QuantumParser.ApplyGateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#measureStmt.
    def visitMeasureStmt(self, ctx:QuantumParser.MeasureStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#groverBlock.
    def visitGroverBlock(self, ctx:QuantumParser.GroverBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#block.
    def visitBlock(self, ctx:QuantumParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#type.
    def visitType(self, ctx:QuantumParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#intDivExpr.
    def visitIntDivExpr(self, ctx:QuantumParser.IntDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:QuantumParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#modExpr.
    def visitModExpr(self, ctx:QuantumParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#addExpr.
    def visitAddExpr(self, ctx:QuantumParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#numberExpr.
    def visitNumberExpr(self, ctx:QuantumParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#functionCallExpr.
    def visitFunctionCallExpr(self, ctx:QuantumParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#mulExpr.
    def visitMulExpr(self, ctx:QuantumParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#divExpr.
    def visitDivExpr(self, ctx:QuantumParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#powExpr.
    def visitPowExpr(self, ctx:QuantumParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#subExpr.
    def visitSubExpr(self, ctx:QuantumParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#parenExpr.
    def visitParenExpr(self, ctx:QuantumParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#idExpr.
    def visitIdExpr(self, ctx:QuantumParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#functionCall.
    def visitFunctionCall(self, ctx:QuantumParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#arg.
    def visitArg(self, ctx:QuantumParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#argList.
    def visitArgList(self, ctx:QuantumParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#idList.
    def visitIdList(self, ctx:QuantumParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumParser#gate.
    def visitGate(self, ctx:QuantumParser.GateContext):
        return self.visitChildren(ctx)



del QuantumParser