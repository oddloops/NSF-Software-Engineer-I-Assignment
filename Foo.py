class Foo:
    def __init__(self, radius) -> None:
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = radius
