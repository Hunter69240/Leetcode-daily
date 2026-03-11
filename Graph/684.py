class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Number of edges (since the graph has N nodes and N edges, N = len(edges))
        N = len(edges)

        # Initialize parent array for Union-Find (1-indexed)
        par = [i for i in range(N + 1)]

        # Initialize rank (size of each set, used for union by size)
        rank = [1] * (N + 1)

        # Find function with path compression
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])   # Path compression step
            return par[n]

        # Union function with union by rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # If both nodes already have the same parent → cycle detected
            if p1 == p2:
                return False

            # Union by size/rank: attach smaller tree to bigger one
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Iterate over all edges
        for n1, n2 in edges:
            # If union fails (cycle found), this is the redundant edge
            if not union(n1, n2):
                return [n1, n2]
