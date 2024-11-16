from core.utils.operations import *

class Point:
    def __init__(self, id_, value): 
        self.id = id_
        self.value = value 
        self.magnitude = None 

    def __repr__(self): 
        return f"Point({','.join([str(round(x, 4)) for x in self.value])})"
    
    def normalized(self):
        magnitude_  = magnitude(self.value) 
        normalized_ = normalize(self.value)
        return magnitude_, normalized_

    def normalize(self): 
        magnitude_  = magnitude(self.value) 
        normalized_ = normalize(self.value)
        self.magnitude = magnitude_
        self.value = normalized_ 


