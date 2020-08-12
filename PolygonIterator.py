import math 
from Polygon import Polygon
from Polygons import Polygons

class PolygonIterator: 
  def __init__(self, n, R): 
    if n < 3: 
      raise ValueError(' ')
    self._n = n 
    self._R = R
    self._i = 3 
  
  def __iter__(self): 
    return self 

  def __next__(self): 
    if self._i > self._n : 
      raise StopIteration
    else: 
      result = Polygon(self._i, self._R)
      self._i += 1
      return result 

p_iter = PolygonIterator(5, 3)
next(p_iter)

polygons = Polygons(5, 3)
for p in polygons: 
  print(p)

