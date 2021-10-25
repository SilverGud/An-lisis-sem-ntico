from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
from myexceptions import *
import structure

class Typecheck(CoolListener):
    typeTable = {}
    varTable = {}
    

    def __init__(self):
        structure.setBaseClasses()

    def enterAtribute(self, ctx: CoolParser.AtributeContext):
        self.varTable[ctx.ID().getText()] = ctx.TYPE().getText()    

    def exitInteger(self, ctx: CoolParser.IntegerContext):
        self.typeTable[ctx] = structure._allClasses["Int"]
    
    def exitString(self, ctx: CoolParser.StringContext):
        self.typeTable[ctx] = structure._allClasses["String"]
    
    def exitBool(self, ctx:CoolParser.BoolContext):
        self.typeTable[ctx] = structure._allClasses["Bool"]

    def exitBase(self, ctx: CoolParser.BaseContext):
        self.typeTable[ctx] = self.typeTable[ctx.getChild(0)]

    def exitObject(self, ctx: CoolParser.ObjectContext):
        self.typeTable[ctx] = self.varTable[ctx.ID().getText()]

    def exitAdd(self, ctx: CoolParser.AddContext):
        if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
            self.typeTable[ctx] = "Int"
        else:
            raise TypeCheckMismatch

    def exitMult(self, ctx: CoolParser.MultContext):
        if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
            self.typeTable[ctx] = "Int"
        else:
            raise Exception("Type error")
    
    def exitDiv(self, ctx: CoolParser.DivContext):    
        if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
            self.typeTable[ctx] = "Int"
        else:
            raise Exception("Type error")
    
    def exitSub(self, ctx: CoolParser.SubContext):     
        if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
            self.typeTable[ctx] = "Int"
        else:
            raise Exception("Type error")

    def exitLt(self, ctx: CoolParser.LtContext):
        if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
            self.typeTable[ctx] = "Bool"
        else:
            raise TypeCheckMismatch
    
    def exitLe(self, ctx: CoolParser.LeContext):
        if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] == "Int":
            self.typeTable[ctx] = "Bool"
        else:
            raise TypeCheckMismatch
    
    def exitEq(self, ctx: CoolParser.EqContext):
        if self.typeTable[ctx.expr(0)] == "Int" and self.typeTable[ctx.expr(1)] != "Int":
            raise TypeCheckMismatch

        elif self.typeTable[ctx.expr(0)] == "String" and self.typeTable[ctx.expr(1)] != "String":
            raise TypeCheckMismatch
        
        elif self.typeTable[ctx.expr(0)] == "Bool" and self.typeTable[ctx.expr(1)] != "Bool":
            raise TypeCheckMismatch

        else:
            self.typeTable[ctx] = "Bool"
    
    def exitNot(self, ctx: CoolParser.NotContext):
        if self.typeTable[ctx.expr()] == "Bool":
            self.typeTable[ctx] = "Bool"
        else:
            raise Exception("Type error")
    
    def exitIf(self, ctx: CoolParser.IfContext):
        if self.typeTable[ctx.expr(0)] == "Bool":
            self.typeTable[ctx] = "Bool"
        else:
            raise Exception("Type error")
        
        if structure._allClasses[ctx.expr(1)] == None:
             raise Exception("Type error")

    
    def exitWhile(self, ctx: CoolParser.WhileContext):
        self.typeTable[ctx] = "Object"

        if self.typeTable[ctx.expr(0)] == "Bool":
            if structure._allClasses[self.typeTable[ctx.expr(1)].name] == None:
                raise MethodNotFound
        else:
            raise TypeCheckMismatch

    def exitBlock(self, ctx: CoolParser.BlockContext):
        last = 0
        for i in ctx.expr():
            if structure._allClasses[self.typeTable[i].name] == None:
                raise Exception("Type error")
            last = i  

        self.typeTable[ctx] = self.typeTable[last].name

    def exitIsvoid(self, ctx: CoolParser.IsvoidContext):
        if structure._allClasses[self.typeTable[ctx.expr()].name] != None:
                self.typeTable[ctx] = "Bool"
        else:
            raise Exception("Type error")
    
    def exitNeg(self, ctx: CoolParser.NegContext):
        if self.typeTable[ctx.expr()] == "Int":
            self.typeTable[ctx] = "Int"
        else:
            raise Exception("Type error")
    
    def exitCall(self, ctx: CoolParser.CallContext):
        for i in ctx.expr():
            if structure._allClasses[self.typeTable[i].name] == ctx.ID():
                raise Exception("Type error")
            
        self.typeTable[ctx] = ctx.ID()
    
    def exitLet(self, ctx: CoolParser.LetContext):
        print("Hola Let")
    
    def exitCase(self, ctx: CoolParser.CaseContext):
        print("Hola Case")
    
    def exitAssign(self, ctx: CoolParser.AssignContext):
        if self.varTable[ctx.ID().getText()] != structure._allClasses[self.typeTable[ctx.expr()].name]:
            raise DoesNotConform

    def exitNew(self, ctx: CoolParser.NewContext):
        if ctx.TYPE().getText() not in self.typeTable:
            raise TypeNotFound