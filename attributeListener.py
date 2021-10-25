from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser
from myexceptions import *
import structure

class AttributeListener(CoolListener):
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
    
    def exitAssign(self, ctx: CoolParser.AssignContext):
        if self.varTable[ctx.ID().getText()] != structure._allClasses[self.typeTable[ctx.expr()].name]:
            raise DoesNotConform

    def exitNew(self, ctx: CoolParser.NewContext):
        
        if ctx.TYPE().getText() not in self.typeTable:
                raise DoesNotConform

        
        
    