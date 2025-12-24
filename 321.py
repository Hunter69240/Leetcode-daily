class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        # ---------------------------------------------------------
        # EXPLANATION (HIGH LEVEL):
        # We want to create the LARGEST possible number of length k
        # using digits from nums1 and nums2.
        #
        # Rules:
        # - Relative order inside nums1 must be preserved
        # - Relative order inside nums2 must be preserved
        #
        # STRATEGY:
        # 1) Decide how many digits to take from nums1 (say i)
        #    and nums2 (k - i)
        # 2) From each array, pick the MAXIMUM subsequence of that length
        # 3) Merge the two subsequences greedily to form the largest number
        # 4) Try all valid splits and keep the best result
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # FUNCTION 1: maxSubsequence(nums, k)
        #
        # Greedy + Monotonic Stack
        #
        # Goal:
        # Pick k digits from nums (keeping order)
        # such that the resulting sequence is MAXIMUM.
        #
        # Idea:
        # - We can drop (len(nums) - k) elements
        # - While the current number is larger than the last chosen
        #   and we still can drop elements, pop the stack
        # ---------------------------------------------------------
        def maxSubsequence(nums, k):
            stack = []
            drop = len(nums) - k   # how many elements we are allowed to drop

            for num in nums:
                # Remove smaller elements if a bigger one appears
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            # Only keep first k elements
            return stack[:k]

        # ---------------------------------------------------------
        # FUNCTION 2: merge(seq1, seq2)
        #
        # Merge two sequences to form the maximum possible number.
        #
        # Greedy rule:
        # - Compare seq1 and seq2 lexicographically
        # - Take from the sequence which is GREATER
        #
        # This ensures the leftmost digit is as large as possible.
        # ---------------------------------------------------------
        def merge(seq1, seq2):
            res = []
            while seq1 or seq2:
                if seq1 > seq2:
                    res.append(seq1.pop(0))
                else:
                    res.append(seq2.pop(0))
            return res

        best = []
        m, n = len(nums1), len(nums2)

        # ---------------------------------------------------------
        # TRY ALL VALID SPLITS
        #
        # i = number of digits taken from nums1
        # k - i = number of digits taken from nums2
        #
        # Constraints:
        # - i cannot exceed len(nums1)
        # - k - i cannot exceed len(nums2)
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        #
        # nums1 = [3,4,6,5]
        # nums2 = [9,1,2,5,8,3]
        # k = 5
        #
        # Try splits:
        # i = 1 → nums1:1, nums2:4
        # i = 2 → nums1:2, nums2:3
        # i = 3 → nums1:3, nums2:2
        # i = 4 → nums1:4, nums2:1
        #
        # For each split:
        # - compute maxSubsequence from nums1
        # - compute maxSubsequence from nums2
        # - merge them greedily
        # - keep the maximum result
        # ---------------------------------------------------------

        for i in range(max(0, k - n), min(k, m) + 1):

            # Pick i digits from nums1
            part1 = maxSubsequence(nums1, i)

            # Pick k-i digits from nums2
            part2 = maxSubsequence(nums2, k - i)

            # Merge both parts to get a candidate result
            candidate = merge(part1[:], part2[:])

            # Keep the best lexicographical result
            best = max(best, candidate)

        return best
