import math

def circle_stats(radius):
    # PI = 3.1415
   area = math.pi * radius **2
   circ = 2 * math.pi * radius
   return area, circ

area, circ = circle_stats(4.3)
print("Area: ", area, "Circumference: ", circ)