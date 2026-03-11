class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # 📌 PROBLEM TYPE:
        # "Minimum Subarray to Remove for Divisibility"
        # Given an array `nums` and a number `p`, remove the **smallest length subarray**
        # so that the sum of the remaining array is divisible by `p`.
        #
        # If no such subarray exists, return -1.
        #
        # Example:
        # nums = [3,1,4,2], p = 6
        # total sum = 10 → 10 % 6 = 4, so we must remove a subarray whose sum ≡ 4 (mod 6)
        # Smallest such subarray is [4,2] of length 2 → answer = 2

        total = sum(nums)
        remain = total % p

        # 🧠 If the total sum is already divisible by p, no need to remove anything
        if remain == 0:
            return 0

        res = len(nums)      # best (minimum) subarray length found
        cur_sum = 0          # running prefix sum mod p
        remain_to_idx = {0: -1}  # map: (prefix sum mod p) → earliest index

        # 🧠 INTUITION:
        # We want to remove a subarray whose sum % p == remain
        #
        # Let:
        #   prefix(i) = (nums[0] + nums[1] + ... + nums[i]) % p
        #
        # We need: (prefix(i) - prefix(j)) % p = remain
        #   → prefix(j) = (prefix(i) - remain + p) % p
        #
        # So we look for prefix(j) seen earlier that matches this target.
        # j+1 .. i will be the removable subarray, length = i - j.

        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n) % p

            # target prefix that would make subarray removal divisibility valid
            prefix = (cur_sum - remain + p) % p

            # If we have seen this prefix before, we found a candidate subarray
            if prefix in remain_to_idx:
                length = i - remain_to_idx[prefix]
                res = min(res, length)

            # Always store the latest index of cur_sum (best for shorter subarrays later)
            remain_to_idx[cur_sum] = i

        # If no valid subarray was found, res stayed equal to len(nums)
        return -1 if res == len(nums) else res


"""
-------------------------- 🔎 DRY RUN EXAMPLE --------------------------

Input:
nums = [3, 1, 4, 2], p = 6
total = 10, total % 6 = 4 → we need to remove a subarray whose sum % 6 = 4

Initial:
res = 4
cur_sum = 0
remain_to_idx = {0: -1}

i = 0, n = 3
cur_sum = (0 + 3) % 6 = 3
prefix = (3 - 4 + 6) % 6 = 5   → not in map
remain_to_idx = {0:-1, 3:0}

i = 1, n = 1
cur_sum = (3 + 1) % 6 = 4
prefix = (4 - 4 + 6) % 6 = 0   → FOUND (at index -1)
length = 1 - (-1) = 2
res = 2
remain_to_idx = {0:-1, 3:0, 4:1}

i = 2, n = 4
cur_sum = (4 + 4) % 6 = 2
prefix = (2 - 4 + 6) % 6 = 4   → FOUND (at index 1)
length = 2 - 1 = 1
res = 1
remain_to_idx = {0:-1, 3:0, 4:1, 2:2}

i = 3, n = 2
cur_sum = (2 + 2) % 6 = 4
prefix = (4 - 4 + 6) % 6 = 0   → FOUND (at index -1)
length = 3 - (-1) = 4 → not better than res=1
remain_to_idx = {0:-1, 3:0, 4:3, 2:2}

End:
res = 1 → remove subarray [4] (index 2)

------------------------------------------------------------
⏱ Complexity:
Time  → O(n)
Space → O(n) for the hashmap

------------------------------------------------------------
"""
