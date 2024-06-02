import math

class Foo:
    def calculate_sphere_volume(self, radius):
        '''
        Given the radius of a sphere, returns the volume
        Throws exception if radius < 0
        '''
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        return (4/3)*math.pi*(radius**3)