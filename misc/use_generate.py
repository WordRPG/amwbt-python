from core.utils.generate import generate_point, generate_points

print(":: Generating point.")
point = generate_point(3)
print(point)

print(":: Generating points.")
points = generate_points(10, lambda: generate_point(3))
for point in points:
    print("\t", point)