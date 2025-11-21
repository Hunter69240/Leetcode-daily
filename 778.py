import heapq  # required for using min heap (priority queue)

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)  # size of the NxN grid
        visit = set()  # keeps track of visited cells
        # min-heap with tuple: (time, row, col)
        # initially it starts at the top-left cell with its height = grid[0][0]
        minH = [[grid[0][0], 0, 0]]
        
        # possible movement directions (right, left, down, up)
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))  # mark the starting cell as visited

        # process until reaching the bottom-right cell
        while minH:
            # take the cell with the smallest "time" (i.e. min water level)
            t, r, c = heapq.heappop(minH)

            # if we reached the destination cell, return the required time
            if r == N - 1 and c == N - 1:
                return t

            # explore all 4 directions
            for dr, dc in direction:
                neiR, neiC = r + dr, c + dc

                # check if neighbor is inside bounds and not yet visited
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                    continue

                visit.add((neiR, neiC))  # mark neighbor as visited
                # push neighbor into heap:
                # - Time is the max of current time t and the cell's height
                #   because we can only enter when the water level is >= cell's height
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
