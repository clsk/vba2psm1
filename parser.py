import ply.yacc as yacc
from node import *

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
        pass

    def p_statement(self, p):
        '''statement : declaration
                     | assignment'''
        p[0] = p[1]
        if (p[1] is not None):
            self.get_current_block().children.append(p[1])

    def p_declaration(self, p):
        "declaration : DIM IDENTIFIER AS TYPE"
        self.identifiers[p[2]] = Identifier(p[4], p[2])


    def p_assignment(self, p):
        '''assignment : IDENTIFIER ASSIGN const_literal'''
        id = self.identifiers.get(p[1], None)
        if (not id):
            raise TypeError("%d: Undeclared IDENTIFIER '%s'." % (p.lineno(1), p[1]))

        if ((id.t == "Boolean" and p[3].type != "BOOLEAN") or
            (id.t == "Integer" and p[3].type != "INT") or
            (id.t == "Double" and p[3].type == "BOOLEAN") or
            (id.t == "Byte" and p[3].type != "INT")):
            print("%d: Type mismatch. Trying to assign (%s) to identifier '%s' which is of type %s" % (p.lineno(3), p[3], p[1], p[3].type))

        id.value = p[3].literal
        p[0] = NodeAssignment(id, p[3])


    def p_const_literal(self, p):
        '''const_literal : BOOLEAN
                         | DOUBLE
                         | INT'''
        p[0] = NodeConstLiteral(p[1], p.slice[1].type)

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
        self.block_stack = [NodeBlock([])]

    def push_block(self):
        self.block_stack.apend(NodeBlock())
        return self.get_current_bloc()

    def pop_block(self):
        return self.block_stack.pop()

    def get_current_block(self):
        return self.block_stack[-1]

    def build(self, text):
        self.text = text
        self.scanner.text = text
        self.parser = yacc.yacc(module=self, outputdir=self.outputdir)
        self.parser.parse(input=text, lexer=self.scanner.lexer);
        return self.block_stack[0]


