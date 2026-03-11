class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]  # List of directed edges (u -> v with travel time w)
        :type n: int                  # Number of nodes in the graph
        :type k: int                  # Starting node
        :rtype: int                   # Minimum time for all nodes to receive the signal, or -1 if impossible
        """

        # Build adjacency list (graph representation)
        # edges[u] will contain a list of (v, w), where v is neighbor and w is weight (time to reach v)
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # Min-heap (priority queue) => (time_taken, current_node)
        # Start from node k with time 0
        minHeap = [(0, k)]

        # Set to track visited nodes
        visit = set()

        # Variable to keep track of the maximum time taken (final answer)
        t = 0

        # Dijkstra's Algorithm using a min-heap
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # Pop the node with the smallest travel time

            if n1 in visit:  
                continue  # Skip if already visited

            visit.add(n1)  
            t = max(t, w1)  # Update max time so far (latest reached node time)

            # Explore neighbors
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # Push cumulative travel time to reach n2
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # If all n nodes were visited, return max travel time
        # Otherwise, return -1 (not all nodes are reachable)
        return t if len(visit) == n else -1
