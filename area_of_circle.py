class Circle:
    pi = 3.142 #class object attribute
    def __init__(self,radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * self.pi * self.radius
    def get_area(self):
        return self.pi * (self.radius*self.radius)

circle_1 = Circle(4)
print(circle_1.self)
print (circle_1.get_circumference())

circle_2 = Circle(4)
print(circle_2.get_area())
