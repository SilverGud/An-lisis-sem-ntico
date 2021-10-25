from antlr.CoolListener import CoolListener
from antlr.CoolParser import CoolParser


class Declarations(CoolListener):
    idTable = {}

    def exitAtribute(self, ctx: CoolParser.AtributeContext):
        self.idtable[ctx.ID().getText()] = ctx.TYPE().getText()