import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def volume(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
        
    def length_of_diagonals(self):      
        return math.sqrt(self.length**2 + self.width**2)
    
    def __str__(self):
        return f"Rectangle [length={self.length}, width={self.width}, perimeter={self.perimeter()}]"
    
# create a Rectangle object
rect = Rectangle(3, 4)

# calculate volume, perimeter, and length of diagonals
volume = rect.volume()
perimeter = rect.perimeter()
diagonal_length = rect.length_of_diagonals()

# print the results
print(f"Volume: {volume}")
print(f"Perimeter: {perimeter}")
print(f"Length of diagonals: {diagonal_length}")
print(rect)