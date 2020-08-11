import math
from Polygon import Polygon 


class Polygons: 
  def __init__(self, m, R): 
    if m < 3: 
      raise ValueError('m must be greater than 3')
    self._m = m
    self._R = R
    self._polygons = [Polygon(i, R) for i in range(3, m+1)]

  
  def __len__(self): 
    return self._m-2 

  def __repr__(self): 
    return f'Polygons(m={self._m}, R={self._R})'


  def __getitem__(self, s): 
    return self._polygons[s]

  @property
  def max_efficiency_polygon(self): 
    sorted_polygons = sorted(self._polygons, key=lambda p: p.area/p.perimeter, reverse=True) 
    return sorted_polygons[0]


polygon = Polygons(6, 1) 
len(polygon)

print(polygon) 


polygons = Polygons(8,1)
for p in polygons: 
  print(p)

for p in polygons[2:5]: 
  print(p)

for p in polygons[:-1]:
  print(p)

polygons = Polygons(10, 1)

print(polygons.max_efficiency_polygon) 

# print[(p, p.area/p.perimeter) for p in polygons]  

polygons = Polygons(1000, 1)
p = polygons.max_efficiency_polygon
print(p) 
print(p.area)   #Very close to pi, as the n increases to infinite, the polygon seems more and more alike a circle. 

assert math.isclose(p.area, math.pi, rel_tol=0.001, abs_tol=0.001)



