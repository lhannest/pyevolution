from Genome import *
from Function import *

def build(genome):
  nmap={}
  rnn = []
  for n in genome.ndict:
    f = F(-1*n.inov)
    f.add(C(genome.ndict[n]))
    rnn.append(f)
    nmap[n]=f
    nmap[f]=n
    prt(f)
    
  for a in genome.adict:
    p = nmap[a.p]
    c = nmap[a.c]
    c.add(p)
  
  return rnn
    
g=Genome()
a=Node(1)
b=Node(2)
c=Node(3)
d=Arc(4,a,b)
e=Arc(5,b,c)
g.addNodes([a,b,c])
g.addArcs([d,e])

functions=build(g)

for f in functions:
  expand(f)

for f in functions:
  print "    "+toString(f)