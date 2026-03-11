class Solution:
    def jump(self, nums: List[int]) -> int:
        # ⚡ PROBLEM TYPE:
        # "Jump Game II" — Find the MINIMUM number of jumps needed to reach
        # the last index of the array. Each element nums[i] tells the maximum
        # jump length from that index.
        #
        # ⚡ WHY A GREEDY APPROACH?
        # At every step, instead of trying all possible jump paths (like DP/backtracking),
        # we choose the jump that takes us the FARTHEST in the next move.
        # This is greedy because we ALWAYS pick what looks like the best immediate option.
        #
        # Greedy observation:
        # - A single jump gives us a *range* of reachable indices.
        # - From that range, we pick the index that allows the farthest future reach.
        # - We don't need to explore alternatives because the *locally optimal choice*
        #   (farthest reach) leads to the *globally optimal result* (min jumps).

        res = 0       # Count of jumps made
        l = r = 0     # Current reachable range (window) from the last jump

        # Continue until we are able to reach or pass the last index
        while r < len(nums) - 1:
            farthest = 0  # The farthest point reachable from the current range

            # Explore all indices we can currently reach
            for i in range(l, r + 1):
                # Calculate how far we can go if we jump from index i
                farthest = max(farthest, i + nums[i])

            # After covering the current window, move to the next layer/window
            l = r + 1     # new left boundary is just after old right boundary
            r = farthest  # new right boundary is the farthest reachable in one more jump
            res += 1      # we used one extra jump to reach this new range

        return res


"""
-------------------- 🔎 DETAILED DRY RUN --------------------

Example Input:
nums = [2, 3, 1, 1, 4]

Index:  0  1  2  3  4
Value:  2  3  1  1  4

Initially:
res = 0
l = 0, r = 0 (we start only at index 0)

-------------------------------------------------
Iteration 1:
Window = [0 → 0] (indices we can currently stand on)

From index 0:
  reachable = 0 + 2 = 2 → farthest = 2

New window becomes:
l = 1, r = 2   (we can now reach indices 1 and 2)
res = 1        (first jump completed)

-------------------------------------------------
Iteration 2:
Window = [1 → 2]

From index 1:
  reachable = 1 + 3 = 4 → farthest = 4
From index 2:
  reachable = 2 + 1 = 3 → farthest remains = 4

New window becomes:
l = 3, r = 4
res = 2        (second jump completed)

Now r (4) >= last index → stop

-------------------------------------------------
Final Answer: 2 jumps


-------------------- 💡 WHY THE GREEDY CHOICE WORKS --------------------

At each jump, instead of deciding exactly WHICH index to land on,
we decide the maximum RANGE we can reach with that jump.

We don't need to track the exact path because:
- If there is a path that reaches farther, taking it is ALWAYS better (minimizes jumps).
- We postpone the choice of exact landing point until we finish scanning the current range.
- This prevents exploring unnecessary paths (unlike DP/backtracking).

So, the algorithm works in "layers" like BFS:
Layer 0 → start at index 0
Layer 1 → reachable from index 0 → [1, 2]
Layer 2 → reachable from [1, 2] → [3, 4]
And the number of layers = minimum jumps.

Time Complexity:  O(n)
Space Complexity: O(1)
Greedy choice confirms global optimality → minimum jumps guaranteed.
"""
