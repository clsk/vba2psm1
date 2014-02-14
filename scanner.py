import ply.lex as lex

class Scanner:
    tokens = (
            "DOUBLE",
            "IDENTIFIER",
            "INT",
            "TYPE",
            "BOOLEAN",
            "DIM",
            "AS",
            "ASSIGN",
            "SUB",
            "END SUB",
            "LPAR",
            "RPAR"
    )

    t_INT = "\d+"
    t_DOUBLE = r"-?\d+\.\d+([e|E][+-]?\d+)?"
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

# Ignore comments
    def t_comment(self, t):
        r"['|REM][^\n]*"
        pass

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)
        pass

    def t_error(self, t):
        raise TypeError("%d:%d: Unknown text '%s'" % (t.lineno, find_column(self.text, t), t.value,))

    def build(self, outputdir = None, **kwargs):
        self.lexer = lex.lex(module=self, outputdir=outputdir, **kwargs)
    # Compute column
    #input is the input text string
    #token is a token instance
    def find_column(self,input,token):
        last_cr = input.rfind('\n',0,token.lexpos)
        if last_cr < 0:
            last_cr = 0
        column = (token.lexpos - last_cr) + 1
        return column
