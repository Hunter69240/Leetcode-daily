def a():
    nums = [1,2,1,2,1,2,3,1,3,2]
    k = 2

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    # Step 1: Count frequency of each number
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # Dry Run after loop:
    # nums = [1,2,1,2,1,2,3,1,3,2]
    # count = {
    #   1:4,
    #   2:4,
    #   3:2
    # }

    # Step 2: Place numbers into buckets based on frequency
    for n, c in count.items():
        freq[c].append(n)

    # Dry Run after bucket filling:
    # freq index = frequency
    #
    # freq[0] = []
    # freq[1] = []
    # freq[2] = [3]
    # freq[3] = []
    # freq[4] = [1,2]
    # freq[5] = []
    # ...
    # freq[10] = []

    res = []

    # Step 3: Traverse from highest frequency
    for i in range(len(freq)-1, 0, -1):

        # i=10 → []
        # i=9  → []
        # ...
        # i=4  → [1,2]

        for n in freq[i]:
            res.append(n)

            # Dry Run:
            # First iteration
            # res = [1]

            # Second iteration
            # res = [1,2]

            if len(res) == k:
                return res


print(a())

# Final Output
# [1,2]
# (Top 2 frequent elements)