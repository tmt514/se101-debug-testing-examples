class Vector:
    def __init__(self, *contents):
        self.vector = contents
        
    def __add__(self, another):
        return Vector(*[x + y for x, y in zip(self.vector, another.vector)])
        
    def __mul__(self, another):
        if isinstance(another, Vector):
            return sum([x * y for x, y in zip(self.vector, another.vector)])
        else:
            return Vector(*[x * another for x in self.vector])
        
    def __eq__(self, another):
        return self.vector == another.vector