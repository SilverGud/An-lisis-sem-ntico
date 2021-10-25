from antlr.CoolListener import CoolListener
from myexceptions import *

class TreePrinter(CoolListener):
    def __init__(self, types={}):
        self.depth = 0
        self.types = types

    def enterEveryRule(self, ctx):
        self.depth = self.depth + 1
        s = ''
        for i in range(self.depth-1):
            s += " "
        try:
            print ("%s%s:%s" % (s, type(ctx).__name__[:-7], self.types[ctx]))
        except:
            print ("%s%s" % (s, type(ctx).__name__[:-7]))

    def exitEveryRule(self, ctx):
        self.depth = self.depth - 1
