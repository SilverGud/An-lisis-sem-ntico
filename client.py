from antlr.CoolLexer import *
from antlr.CoolParser import *
from antlr4 import *

from typecheck import Typecheck
from klassListener import KlassListener

def main(file):
    parser = CoolParser(CommonTokenStream(CoolLexer(FileStream(file))))
    tree = parser.program()

    walker = ParseTreeWalker()
    typecheck = Typecheck()
    walker.walk(typecheck, tree)

if __name__ == '__main__':
    main("./resources/semantic/input/assignnoconform.cool")
