import math

class Foo:
    def __init__(self) -> None:
        self.PI = math.pi

    def calculate_sphere_volume(self, radius):
        '''
        Given the radius of a sphere, returns the volume
        Throws exception if radius < 0
        '''
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        return (4/3)*self.PI*(radius**3)
    
'''
Explanation
I decided to take an Object Oriented approach as this software package needs to be flexible and extendable.
Using an OOP approach allows me to utilize the Open/Close principle which will allow for the desire flexbility and continued contribution.
I decided to create a utility class since this package is expected to be used for complex calculations. 
Other developers will therefore be able to define new methods within the class that suits their needs.
I defined a method, "calculate_sphere_volume", to take a radius and return the volume. It contains a simple check to ensure the radius is valid before executing the calculation.

Assumptions & Expectations:
- input for calculate_sphere_volume will always be a number, i.e. "2" will NOT be an input
'''