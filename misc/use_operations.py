from core.utils.generate import generate_point
from core.utils.operations import *

print(":: Generating Points")

point_a = generate_point(3)
point_b = generate_point(3)
point_c = generate_point(3)

print(f"\tPoint A: {point_a}")
print(f"\tPoint B: {point_b}")
print(f"\tPoint C: {point_c}")

print(":: Computing magnitude") 

print(f"\tPoint A: {magnitude(point_a)}")
print(f"\tPoint B: {magnitude(point_b)}")
print(f"\tPoint C: {magnitude(point_c)}")

print(":: Normalizing vectors") 

print(f"\tPoint A: {normalize(point_a)}")
print(f"\tPoint B: {normalize(point_b)}")
print(f"\tPoint C: {normalize(point_c)}")

print(":: Computing dot products.") 

print(f"\tPoint A and B: {dot_product(point_a, point_b)}")
print(f"\tPoint B and C: {dot_product(point_b, point_c)}")
print(f"\tPoint A and C: {dot_product(point_a, point_c)}")

print(":: Projecting Points.") 

print(f"\tPoint C to A and B: {project_to_line(point_a, point_b, point_c)}")
print(f"\tPoint A to B and C: {project_to_line(point_b, point_c, point_a)}")
print(f"\tPoint B to A and C: {project_to_line(point_a, point_c, point_b)}")
print(f"\tCheck Default (7, 8, 9): {project_to_line([1, 2, 3], [4, 5, 6], [7, 8, 9])}")
