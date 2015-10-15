from random import uniform

def rbool(frequency):
  return uniform(0.0, 1.0) >= frequency*1.0

def grab(a, b):
  if rbool(0.5):
    return a
  else:
    return b

def aggregate(a, b):
  l=[];
  for x in a: l.append(a);
  for x in b: l.append(b);