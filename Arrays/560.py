class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        freq = {0: 1}   # prefix sum 0 occurs once (important)
        count = 0

        # ---------------------------------------------------------
        # EXPLANATION:
        # We use prefix sums and a frequency map.
        #
        # prefix_sum = sum of elements from index 0 to current index
        #
        # If:
        #   prefix_sum - k has appeared before,
        # then there exists a subarray ending at current index
        # whose sum is exactly k.
        #
        # freq keeps track of how many times each prefix_sum occurred.
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        # nums = [1, 1, 1], k = 2
        #
        # Initial:
        # prefix_sum = 0
        # freq = {0:1}
        # count = 0
        #
        # num = 1:
        #   prefix_sum = 1
        #   prefix_sum - k = -1 → not in freq
        #   freq = {0:1, 1:1}
        #
        # num = 1:
        #   prefix_sum = 2
        #   prefix_sum - k = 0 → in freq (1 time)
        #   count += 1 → count = 1
        #   freq = {0:1, 1:1, 2:1}
        #
        # num = 1:
        #   prefix_sum = 3
        #   prefix_sum - k = 1 → in freq (1 time)
        #   count += 1 → count = 2
        #   freq = {0:1, 1:1, 2:1, 3:1}
        #
        # FINAL ANSWER: 2
        # Subarrays: [1,1] (index 0–1), [1,1] (index 1–2)
        # ---------------------------------------------------------

        for num in nums:
            # Add current number to prefix sum
            prefix_sum += num

            # Check if there exists a prefix sum that makes subarray sum = k
            if (prefix_sum - k) in freq:
                count += freq[prefix_sum - k]

            # Record current prefix sum frequency
            if prefix_sum in freq:
                freq[prefix_sum] += 1
            else:
                freq[prefix_sum] = 1

        return count
