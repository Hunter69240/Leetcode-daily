class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Build adjacency list (course -> list of prerequisites)
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Set to track the recursion path (helps detect cycles)
        visitSet = set()

        # DFS to check if course can be completed
        def dfs(crs):
            # Case 1: Cycle detected (course already in current path)
            if crs in visitSet:
                return False

            # Case 2: No prerequisites left → this course is already resolvable
            if preMap[crs] == []:
                return True

            # Add course to recursion path
            visitSet.add(crs)

            # Check all prerequisites recursively
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # Remove course from recursion path (backtrack)
            visitSet.remove(crs)

            # Optimization: mark course as resolved (empty prereq list)
            preMap[crs] = []
            return True

        # Run DFS for every course
        for crs in range(numCourses):
            if not dfs(crs):  # cycle found → cannot finish
                return False

        return True  # no cycles → all courses can be finished
