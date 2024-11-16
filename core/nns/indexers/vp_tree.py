
""" 
    VANTAGE POINT TREE 
    -------------------------------------------------------------------------------------
    Modified version of: 
        https://github.com/RickardSjogren/vptree/blob/master/vptree.py
    -------------------------------------------------------------------------------------
""" 
from ..indexer import Indexer
from core.utils.operations import median

import math
import stats

class VPTree(Indexer): 
    def __init__(self, 
            verbose_build = False,
            *args, 
            **kwargs
        ): 
        Indexer.__init__(self, *args, **kwargs) 

        # --- verbosity controls --- #
        self.verbose_build = verbose_build 

    """ 
        TREE CONSTRUCTION 
    """ 
    def build_indexer(self, points):   
        state = {}
        self.root = self.build_for(state, points, 0)
        self.tree_info["innerNodeCount"] = \
            self.tree_info["nodeCount"] - self.tree_info["leaves"]["count"]
             
    def build_for(self, state, points, depth): 
        # --- build tree recursively --- #
        vantage_point = points[0]
        points = points[1:]  

        # --- update details in tree info --- #  
        if self.verbose_build: 
            print(f"{self.indent}\t--- Adding point {state['nodeVisits']}")   
        self.tree_info["nodeCount"] += 1 
        
        if depth not in self.tree_info["levels"]:
            self.tree_info["levels"][depth] = 0 
        self.tree_info["levels"][depth] += 1 

        # --- if there is only one point left (no children), return leaf node --- # 
        if len(points) == 0:    
            self.tree_info["leaves"]["count"] += 1 
            if depth not in self.tree_info["leaves"]["levels"]:
                self.tree_info["leaves"]["levels"][depth] = 0 
            self.tree_info["leaves"]["levels"][depth] += 1 

            node = {
                "id" : vantage_point.id, 
                "is_leaf" : True 
            }
            return node 

        # --- choose division boundary at median of distances --- #
        distances = [self.measure(vantage_point.value, point.value) for point in points] 
        distances.sort()
        median_index = len(distances) // 2 
        median_distance = median(distances)

        # --- build left and right children --- #
        left_points  = [] 
        right_points = []
        
        left_min     = math.inf
        left_max     = 0
        
        right_min    = math.inf
        right_max    = 0

        for i in range(len(points)):
            other_point = points[i] 
            distance = distances[i]

            if distance >= median_distance: 
                right_min = min(distance, right_min)
                if distance > right_max:
                    right_max = distance 
                    right_points.insert(0, other_point)
                else: 
                    right_points.append(other_point)  
            
            else: 
                left_min = min(distance, left_min)
                if distance > left_max: 
                    left_max = distance 
                    left_points.insert(0, other_point) 
                else: 
                    left_points.append(other_point)

        # --- build left and right nodes --- #
        if len(left_points) > 0:
            left_node = self.build_for(state, left_points, depth + 1)
        else:
            left_node = None 

        if len(right_points) > 0:
            right_node = self.build_for(state, right_points, depth + 1) 
        else:
            right_node = None 

        # --- make node --- # 
        node = {
            "id" : vantage_point.id, 
            "left_min" : left_min, 
            "left_max" : left_max,
            "right_min" : right_min, 
            "right_max" : right_max,
            "left" : left_node,
            "right" : right_node
        }

        return node

    """ 
        TREE QUERY
    """ 
    def query(self, target, k): 
        pass

