from core.utils.measures import * 

from core.utils.generate import generate_point
from core.utils.operations import *

print(":: Generating Points")

point_a = generate_point(3)
point_b = generate_point(3)

print(f"\tPoint A: {point_a}")
print(f"\tPoint B: {point_b}")

print(":: Computing euclidean distance.") 

print(f"\tPoint A and B: {euclidean_distance(point_a, point_b)}")

print(":: Computing cosine similarity.") 

print(f"\tPoint A and B: {cosine_similarity(point_a, point_b)}")

print(":: Computing cosine distance.") 

print(f"\tPoint A and B: {cosine_distance(point_a, point_b)}")

print(":: Computing inverted cosine distance.") 

print(f"\tPoint A and B: {inverse_cosine_distance(point_a, point_b)}")

print(":: Computing cosine similarity score.") 

print(f"\tPoint A and B: {cosine_similarity_score(point_a, point_b)}")
