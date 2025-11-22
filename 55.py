class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Intuition:
        # We move **backwards** from the end and try to track the earliest index
        # that can reach the goal.
        #
        # - Start with goal = last index.
        # - If from position i you can jump to (or beyond) the current goal,
        #   then we update the goal to i.
        # - In the end, if the goal becomes 0, it means the first index can reach
        #   the last index through a chain of possible jumps.
        #
        # Example:
        # nums = [2, 3, 1, 1, 4]
        # goal = 4 (last index)
        # i = 4 → 4 + nums[4]=4 ≥ goal → goal = 4
        # i = 3 → 3 + 1 = 4 ≥ goal → goal = 3
        # i = 2 → 2 + 1 = 3 ≥ goal → goal = 2
        # i = 1 → 1 + 3 = 4 ≥ goal → goal = 1
        # i = 0 → 0 + 2 = 2 ≥ goal → goal = 0
        # Since goal reaches 0 → return True
        #
        # This greedy method ensures O(n) time and no extra space.

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
