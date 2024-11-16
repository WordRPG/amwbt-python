import time
import json

import settings 
from core.utils.generate import generate_points, generate_point
from core.utils.measures import *

class NNSRunner:
    def start(self):
        # --- benchmark times --- # 
        self.benchmark = {
            "build" : 0, 
            "query" : 0
        }

        # --- generate points --- # 
        print("Generating points.") 
        self.points = self.generate_points() 
        print(
            f"\tGenerated {len(self.points)} points with " + \
            f"{len(self.points[0])} dimensions."
        )

        # --- build indexer --- # 
        print("Building indexer.") 
        self.indexer = self.build_indexer()

        # --- run query --- # 
        print("Running query.")
        self.run_query()

        # --- show benchmark results --- # 
        print("Showing benchmark results.")
        self.show_benchmark_results()
    
    def generate_points(self): 
        points = generate_points(
            settings.NNS_POINT_COUNT, 
            lambda: generate_point(settings.NNS_POINT_DIMENSIONS)
        )
        return points

    def build_indexer(self): 
        pass

    def run_query(self):
        indexer = self.indexer
        target = indexer.points[settings.NNS_TARGET] 
        start = time.time()
        results = indexer.query(target, settings.NNS_QUERY_COUNT)
        end = time.time() 
        self.benchmark["query"] = end - start
        nearest = results["nearest"]
        print("\t:: Nearest Neighbors")
        for neighbor in nearest:
            print(f"\t\t{neighbor['id']} | {neighbor['distance']}")
        results["nearest"] = "..."
        print("\t:: Result Info")
        print(json.dumps(results, indent=4))

    def show_benchmark_results(self): 
        print("BUILD DURATION :", round(self.benchmark["build"], 8), "seconds")
        print("QUERY DURATION :", round(self.benchmark["query"], 8), "seconds")

