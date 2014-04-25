import ply.lex as lex

class Scanner:
    reserved = {
    "Dim": "DIM",
    "As": "AS",
    "Sub": "SUB",
    "End": "END",
    "If": "IF",
    "Then": "THEN",
    "Else": "ELSE",
    "For": "FOR",
    "Each": "Each",
    "Double": "TYPE",
    "Integer": "TYPE",
    "Boolean": "TYPE",
    "Byte": "TYPE",
    "String": "TYPE",
    "Date": "TYPE",
    "Currency": "TYPE",
    "True": "BOOLEAN_LITERAL",
    "False": "BOOLEAN_LITERAL"
    }

    tokens = [
            "DOUBLE",
            "IDENTIFIER",
            "INT",
            "TYPE",
            "BOOLEAN",
            "ASSIGN",
            "LPAR",
            "RPAR",
            "PLUS",
            "MINUS",
            "DIVIDE",
            "MULTI" #Multiplicacion
    ] + list(reserved.values())


    t_INT = "\d+"
    t_DOUBLE = r"-?\d+\.\d+([e|E][+-]?\d+)?"
    t_ASSIGN = "="
    t_LPAR = "\("
    t_RPAR = "\)"
    t_PLUS = r"\+"
    t_MINUS = r"\-"
    t_DIVIDE = r"\/"
    t_MULTI = r"\*"
    t_ignore = ' \t'

    def t_IDENTIFIER(self, t):
        r"[a-zA-Z]+"
        t.type = Scanner.reserved.get(t.value, "IDENTIFIER")
        return t

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
