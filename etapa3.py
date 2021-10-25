import sys
import unittest

from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser
#from structure import Jerarquia, JerarquiaPre, types
from tree import TreePrinter
from myexceptions import *

from etapa1Listener import Listener
from klassListener import KlassListener
from typecheck import Typecheck
from methodListener import  MethodListener

def parseAndCompare(caseName):
    parser = CoolParser(CommonTokenStream(CoolLexer(FileStream("resources/semantic/input/%s.cool" % caseName))))
    tree = parser.program()
    walker = ParseTreeWalker()

    walker.walk(KlassListener(), tree)
    walker.walk(Typecheck(), tree)
    walker.walk(Listener(), tree)

#Prueba basica
class BaseTest(unittest.TestCase):
    def setUp(self): 
        self.walker = ParseTreeWalker()

#Ciclo para probar los casos y realizar las pruebas
cases = ['simplearith',
        'basicclassestree',
        'expressionblock',
        'objectdispatchabort',
        'initwithself',
        'compare',
        'comparisons',
        'cycleinmethods',
        'letnoinit',
        'forwardinherits',
        'letinit',
        'newselftype',
        'basic',
        'overridingmethod',
        'letshadows',
        'neg',
        'methodcallsitself',
        'overriderenamearg',
        'isvoid',
        'overridingmethod3',
        'inheritsObject',
        'scopes',
        'letselftype',
        'if',
        'methodnameclash',
        'trickyatdispatch',
        'stringtest',
        'overridingmethod2',
        'simplecase',
        'assignment',
        'subtypemethodreturn',
        'dispatch',
        'io',
        'staticdispatch',
        'classes',
        'hairyscary',
        'cells',
        'list',
        ]

if __name__ == '__main__':
    methods = {}
    i = 0
    for caso in cases:
        methods['test%d' % i] = lambda self: self.assertTrue(parseAndCompare(caso))
        i = i+1
    CoolTests = type('CoolTests', (BaseTest,), methods)
    unittest.main()