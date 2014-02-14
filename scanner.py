import ply.lex as lex

class Scanner:
    tokens = (
            "DOUBLE",
            "IDENTIFIER",
            "INT",
            "TYPE",
            "BOOLEAN",
            "BYTE",            
            "STRING",
            "DIM",
            "AS",
            "ASSIGN",
            "SUB",
            "END SUB",
            "LPAR",
            "RPAR"
    )

    t_INT = "\d+"
    t_DOUBLE = r"-?\d+(\.\d+)?([e|E][+-]?\d+)?"
    t_IDENTIFIER = r"\w+"
    t_TYPE = "Double|Integer|Boolean|Byte|String"
    t_BOOLEAN = "True|False"
    t_DIM = "DIM"
    t_AS = "AS"
    t_ASSIGN = "="
    t_SUB = "SUB"
    t_ENDSUB = "END SUB"
    t_LPAR = "\("
    t_RPAR = "\)"
    t_ignore = ' \t'
    def t_BYTE(self, t):
        '''\d{1,3}'''
        i = int(t[0])
        if (i > 255 or i < 0):
            raise TypeError("%d: Value out of range for Byte %d. Byte range is 0-255." % (t.lineno, t.value,))
        return t

# Ignore comments
    def t_comment(self, t):
        r"['|REM][^\n]*"
        pass

    def t_newline(self, t):
        r"\n+"
        t.lineno += t.value.count("\n")

    def t_error(self, t):
        raise TypeError("%d: Unknown text '%s'" % (t.lineno,t.value,))

    def build(self, outputdir = None, **kwargs):
        self.lexer = lex.lex(module=self, outputdir=outputdir, **kwargs)
