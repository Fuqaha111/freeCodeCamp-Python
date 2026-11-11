class Circle:
    def __init__(self, radius):
        self.radius = radius


    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Value must be a positive integer")
        self._radius = value

circle1 = Circle(3.13333)

print(circle1.radius)