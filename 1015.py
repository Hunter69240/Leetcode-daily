class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # We are looking for the smallest number consisting only of 1's
        # (like 1, 11, 111, 1111, ...) that is divisible by k.

        cur = 1   # Current repunit mod k → represents number "1"
        res = 1   # Count of digits in current repunit ("1" has length 1)

        prev = set()  # Track previously seen remainders to detect loops

        # While current remainder is NOT divisible by k
        while cur % k:
            # If we've seen this remainder before, we are in a cycle,
            # meaning no repunit will ever be divisible by k
            if cur in prev:
                return -1

            # Mark this remainder as visited
            prev.add(cur)

            # Instead of forming large numbers, we keep track of remainder only:
            # new number = previous_repunit * 10 + 1
            # So new remainder = (cur * 10 + 1) % k
            cur = 10 * (cur % k) + 1

            # Increase number of digits in our repunit
            res += 1

        # If we break the loop, cur % k == 0 meaning we found divisibility
        return res

'''
🔍 How the Algorithm Works

This problem asks for the length of the smallest number made of only digit 1 that is divisible by k.

Example sequence of repunits:

1 → 11 → 111 → 1111 → ...


Instead of constructing large numbers, we track only the remainder:

if remainder repeats → infinite loop → return -1
else if remainder == 0 → divisible → return length

🧠 DRY RUN EXAMPLE (inside comments)

Let's dry-run with:

k = 7

Step	Repunit	Computed as	cur % 7	res	prev set
1	1	1	1	1	{ }
2	11	(1 * 10 + 1) = 11 → remainder stored as (1 * 10 + 1)	4	2	{1}
3	111	(4 * 10 + 1) = 41	6	3	{1, 11(remainder=4)}
4	1111	(6 * 10 + 1) = 61	5	4	{1,4,6}
5	11111	(5 * 10 + 1) = 51	2	5	{1,4,6,5}
6	111111	(2 * 10 + 1) = 21	0 ✔	6	{1,4,6,5,2}

Final result:

111111 is divisible by 7 → return 6


'''