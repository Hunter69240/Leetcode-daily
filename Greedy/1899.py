class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        ---------------------------------------------------------------------------
        📌 PROBLEM TYPE & WHY
        ---------------------------------------------------------------------------
        This is a greedy filtering problem (LeetCode – Merge Triplets To Form Target Triplet).
        We are given multiple triplets and we want to determine whether we can select
        some of them so that when taking the element-wise maximum across the selected
        triplets, we get exactly the target triplet.

        ---------------------------------------------------------------------------
        💡 INTUITION
        ---------------------------------------------------------------------------
        • A triplet can only contribute to forming the target if NO value in it
          exceeds the corresponding value in the target. Otherwise, it overshoots.
        • To form the target, each of the three target values (index 0, 1, 2)
          must appear exactly in at least one valid triplet.
        • So we collect which indices of the target are "matched"
          and if all 3 (0, 1, 2) are matched, forming the target is possible.

        ---------------------------------------------------------------------------
        🔍 HOW THE CODE WORKS (LINE BY LINE)
        ---------------------------------------------------------------------------
        good = set()                    → keeps track of indices 0/1/2 that match target values
        for t in triplets:              → iterate through every triplet

            if t[0] > target[0] or
               t[1] > target[1] or
               t[2] > target[2]:        → skip this triplet if it has any element larger
                                         than the corresponding target element (it can't help)
                continue

            for i, v in enumerate(t):   → iterate through indices/values of this valid triplet
                if v == target[i]:      → if value matches target at the same index
                    good.add(i)         → store that this index is satisfied

        return len(good) == 3           → if all 3 indices are satisfied, we can form target

        ---------------------------------------------------------------------------
        🧪 DRY RUN EXAMPLE
        ---------------------------------------------------------------------------
        triplets = [[2,5,3], [1,8,4], [2,3,3], [2,5,5]]
        target   = [2,5,3]

        good = {}

        triplet [2,5,3] → valid (no element > target)
                          matches target at index 0 → good = {0}
                          matches target at index 1 → good = {0,1}
                          matches target at index 2 → good = {0,1,2}

        triplet [1,8,4] → skip (8 > 5, overshoots)

        triplet [2,3,3] → valid
                          matches target at index 0 (already in set)
                          matches target at index 2 (already in set)

        triplet [2,5,5] → skip (5 > 3, overshoots)

        final good = {0,1,2} → size is 3 → return True

        ---------------------------------------------------------------------------
        END SUMMARY
        ---------------------------------------------------------------------------
        ✔ Problem asks if we can merge triplets to exactly match target using max rule
        ✔ Triplets that overshoot are ignored
        ✔ Each index of target must be matched by at least one allowed triplet
        ✔ If we match indices 0, 1, and 2 → merging is possible → return True
        ---------------------------------------------------------------------------
        '''

        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3
