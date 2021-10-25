#Etapa1
class NoMainException(Exception):
    pass

class RedefineBasicClassException(Exception):
    pass

class InheritsSelfException(Exception):
    pass

class SelfVariableException(Exception):
    pass

class InvalidInheritsException(Exception):
    pass

class SelfAssignmentException(Exception):
    pass

class SelftypeInvalidUseException(Exception):
    pass


#Etapa2

class CallTypeCheckMismatch(Exception):
    pass

class ClassRedefinition(Exception):
    pass

class DoesNotConform(Exception):
    pass

class InvalidCase(Exception):
    pass

class InvalidMethodOverride(Exception):
    pass

class MethodNotFound(Exception):
    pass

class NotSupported(Exception):
    pass

class TypeCheckMismatch(Exception):
    pass

class TypeNotFound(Exception):
    pass

class UndeclaredIdentifier(Exception):
    pass
