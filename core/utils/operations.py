import math 

def magnitude(A): 
    component_total = 0 
    for i in range(len(A)):
        component_total += A[i] * A[i]
    return math.sqrt(component_total)

def normalize(A):
    magnitude_ = magnitude(A) 
    normalized = []
    for i in range(len(A)): 
        normalized.append(A[i] / magnitude_)
    return normalized

def dot_product(A, B): 
    dot_total = 0
    for i in range(len(A)): 
        dot_total += A[i] * B[i]
    return dot_total 

def project_to_line(A, B, C): 
    AB = [B[i] - A[i] for i in range(len(A))]
    AC = [C[i] - A[i] for i in range(len(C))] 
    dot_product_ = dot_product(AB, AC)
    magnitude_ab_squared = sum(AB[i] * AB[i] for i in range(len(AB))) 
    projection_factor = dot_product_ / magnitude_ab_squared 
    D = [A[i] + projection_factor * AB[i] for i in range(len(A))]
    return D




