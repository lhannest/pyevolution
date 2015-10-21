from random import uniform

class C(object):
  def __init__(self, name):
    self.name = name
    self.value = 0
  def __repr__(self):
    return str(self.name)

class W(object):
  def __init__(self, f):
    self.f = f
    self.name = f.name + "'"
    @property
    def value(self): return self.f.value
  def __repr__(self):
    return str(self.f.name) + "'"

class F(object):
  def __init__(self, name):
    self.summands = []
    self.name = name
    self.bias = uniform(0, 2)
    self.value = 0
  def add(self, sums):
    if type(sums) is list:
      for s in sums:
        self.summands.append(s)
    else:
      self.summands.append(sums)
  def __repr__(self):
    return str(self.name)
    
def prt(f):
  st ="  "+str(f.name)+"="+toString(f)
  print(st)
  
def toString(f):
  if type(f) is not F:
    return repr(f)
  st = "f("
  for i, s in enumerate(f.summands):
  	  if i != 0: st +="+"
  	  st+=toString(s)
  return st +")"

def expand(f, callers = []):
  c = list(callers)
  c.append(f)
  for i, s in enumerate(f.summands):
    flg=type(s) is W and s.f not in c
    if s in c:
      f.summands[i] = W(s)
    elif flg:
      expand(s.f, c)
    else:
      if type(s) is F:
        expand(s, c)

def evaluate(f):
  if type(f) is C:
    return f.value
  elif type(f) is W:
    return f.f.value
  else:
    _sum = 0
    for s in f.summands:
      _sum += evaluate(s)
    if _sum >= f.bias:
      f.value = _sum - f.bias
      return f.value - f.bias
    else:
      return 0

x = C('x')
a = F('a')
b = F('b')
c=F('c')
y = F('y')

a.add([x, b])
b.add([a, c])
c.add(b)
y.add([a, b])
expand(y)
#prt(y)
#prt(a)
#prt(b)
#prt(c)

#x.value = 1.23
#print(evaluate(y))