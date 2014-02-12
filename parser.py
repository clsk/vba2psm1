import ply.yacc as yacc

class Identifier:
    def __init__(self, t, name, value):
        self.t = t # type
        self.name = name
        self.value = value

    def __repr__(self):
        return self.t + " " + self.name + " = " + repr(self.value)

class Parser:
    identifiers = {}

    def p_assignment_expression(self, p):
        '''assignment : IDENTIFIER ASSIGN BOOLEAN
                      | IDENTIFIER ASSIGN DOUBLE
                      | IDENTIFIER ASSIGN INT
                      | IDENTIFIER ASSIGN BYTE'''
        id = self.identifiers.get(p[1], None)
        if (not id):
            raise TypeError("%d: Identifier '%s' not found." % (p.lineno, p[1]))


        if (p[3].type != id.t):
            raise TypeError("%d: Type mismatch. Trying to assign (%s) to identifier '%s' which is of type %s" % (p.lineno, p[3], p[1], p[3].type))

        id.value = p[3]


    def p_declaration_expression(self, p):
        "declaration : DIM IDENTIFIER AS TYPE"
        self.identifiers[p[2]] = Identifier(p[4], p[2], None)


    #def p_vector_expression(self, p):
        #"vector : floats"
        #p[0] = p[1]

    #def p_floats_expression(self, p):
        #'''floats : FLOAT
                  #| floats FLOAT'''
        #if (not isinstance(p[1], list)):
            #p[0] = [p[1]]
        #else:
            #p[1].append(p[2])
            #p[0] = p[1]

    def p_error(self, p):
        print "line %d: Syntax error near '%s'" % (p.lineno, p.value)


    def __init__(self, scanner, outputdir=None):
        self.outputdir = outputdir
        self.scanner = scanner;
        scanner.build(outputdir=outputdir)
        self.tokens = scanner.tokens

    def build(self, text):
        self.parser = yacc.yacc(module=self, outputdir=self.outputdir)
        return self.parser.parse(input=text, lexer=self.scanner.lexer);
