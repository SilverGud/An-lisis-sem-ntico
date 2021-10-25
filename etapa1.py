import sys
import unittest

from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser
from antlr.CoolListener import CoolListener
from myexceptions import *

from etapa1Listener import Listener

def parseCase(caseName):
    parser = CoolParser(
        CommonTokenStream(
            CoolLexer(FileStream("./resources/semantic/input/%s.cool" % caseName))
        )
    )
    return parser.program()


class CoolTests(unittest.TestCase):
    def setUp(self):
        self.walker = ParseTreeWalker()

    """
    las purebas seran realizadas de la siguiente manera

    def prueba#(self):
        tree = parseCase("nombrecaso")
        with self.assertRaises(Prueba a usar):
            self.walker.walk(listener a usar(), tree)
    
    """ 

    #Prueba caso nomain
    def test1(self):
        tree = parseCase("nomain")
        with self.assertRaises(NoMainException):
            print(self.walker.walk(Listener(), tree))

    #Prueba caso badredefineint
    def test2(self):
        tree = parseCase("badredefineint")
        with self.assertRaises(RedefineBasicClassException):
            self.walker.walk(Listener(), tree)

    #Prueba caso anattributenamedself
    def test3(self):
        tree = parseCase("anattributenamedself")
        with self.assertRaises(SelfVariableException):
            self.walker.walk(Listener(), tree)

    #Prueba caso letself
    def test4(self):
        tree = parseCase("letself")
        with self.assertRaises(SelfVariableException):
            self.walker.walk(Listener(), tree)

    #Prueba caso inheritsbool
    def test5(self):
        tree = parseCase("inheritsbool")
        with self.assertRaises(InvalidInheritsException):
            self.walker.walk(Listener(), tree)

    #Prueba caso inheritsselftype
    def test6(self):
        tree = parseCase("inheritsselftype")
        with self.assertRaises(InvalidInheritsException):
            self.walker.walk(Listener(), tree)

    #Prueba caso inheritsstring
    def test7(self):
        tree = parseCase("inheritsstring")
        with self.assertRaises(InvalidInheritsException):
            self.walker.walk(Listener(), tree)

    #Prueba caso redefinedobject
    def test8(self):
        tree = parseCase("redefinedobject")
        with self.assertRaises(RedefineBasicClassException):
            self.walker.walk(Listener(), tree)

    #Prueba caso self-assignment
    def test9(self):
        tree = parseCase("self-assignment")
        with self.assertRaises(SelfAssignmentException):
            self.walker.walk(Listener(), tree)

    #Prueba caso selfinformalparameter
    def test10(self):
        tree = parseCase("selfinformalparameter")
        with self.assertRaises(SelfVariableException):
            self.walker.walk(Listener(), tree)

    #Prueba caso selftyperedeclared
    def test11(self):
        tree = parseCase("selftyperedeclared")
        with self.assertRaises(RedefineBasicClassException):
            self.walker.walk(Listener(), tree)

    #Prueba caso selftypeparameterposition
    def test12(self):
        tree = parseCase("selftypeparameterposition")
        with self.assertRaises(SelftypeInvalidUseException):
            self.walker.walk(Listener(), tree)


if __name__ == "__main__":
    unittest.main()
