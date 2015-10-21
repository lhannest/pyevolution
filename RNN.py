from random import uniform

class Node(object):
  def __init__(self):
    self.layer = None
    self.arcs = []
    
class Arc(object):
  def __init__(self, parent):
    self.parent = parent
  def isRecurrent(node):
    return node.layer <= arc.parent.layer

class Layer(object):
  def __init__(self):
    self.nodes = []
    
class RNN(object):
  def __init__(self):
    self.layers = []
    
  def step(self):
    for layer in self.layers:
      for node in layer.nodes:
        for arc in node.arcs:
          if arc.isRecurrent(node):
            arc.take()
          else:
            arc.takePrior()
            
#Mutation Methods
def bumpNode():
  #choose a hidden node and move it into either a higher or lower layer
  None