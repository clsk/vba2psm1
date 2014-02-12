from scanner import Scanner
from parser import Parser

outputdir = "bin/"
parser = Parser(Scanner(), outputdir)
parser.build("DIM a AS Integer\na = 3")

for k,v in Parser.identifiers.iteritems():
    print k + ": " + repr(v)
print len(Parser.identifiers)

