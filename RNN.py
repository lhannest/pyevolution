from random import uniform

class Node(object):
  def __init__(self):
    self.layer = None
    self.arcs = []
    
class Arc(object):
  def __init__(self, parent, child):
    self.parent = parent
    self.child = child
  def isRecurrent(node):
    return node.layer <= arc.parent.layer

class Layer(object):
  def __init__(self, size):
    self.nodes = []
    for i in range(size):
      self.nodes.append(Node())
      
    self.size = size
  def feedInto(other):
    for n in self.nodes:
      
    
class RNN(object):
  def __init__(self, layers=[]):
    self.layers = layers
    
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
  
  
  
a = Layer(2)
b = Layer(3)
c = Layer(3)
d = Layer(1)
rnn = RNN([a,b,c,d])

x = rnn.step()
print x