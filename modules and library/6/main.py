#Create a package shapes with modules for circle and rectangle

from shapes.circle import area as circle_area
from shapes.rectangle import area as rectangle_area

print(circle_area(2))
print(rectangle_area(4,5))