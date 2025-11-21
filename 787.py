#Bellman Ford algo - can handle negative weights compared to dijkstra

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize price array with "infinity" (can't reach initially)
        prices = [float("inf")] * n
        prices[src] = 0  # cost to reach source = 0

        # Relax edges up to k+1 times (Bellman-Ford style)
        # Why k+1? Because with k stops, there can be at most k+1 edges
        for i in range(k + 1):
            tmpPrices = prices.copy()  # temp copy to avoid using updated values in same iteration
            for s, d, p in flights:  # s = source, d = destination, p = price
                # If we can't reach 's', skip
                if prices[s] == float("inf"):
                    continue
                # Update minimum cost to reach destination 'd'
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices  # update the prices for the next iteration

        # If destination is still infinity, it means unreachable
        return -1 if prices[dst] == float("inf") else prices[dst]


