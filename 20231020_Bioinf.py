#!usr/bin/python

import sys
import getopt

def usage():
    print("""Program to do some bioinformatics
    -h  Print help
    -n  Specify THE parameter""")



################
seq= 'AGCCTACTA'

def compl(s):
    dict= {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    newS= ''
    for l in s:
        #print('letter %s' % l)
        newL= dict[l]
        newS += newL
    return(newS)
        
out= compl(seq)
print('complement: %s' % out)   
################

#print("ARGV: %s" % sys.argv)
optArg, reqArg= getopt.getopt(sys.argv[1:], 'n:h')
print("Optarg %s:" % optArg)

opt= {}
for a,b in optArg:
    opt[a]= b

print("opt: %s" % opt)

if '-h' in opt.keys():
    usage()
    sys.exit()

if '-n' in opt.keys():
    param= opt['-n']


if (len(sys.argv) > 1):
    file= sys.argv[1]
else:
    file= 'HelloDNA.fa'

try:
    f= open(file,'r')
except IOError:
    'Could not open file!'
    
r= f.read()
print(r)

    
f.close()


################
