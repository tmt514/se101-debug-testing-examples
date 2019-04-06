import math

def compute_two_norm(vector):
    square_sum = sum(map(lambda x: x*x, vector))
    norm_value = math.sqrt(square_sum)
    return norm_value