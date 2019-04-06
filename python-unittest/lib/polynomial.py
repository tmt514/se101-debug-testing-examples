from .vector import Vector

class Polynomial(Vector):
    def __init__(self, *contents):
        super().__init__(*contents)
        
    def __call__(self, x):
        result = 0
        n = len(self.vector)
        for i in range(n-1, 0, -1):
            result = result * x + self.vector[i]
        return result
        
    def __mul__(self, another):
        # TODO: change this to polynomial multiplication!
        if isinstance(another, Vector):
            return sum([x * y for x, y in zip(self.vector, another.vector)])
        else:
            return Vector(*[x * another for x in self.vector])
    