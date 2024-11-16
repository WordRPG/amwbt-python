import random 
import settings

default_generator = random.Random(settings.SEED)

def generate_point(dims, generator = "auto"): 
    if generator == "auto": 
        generator = default_generator
    point = []
    for i in range(dims): 
        point.append(round(generator.uniform(-10, 10), 4)) 
    return point

def generate_points(count, generator = "auto"):
    if generator == "auto": 
        generator = lambda: generate_point(2) 
    points = []
    for i in range(count): 
        points.append(generator()) 
    return points