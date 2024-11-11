import numpy as np
from collections import Counter

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for p in points:
            x = p[0]
            y = p[1]
            dist.append(x*x + y*y)

        dist_point = list(zip(points, dist))
        # print(dist_point)
        dist_point.sort(key = lambda x: x[1])
        dist_point = [x[0] for x in dist_point[:k]]
        return dist_point

        