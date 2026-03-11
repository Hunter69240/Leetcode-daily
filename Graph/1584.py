import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)  # Number of points

        # Build adjacency list: For each point, store (cost, other_point) for all other points
        adj = {i: [] for i in range(N)}  # i: list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                # Manhattan distance between points i and j
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's Algorithm to find the Minimum Spanning Tree (MST)
        res = 0              # Total cost to connect all points
        visit = set()        # Points already in MST
        minH = [[0, 0]]      # Min-heap for (cost, point). Start with point 0, cost 0

        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue    # Skip if this node is already in the MST
            res += cost     # Add cost of edge to MST
            visit.add(i)    # Mark the node as visited

            # Consider all neighbors of the current point
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    # Add edge to the heap if the neighbor is not yet in MST
                    heapq.heappush(minH, [neiCost, nei])
        return res  # Return total cost to connect all points
