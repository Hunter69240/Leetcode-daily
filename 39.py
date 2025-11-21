class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []   # stores all valid combinations that sum to target

        # dfs(i, cur, total)
        # i -> current index in candidates list
        # cur -> current combination being built
        # total -> current sum of cur
        def dfs(i, cur, total):
            # ✅ base case: found a valid combination
            if total == target:
                res.append(cur.copy())  # add a copy of current list
                return 
            
            # ❌ base case: out of bounds OR sum exceeded target
            if i >= len(candidates) or total > target:
                return
            
            # decision 1: include candidates[i]
            cur.append(candidates[i])
            # note: we pass "i" (not i+1), because we can reuse the same number
            dfs(i, cur, total + candidates[i])
            
            # backtrack: undo the choice
            cur.pop()

            # decision 2: skip candidates[i] and move forward
            dfs(i + 1, cur, total)

        # start recursion
        dfs(0, [], 0)
        return res
