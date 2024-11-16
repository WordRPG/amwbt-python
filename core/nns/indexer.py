from core.nns.point import Point
from core.utils.measures import * 

class Indexer:
    def __init__(
        self,
        measure = euclidean_distance,
        verbose = False,
        normalize = True,
        indent = 1, 
        PointClass = Point,
        inversed = False 
    ):  
        # --- point storage --- #    
        self.points = [] 

        # --- measurement basis --- # 
        self.measure = measure

        # --- verbose logging ---- # 
        self.verbose = verbose

        # --- indent --- # 
        self.indent = "\t" * indent 

        # --- whether to normalize points --- # 
        self.normalize = normalize   

        # --- point class to use --- # 
        self.PointClass = Point

        # --- (optional) tree root --- #
        self.root = {}

    """ 
        TREE CONSTRUCTION
    """ 

    def build(self, points):
        print(f"{self.indent}-- Building...")
        self.add_points(points) 
        self.build_indexer(points)
    
    def add_points(self, points): 
        print(f"{self.indent}-- Adding points.")
        for i in range(len(points)):
            point = self.PointClass(i, points[i])
            if self.normalize: 
                point.normalize()
            self.points.append(point) 

    def build_indexer(self, points): 
        print(f"{self.indent}-- Building indexer") 


     

