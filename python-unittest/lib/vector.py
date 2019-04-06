class Vector:
    def __init__(self, *contents):
        self.vector = contents
        
    def __iter__(self):
        self.iter_idx = 0
        return self
        
    def __next__(self):
        if self.iter_idx < len(self.vector):
            result = self.vector[self.iter_idx]
            self.iter_idx += 1
            return result
        else:
            raise StopIteration
        
    def __add__(self, another):
        if len(self.vector) != len(another.vector):
            Exception("Dimension Mismatch Error!")
        return Vector(*[x + y for x, y in zip(self.vector, another.vector)])
        
    def __eq__(self, another):
        return self.vector == another.vector
        
    def __mul__(self, another):
        if isinstance(another, Vector):
            return sum([x * y for x, y in zip(self.vector, another.vector)])
        else:
            return Vector(*[x * another for x in self.vector])
    