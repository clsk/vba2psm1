import ply.yacc as yacc

class Identifier:
    def __init__(self, t, name):
        self.t = t # type
        self.name = name
        if (t == "BOOLEAN"):
            self.value = "False"
        else:
            self.value = "0"

    def __repr__(self):
        return self.t + " " + self.name + " = " + repr(self.value)

class Parser:
    def p_statements(self, p):
        '''statements : statement
                      | statements statement'''

    def p_statement(self, p):
        '''statement : declaration
                     | assignment'''
        p[0] = p[1]

    def p_declaration(self, p):
        "declaration : DIM IDENTIFIER AS TYPE"
        self.identifiers[p[2]] = Identifier(p[4], p[2])


    def p_assignment(self, p):
        '''assignment : IDENTIFIER ASSIGN BOOLEAN
                      | IDENTIFIER ASSIGN DOUBLE
                      | IDENTIFIER ASSIGN INT'''
        id = self.identifiers.get(p[1], None)
        if (not id):
            raise TypeError("%d: Undeclared IDENTIFIER '%s'." % (p.lineno(1), p[1]))

        if ((id.t == "Boolean" and p.slice[3].type != "BOOLEAN") or
            (id.t == "Integer" and p.slice[3].type != "INT") or
            (id.t == "Double" and p.slice[3].type == "BOOLEAN") or
            (id.t == "Byte" and p.slice[3].type != "INT")):
            print("%d: Type mismatch. Trying to assign (%s) to identifier '%s' which is of type %s" % (p.lineno(3), p[3], p[1], p[3].type))

        id.value = p[3]


    def p_error(self, p):
        if p:
            raise TypeError("line %d:%d Syntax error near '%s': Unexpected %s found." % (p.lineno, self.scanner.find_column(self.text, p), p.value, p.type))
        else:
            print "Syntax error: Reached end ouf output."

    def __init__(self, scanner, outputdir=None):
        self.outputdir = outputdir
        self.scanner = scanner;
        scanner.build(outputdir=outputdir)
        self.tokens = scanner.tokens
        self.identifiers = {}

    def build(self, text):
        self.text = text
        self.scanner.text = text
        self.parser = yacc.yacc(module=self, outputdir=self.outputdir)
        return self.parser.parse(input=text, lexer=self.scanner.lexer);
