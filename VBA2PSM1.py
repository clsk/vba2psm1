from scanner import Scanner
from parser import Parser

outputdir = "bin/"
parser = Parser(Scanner(), outputdir)
parser.build("DIM a AS Integer\na = 3")
#parser.build("a = 5")

print "Identifiers(" + repr(len(parser.identifiers)) + ")"
for k,v in parser.identifiers.iteritems():
    print repr(v)

