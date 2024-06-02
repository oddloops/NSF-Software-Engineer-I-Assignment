import unittest
from foo import Foo

class TestFoo(unittest.TestCase):
    def test_positive_radius(self):
        radius = 2.5
        expected_volume = 65.44985
        calculated_volume = Foo().calculate_sphere_volume(radius)
        self.assertAlmostEqual(calculated_volume, expected_volume, places=4)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            radius = -1
            negative_foo = Foo()
            negative_foo.calculate_sphere_volume(radius)

    def test_zero_radius(self):
        radius = 0
        expected_volume = 0
        calculated_volume = Foo().calculate_sphere_volume(radius)
        self.assertEqual(calculated_volume, expected_volume)

if __name__ == '__main__':
    unittest.main()

'''
I created tests around the different radius inputs. 
Assuming users will only input valid numbers, there are 3 possible inputs, postive, negative, and 0.
Positive inputs will always be valid (Real Numbers)
A 0 radius should simply result in 0 volume
But a negative input should be invalid -> a radius cannot be negative.
'''