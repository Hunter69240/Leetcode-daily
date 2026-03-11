class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Goal: choose a subset with maximum sum divisible by 3.
        # Strategy:
        # - Compute total sum.
        # - If total % 3 != 0, remove the SMALLEST amount that fixes the remainder.
        #
        # IMPORTANT TRUTH:
        # A sum with remainder 1 can be formed by:
        #     - one number % 3 == 1
        #     - OR two numbers % 3 == 2   (because 2 + 2 = 4 ≡ 1 mod 3)
        #
        # A sum with remainder 2 can be formed by:
        #     - one number % 3 == 2
        #     - OR two numbers % 3 == 1   (because 1 + 1 = 2 ≡ 2 mod 3)
        #
        # So we track the SMALLEST possible sum that has remainder 1
        # and the SMALLEST possible sum that has remainder 2.

        total = 0

        # smallest_one:
        #     smallest sum we can remove that has remainder 1
        #
        # smallest_two:
        #     smallest sum we can remove that has remainder 2
        #
        # Start them as infinity (unknown or not found yet)
        smallest_one = float("inf")
        smallest_two = float("inf")

        for n in nums:
            total += n

            # CASE 1: n has remainder 1
            if n % 3 == 1:
                # Using this remainder-1 number, we might be able to form
                # a smaller remainder-2 sum:
                #    remainder-2 sum = this remainder-1 + previous remainder-1
                #    (because 1 + 1 = 2 mod 3)
                smallest_two = min(smallest_two, n + smallest_one)

                # This number alone might be the smallest remainder-1 sum
                smallest_one = min(smallest_one, n)

            # CASE 2: n has remainder 2
            if n % 3 == 2:
                # Using this remainder-2 number, we might be able to form
                # a smaller remainder-1 sum:
                #    remainder-1 sum = this remainder-2 + previous remainder-2
                #    (because 2 + 2 = 4 ≡ 1 mod 3)
                smallest_one = min(smallest_one, n + smallest_two)

                # This number alone might be the smallest remainder-2 sum
                smallest_two = min(smallest_two, n)

        # After processing all numbers:
        # CASE 1: total already divisible by 3
        if total % 3 == 0:
            return total

        # CASE 2: total has remainder 1
        # → remove the SMALLEST remainder-1 sum
        if total % 3 == 1:
            return total - smallest_one

        # CASE 3: total has remainder 2
        # → remove the SMALLEST remainder-2 sum
        if total % 3 == 2:
            return total - smallest_two
