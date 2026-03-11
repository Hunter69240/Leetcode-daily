class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        
        Problem: Course Schedule II (Topological Sort)
        Goal: Return an order of courses you can take to finish all.
               If impossible (cycle exists), return [].
        """

        # Build adjacency list for prerequisites
        # Key = course, Value = list of prerequisites for that course
        prereq = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # States for each course:
        # - visited: course is already processed and added to output
        # - visiting: course is in the current recursion stack (checking dependencies)
        # - unvisited: not yet seen
        output = []       # result (valid course order)
        visit = set()     # courses fully processed
        cycle = set()     # current path of recursion (detects cycles)

        # Depth-First Search helper
        def dfs(crs):
            # If course is already in recursion path → cycle detected
            if crs in cycle:
                return False

            # If course is already processed → no need to redo
            if crs in visit:
                return True

            # Mark course as being visited (part of recursion stack)
            cycle.add(crs)

            # Check all prerequisites (dependencies)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False  # if cycle found in prereq, fail immediately

            # Done exploring prereqs → remove from cycle
            cycle.remove(crs)

            # Mark as processed and add to output
            visit.add(crs)
            output.append(crs)

            return True

        # Run DFS on every course (important for disconnected graphs)
        for c in range(numCourses):
            if dfs(c) == False:
                return []  # cycle detected → impossible to complete all

        return output  # valid order (reverse topological order)
