from scanner import Scanner
from parser import Parser
from generator import *
import ply.argparse as argparse

outputdir = "bin/"

arguments = argparse.ArgumentParser(description="VBA (Excel) to PowerShell Module Translator")
arguments.add_argument("-VBAInput", "-V", required=True ,metavar="VBA", dest="infile", help="Archivo Visual Basic for Application (.bas) con el contenido del modulo.")
arguments.add_argument("-PWSOutput", "-P" ,metavar="psm1", dest="outfile" ,help="Archivo PowerShell (.psm1) con el contenido del modulo producido. Si esta ausente, la salida sera hacia la consola.")

args = arguments.parse_args()
if args.infile is not None:
	print "input file: " + args.infile
if args.outfile is not None:
	print "output file: " + args.outfile

source = ""
with open(args.infile) as f:
	source = f.read()

parser = Parser(Scanner(), outputdir)
node = parser.build(source)
print node
print "Identifiers(" + repr(len(parser.identifiers)) + ")"
for k,v in parser.identifiers.iteritems():
    print repr(v)

# Generate code and append to out string
out = get_generator(node).generate()

if (args.outfile is not None):
	with open(args.outfile, "w") as of:
		of.write(out)
else:
	print out
