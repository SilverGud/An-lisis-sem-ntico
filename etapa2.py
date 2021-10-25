import sys
import unittest

from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser
from antlr.CoolListener import CoolListener
from myexceptions import *

import typecheck
import klassListener
import methodListener
import attributeListener

class Listener(CoolListener):
    c = []
    
def parseCase(caseName):
    parser = CoolParser(CommonTokenStream(CoolLexer(FileStream("./resources/semantic/input/%s.cool" % caseName))))
    return parser.program()

class CoolTests(unittest.TestCase):

    #Crea el walker
    def setUp(self): 
        self.walker = ParseTreeWalker()

    """
    las purebas seran realizadas de la siguiente manera

    def prueba#(self):
        tree = parseCase("nombrecaso")
        with self.assertRaises(Prueba a usar):
            self.walker.walk(listener a usar, tree)
    
    """    

    #Prueba caso assignnoconform
    def test1(self): 
        tree = parseCase("assignnoconform")
        with self.assertRaises(DoesNotConform):
            self.walker.walk(attributeListener.AttributeListener(), tree)

    #Prueba caso attrbadinit
    def test2(self): 
        tree = parseCase("attrbadinit")
        with self.assertRaises(UndeclaredIdentifier):
            self.walker.walk(Listener(), tree)

    #Prueba caso attroverride
    def test3(self): 
        tree = parseCase("attroverride")
        with self.assertRaises(NotSupported):
            self.walker.walk(klassListener.KlassListener(), tree)

    #Prueba caso badargs1
    def test4(self): 
        tree = parseCase("badargs1")
        with self.assertRaises(DoesNotConform):
            self.walker.walk(methodListener.MethodListener(), tree)

    #Prueba caso badarith
    def test5(self): 
        tree = parseCase("badarith")
        with self.assertRaises(TypeCheckMismatch):
            self.walker.walk(typecheck.Typecheck(), tree)

    #Prueba caso baddispatch
    def test6(self): 
        tree = parseCase("baddispatch")
        with self.assertRaises(MethodNotFound):
            self.walker.walk(Listener(), tree)

    #Prueba caso badequalitytest
    def test7(self): 
        tree = parseCase("badequalitytest")
        with self.assertRaises(TypeCheckMismatch):
            self.walker.walk(typecheck.Typecheck(), tree)

    #Prueba caso badequalitytest2
    def test8(self): 
        tree = parseCase("badequalitytest2")
        with self.assertRaises(TypeCheckMismatch):
            self.walker.walk(typecheck.Typecheck(), tree)

    #Prueba caso badmethodcallsitself
    def test9(self): 
        tree = parseCase("badmethodcallsitself")
        with self.assertRaises(CallTypeCheckMismatch):
            self.walker.walk(Listener(), tree)

    #Prueba caso badstaticdispatch
    def test10(self): 
        tree = parseCase("badstaticdispatch")
        with self.assertRaises(MethodNotFound):
            self.walker.walk(Listener(), tree)

    #Prueba caso badwhilebody
    def test11(self): 
        tree = parseCase("badwhilebody")
        with self.assertRaises(MethodNotFound):
            self.walker.walk(Listener(), tree)

    #Prueba caso badwhilecond
    def test12(self): 
        tree = parseCase("badwhilecond")
        with self.assertRaises(TypeCheckMismatch):
            self.walker.walk(typecheck.Typecheck(), tree)

    #Prueba caso caseidenticalbranch
    def test13(self): 
        tree = parseCase("caseidenticalbranch")
        with self.assertRaises(InvalidCase):
            self.walker.walk(Listener(), tree)

    #Prueba caso dupformals
    def test14(self): 
        tree = parseCase("dupformals")
        with self.assertRaises(KeyError):
            self.walker.walk(klassListener.KlassListener(), tree)

    #Prueba caso letbadinit
    def test15(self): 
        tree = parseCase("letbadinit")
        with self.assertRaises(DoesNotConform):
            self.walker.walk(Listener(), tree)

    #Prueba caso lubtest
    def test16(self): 
        tree = parseCase("lubtest")
        with self.assertRaises(DoesNotConform):
            self.walker.walk(Listener(), tree)

    #Prueba caso missingclass
    def test17(self): 
        tree = parseCase("missingclass")
        with self.assertRaises(TypeNotFound):
            self.walker.walk(klassListener.KlassListener(), tree)

    #Prueba caso outofscope
    def test18(self): 
        tree = parseCase("outofscope")
        with self.assertRaises(UndeclaredIdentifier):
            self.walker.walk(Listener(), tree)

    #Prueba caso redefinedclass
    def test19(self): 
        tree = parseCase("redefinedclass")
        with self.assertRaises(ClassRedefinition):
            self.walker.walk(klassListener.KlassListener(), tree)

    #Prueba caso returntypenoexist
    def test20(self): 
        tree = parseCase("returntypenoexist")
        with self.assertRaises(TypeNotFound):
            self.walker.walk(typecheck.Typecheck(), tree)

    #Prueba caso trickyatdispatch2
    def test21(self): 
        tree = parseCase("trickyatdispatch2")
        with self.assertRaises(MethodNotFound):
            self.walker.walk(Listener(), tree)

    #Prueba caso selftypebadreturn
    def test22(self): 
        tree = parseCase("selftypebadreturn")
        with self.assertRaises(TypeCheckMismatch):
            self.walker.walk(methodListener.MethodListener(), tree)

    #Prueba caso overridingmethod4
    def test23(self): 
        tree = parseCase("overridingmethod4")
        with self.assertRaises(InvalidMethodOverride):
            self.walker.walk(methodListener.MethodListener(), tree)

    #Prueba caso signaturechange
    def test24(self): 
        tree = parseCase("signaturechange")
        with self.assertRaises(InvalidMethodOverride):
            self.walker.walk(methodListener.MethodListener(), tree)

if __name__ == '__main__':
    unittest.main()