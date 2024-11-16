

import time
import settings
from .nns_runner import NNSRunner 
from core.nns.indexers.vp_tree import VPTree 
from core.utils.measures import * 

nns = NNSRunner() 

def build_brute_force_nns(): 
    start = time.time()
    indexer = VPTree(
        measure = euclidean_distance,
        verbose = True,
        normalize = settings.NNS_SHOULD_NORMALIZE
    ) 
    indexer.build(nns.points) 
    end = time.time()
    nns.benchmark["build"] = end - start
    return indexer

nns.build_indexer = build_brute_force_nns 

nns.start()