from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser
from antlr.CoolListener import CoolListener
from myexceptions import *

class Listener(CoolListener):
    # No Main
    tiene_main = False

    def enterKlass(self, ctx: CoolParser.KlassContext):
        if ctx.TYPE(0).getText() == "Main":
            self.tiene_main = True

        if ctx.TYPE(1) != None and (
            ctx.TYPE(1).getText() == "Bool"
            or ctx.TYPE(1).getText() == "String"
            or ctx.TYPE(1).getText() == "SELF_TYPE"
        ):
            raise InvalidInheritsException

        if ctx.TYPE(0).getText() == "Object":
            raise RedefineBasicClassException

        if ctx.TYPE(0).getText() == "Int":
            raise RedefineBasicClassException

        if ctx.TYPE(0).getText() == "SELF_TYPE":
            raise RedefineBasicClassException

    def enterFormal(self, ctx: CoolParser.FormalContext):
        if ctx.ID().getText() == "self":
            raise SelfVariableException

        if ctx.TYPE().getText() == "SELF_TYPE":
            raise SelftypeInvalidUseException

    def enterAtribute(self, ctx: CoolParser.AtributeContext):
        if ctx.ID().getText() == "self":
            raise SelfVariableException

    def enterLet(self, ctx: CoolParser.LetContext):
        if ctx.ID(0).getText() == "self":
            raise SelfVariableException

    def enterAssign(self, ctx: CoolParser.AssignContext):
        if ctx.ID().getText() == "self":
            raise SelfAssignmentException

    def exitProgram(self, ctx: CoolParser.ProgramContext):
        if not self.tiene_main:
            raise NoMainException