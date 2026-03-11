class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build adjacency list for the tree
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res = 0  # To count number of connected components where sum % k == 0

        def dfs(cur, parent):
            """
            DFS returns the total sum of values of the subtree rooted at 'cur'.
            'parent' ensures we don't go back up the tree.
            """
            total = values[cur]  # Start with current node's value

            # Traverse all neighbors (children)
            for child in adj[cur]:
                if child != parent:  # Avoid revisiting parent
                    total += dfs(child, cur)  # Add subtree sum from child

            # If sum of this subtree is divisible by k, we count it as a component
            if total % k == 0:
                nonlocal res
                res += 1

            return total  # Return cumulative sum for parent's use

        dfs(0, -1)  # Start DFS from node 0 (root), parent = -1 (none)

        return res


'''
n = 5
edges = [[0,1],[1,2],[1,3],[3,4]]
values = [2, 3, 5, 4, 1]
k = 5

        0(2)
        |
        1(3)
      /     \
   2(5)     3(4)
              |
             4(1)

             dfs(0):
  dfs(1):
    dfs(2):
      total = 5 → 5 % 5 == 0 → res = 1
      return 5

    dfs(3):
      dfs(4):
        total = 1 → 1 % 5 != 0 → res stays 1
        return 1
      total = 4 + 1 = 5 → 5 % 5 == 0 → res = 2
      return 5

    total = 3 + 5 + 5 = 13 → 13 % 5 != 0 → res stays 2
    return 13

  total = 2 + 13 = 15 → 15 % 5 == 0 → res = 3
  return 15

  res = 3


'''