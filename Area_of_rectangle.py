class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def get_area(self):
        return self.length * self.breadth

rectangle_1 = Rectangle(5,4)
print(f'The area of the rectangle is {rectangle_1.get_area()}')