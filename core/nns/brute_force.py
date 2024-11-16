
from .indexer import Indexer

class BruteForceNNS(Indexer): 
    def __init__(self, *args, **kwargs): 
        Indexer.__init__(self, *args, **kwargs)
    
    """
        TREE QUERIES 
    """ 
    def query(self, target, k): 
        nearest = [] 
        for i in range(len(self.points)): 
            otherPoint = self.points[i]
            distance = self.measure(target.value, otherPoint.value) 
            nearest.append({ "id" : otherPoint.id, "distance" : distance })
        nearest.sort(key=lambda x: x["distance"])
        nearest = nearest[:k]
        return nearest