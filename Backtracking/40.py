class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()   # sort first, so we can skip duplicates easily

        # dfs(i, cur, total)
        # i     -> current index in candidates
        # cur   -> current combination being built
        # total -> current sum of cur
        def dfs(i, cur, total):
            # ✅ base case: found a valid combination
            if total == target:
                res.append(cur.copy())
                return

            # ❌ base case: sum exceeded OR no more candidates left
            if total > target or i >= len(candidates):
                return 

            # decision 1: include candidates[i]
            cur.append(candidates[i])
            # here we move to i+1 (not i), because we can't reuse the same element
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()   # backtrack

            # decision 2: skip candidates[i]
            # BUT: skip all duplicates of candidates[i] to avoid repeated results
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        # start recursion
        dfs(0, [], 0)
        return res
