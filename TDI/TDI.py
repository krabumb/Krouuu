class TDI:

    def __init__(self):
        self.declarations = {}
    
    def add_declaration(self, var_name, var_type):
        self.declarations[var_name] = var_type

    def already_declared(self, var_name):
        return var_name in self.declarations

    def get_type(self, var_name):
        if self.already_declared(var_name):
            return self.declarations[var_name]
        else:
            return None

class Scope:

    def __init__(self, parent : 'Scope' = None):
        self.__parent_scope : Scope = parent
        self.__scopeNum = parent.get_scope_num() + 1 if parent is not None else 1
        self.__tdi = TDI()

    def get_scope_num(self):
        return self.__scopeNum
    
    def add_declaration(self, var_name, var_type):
        self.__tdi.add_declaration(var_name, var_type)

    def get_type(self, var_name):
        retour = self.__tdi.get_type(var_name)
        if retour is not None:
            return retour
        elif self.__parent_scope is not None:
            return self.__parent_scope.get_type(var_name)
        else:
            return None

    def get_scope_of_var(self, var_name):
        if self.__tdi.already_declared(var_name):
            return self
        elif self.__parent_scope is not None:
            return self.__parent_scope.get_scope_of_var(var_name)
        else:
            return None

    def get_num_scope_of_var(self, var_name):
        if self.__tdi.already_declared(var_name):
            return self.__scopeNum
        elif self.__parent_scope is not None:
            return self.__parent_scope.get_num_scope_of_var(var_name)
        else:
            return None

    def get_parent_scope(self):
        return self.__parent_scope