from antlr4 import *
from antlr.CoolLexer import CoolLexer
from antlr.CoolParser import CoolParser
from antlr.CoolListener import CoolListener
from myexceptions import *

class MethodListener(CoolListener):
    class_array = []
    dic_methods = {}
    dic_formals = {}

    def __init__(self):
        self.class_array = []
        self.dic_methods = {}
        self.dic_formals = {}     

    #Klass
    def enterKlass(self, ctx: CoolParser.KlassContext):

        if ctx.TYPE(0).getText() not in self.class_array:
            self.class_array.append(ctx.TYPE(0).getText())
        else:
            raise ClassRedefinition

        if  ctx.TYPE(1) != None and (ctx.TYPE(1).getText() not in self.class_array):
            raise TypeNotFound
        
        elif ctx.TYPE(1) != None and (ctx.TYPE(1).getText() in self.class_array):
    
            for i in ctx.feature():
                if  i.ID().getText() in self.dic_methods.get(ctx.TYPE(1).getText()):
                 raise InvalidMethodOverride

        method_array = []

        for i in ctx.feature():
            method_array.append(i.ID().getText())
            
        self.dic_methods[ctx.TYPE(0).getText()] = method_array

    #Method
    def enterMethod(self, ctx: CoolParser.MethodContext):
        formal_array = []

        if self.dic_methods.get(ctx.ID().getText) !=None:
            for i in ctx.formal():
                if i.ID().getText() in self.dic_methods.get(ctx.ID().getText):
                    raise InvalidMethodOverride
        if ctx.TYPE().getText() == "SELF_TYPE":
            raise TypeCheckMismatch

        for i in ctx.formal():
            if i.ID().getText() not in formal_array:
                formal_array.append(i.ID().getText())
            elif i.ID().getText() == "self":
                raise DoesNotConform
            else:
                raise KeyError
                
        self.dic_formals[ctx.ID().getText] =  formal_array
        
