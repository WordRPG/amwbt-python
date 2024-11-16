import math 
from .operations import *

def euclidean_distance(A, B): 
    total = 0 
    for i in range(len(A)):
        diff = A[i] - B[i] 
        diff_squared = diff ** 2 
        total += diff_squared
    distance = math.sqrt(total)
    return distance

def inverse_euclidean_distance(A, B):
    return -1 * euclidean_distance(A, B)

def cosine_similarity(A, B): 
    dot_product_ = dot_product(A, B)
    magnitude_a = magnitude(A)
    magnitude_b = magnitude(B)
    cosine_similarity_ = dot_product_ / (magnitude_a * magnitude_b)
    return cosine_similarity_

def cosine_distance(A, B): 
    return 1 - cosine_similarity(A, B) 

def inverse_cosine_distance(A, B): 
    return -1 * cosine_distance(A, B)

def cosine_similarity_score(A, B): 
    return (cosine_similarity(A, B) + 1) / 2

def inverted_cosine_similarity_score(A, B): 
    return -1 * cosine_similarity_score(A, B)