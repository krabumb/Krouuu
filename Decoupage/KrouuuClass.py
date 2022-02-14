class KrouuuClass:

    def __init__(self):
        self.implements = [] # Liste des classes implémentées
        self.extends = [] # Liste des classes héritées
        self.variable_declarations = {} # {'var_name': 'var_type'}
        self.method_declarations = {} # {'method_name': 'method_return_type'}
    
    def add_implement(self, class_name):
        if class_name in self.implements:
            raise Exception('Class already declared in implementation list')
        self.implements.append(class_name)

    def add_extend(self, class_name):
        if class_name in self.extends:
            raise Exception('Class already declared in extends list')
        self.extends.append(class_name)

    def add_variable_declaration(self, var_name, var_type):
        if var_name in self.variable_declarations:
            raise Exception('Variable already declared, redefinition not allowed')
        self.variable_declarations[var_name] = var_type

    def add_method_declaration(self, method_name, method_return_type):
        if method_name in self.method_declarations:
            raise Exception('Method already declared, redefinition not allowed')
        self.method_declarations[method_name] = method_return_type