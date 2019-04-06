class Vector:
    def __init__(self, *contents):
        self.vector = contents
        
    def __add__(self, another):
        if len(self.vector) != len(another.vector):
            Exception("Dimension Mismatch Error!")
        return Vector(*[x + y for x, y in zip(self.vector, another.vector)])
        