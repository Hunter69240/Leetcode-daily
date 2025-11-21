#djkstra #topological_sorting #graph_theory
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Build adjacency list for all unique chars in words
        adj = {c: set() for w in words for c in w}

        # Step 2: Compare adjacent words to infer precedence rules
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # invalid case: word1 is longer but word2 is prefix, e.g. ["abc", "ab"]
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # find the first difference to establish ordering
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # w1[j] must come before w2[j]
                    adj[w1[j]].add(w2[j])
                    break  # only first differing character matters

        # Step 3: DFS for topological sorting
        visit = {}  # keeps track of visiting state: True = currently in path, False = visited completely
        res = []    # stores the result (topo order)

        def dfs(c):
            # if already visited, return its state
            if c in visit:
                return visit[c]  # True means cycle detected

            visit[c] = True  # mark as being visited (currently in recursion stack)

            # visit all neighbors (characters that must come after c)
            for nei in adj[c]:
                if dfs(nei):  # cycle found
                    return True
            
            visit[c] = False  # mark as finished visiting
            res.append(c)     # add to topological sort order (post-order)
        
        # Step 4: Run DFS on all characters
        for c in adj:
            if dfs(c):  # if cycle detected, return ""
                return ""

        # Step 5: reverse the result to get correct order
        res.reverse()
        return "".join(res)
