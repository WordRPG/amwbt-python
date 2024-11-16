
""" 
    VANTAGE POINT TREE 
    -------------------------------------------------------------------------------------
    Modified version of: 
        https://github.com/RickardSjogren/vptree/blob/master/vptree.py
    -------------------------------------------------------------------------------------
""" 
from ..indexer import Indexer

class VPTree(Indexer): 
    def __init__(self, *args, **kwargs): 
        Indexer.__init__(self, *args, **kwargs) 

    """ 
        TREE CONSTRUCTION 
    """ 
    def build_indexer(self, points): 
        pass  

    """ 
        TREE QUERY
    """ 
    def query(self, target, k): 
        pass
