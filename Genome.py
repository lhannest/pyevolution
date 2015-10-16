from random import uniform
from Utilities import *

def equals(g1, g2):
  return g1.inov is g2.inov

class Node(object):
  def __init__(self, inov, bias=uniform(0, 1)):
    self.inov = inov
    self.b = bias

class Arc(object):
  def __init__(self, inov, parent, child, weight=uniform(0, 1)):
    self.inov = inov
    self.p = parent
    self.c = child
    self.w = weight
    

class Genome(object):
  def __init__(self):
    self.ndict = {}
    self.adict = {}
    
  def copy():
    ndict={}
    adict={}
    
    for n in self.ndict:
      ndict[n] = self.ndict[n]
      
    for a in self.adict:
      adict[a] = self.adict[a]
    
  def mutate(frequency, amount=0.1):
    for g in self.adict:
      if rbool(frequency):
        self.adict[g] += uniform(-amount, amount)
    for g in self.ndict:
      if rbool(frequency):
        self.ndict[g] += uniform(-amount, amount)