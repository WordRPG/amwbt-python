""" 
    BRUTE FORCE NEAREST NEIGHBOR SEARCH
""" 

from .indexer import Indexer

class BruteForceNNS(Indexer): 
    def __init__(self, *args, **kwargs): 
        Indexer.__init__(self, *args, **kwargs)
    
    """
        TREE QUERIES 
    """ 
    def query(self, target, k): 
        # --- main results --- #
        results = {}

        # --- search for nearest neighbors --- # 
        nearest = [] 
        for i in range(len(self.points)): 
            other_point = self.points[i]
            distance = self.measure(target.value, other_point.value) 
            nearest.append({ "id" : other_point.id, "distance" : distance })
        nearest.sort(key=lambda x: x["distance"])
        nearest = nearest[:k]

        # --- make results --- # 
        results = {
            "nearest" : nearest,
            "visitCounts" : {
                "pointsVisited" : len(self.points)
            } 
        }

        return results