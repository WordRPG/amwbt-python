import settings 

from core.utils.generate import generate_points, generate_point
from core.nns.brute_force import BruteForceNNS 
from core.utils.measures import *

# --- generate points --- # 
print("Generating points.")
points = generate_points(
    settings.NNS_POINT_COUNT, 
    lambda: generate_point(settings.NNS_POINT_DIMENSIONS)
)
print(f"\tGenerated {len(points)} points with {len(points[0])} dimensions.")

# --- build indexer --- # 
print("Building indexer.") 
indexer = BruteForceNNS(
    measure = euclidean_distance,
    verbose = True,
    normalize = settings.NNS_SHOULD_NORMALIZE
) 
indexer.build(points) 

# --- run query --- # 
target = indexer.points[settings.NNS_TARGET] 
nearest = indexer.query(target, settings.NNS_QUERY_COUNT)
for neighbor in nearest:
    print(f"\t\t{neighbor['id']} | {neighbor['distance']}")
