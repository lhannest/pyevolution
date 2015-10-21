from random import uniform
from Utilities import *

def equals(g1, g2):
  return g1.inov is g2.inov

class Node(object):
  def __init__(self, inov):
    self.inov = inov

class Arc(object):
  def __init__(self, inov, parent, child):
    self.inov = inov
    self.p = parent
    self.c = child
    
def dictCross(a, b):
  child={}
  for k in a:
    if k in b:
      child[k] = grab(a[k], b[k])
  return child
    
class Genome(object):
  def __init__(self):
    self.nodes = {}
    self.arcs = {}
      
  def add(self, component, other=None):
    value = None
    
    if other is None:
      value = uniform(0, 1)
      
    if type(component) is Node:
      if value is None:
        value = other.nodes[component]
        
      self.nodes[component] = value
      
    elif type(component) is Arc:
      if value is None:
        value = other.arcs[component]
        
      self.arcs[component] = value
      
    else:
      assert False
      
    return component
      
    
  def copy(self):
    g = Genome()
    g.nodes = dict(self.nodes)
    g.arcs = dict(self.arcs)
    return g
  
  def cross(self, other):
    g = Genome()
    g.nodes = dictCross(self.nodes, other.nodes)
    g.arcs = dictCross(self.arcs, other.arcs)
    return g
    
  def mutate(self, frequency=0.1, amount=0.1):
    for g in self.arcs:
      if rbool(frequency):
        self.arcs[g] += uniform(-amount, amount)
    for g in self.nodes:
      if rbool(frequency):
        self.nodes[g] += uniform(-amount, amount)
        
        
g = Genome()
i = g.add(Node(0))
h = g.add(Node(1))
o = g.add(Node(2))
a = g.add(Arc(3,i,h))
b = g.add(Arc(4,h,o))

q = g.copy()
g.mutate()
g.mutate()
r = g.cross(q)