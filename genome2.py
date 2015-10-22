from random import uniform
from Utilities import *

class Node(object):
  def __init__(self):
    self.id = 0

class NProperties(object):
  def __init__(self):
    self.bias = 0
    self.layer = 0
  def copy():
    p = NProperty()
    p.bias = self.bias
    p.layer = self.layer
    return p
    
class Arc(object):
  def __init__(self, parent, child):
    self.id = 0
    self.parent = parent
    self.child = child
    
class AProperty(object):
  def __init__(self):
    self.weight = 0
    
  def copy():
    p = AProperty()
    p.weight = self.weight
    return p
    
class Genome(object):
  def __init__(self):
    self.nodes = {}
    self.arcs = {}
  def addNode(self, node=None, other=None):
    
  def copy(self):
    child = Genome()
    for k in self.nodes:
      child.nodes[k] = self.nodes[k].copy()
    for k in self.arcs:
      child.arcs[k] = self.arcs[k].copy()
    return child
  def cross(self, other):
    child = Genome()
    for k in self.nodes:
      if k in other.nodes):
        p = grab(self.nodes[k], other.nodes[k]).copy()
        child.nodes[k] = p
        
# Reproduction Methods for Dictionaries
def copy(dictionary):
  child = {}
  for k in dictionary:
    child[k] = dictionary[k].copy()
    
def cross(dom, sub):
  child = {}
  for k in dom:
    if k in sub:
      child[k] = grab(dom[k], sub[k]).copy()
    else:
      child[k] = dom[k].copy()
  return child

def merge(a, b):
  for a 
    
    
g = Genome()





#End