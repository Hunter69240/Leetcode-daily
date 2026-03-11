from collections import Counter

def threeSumMulti(arr, target):
    MOD = 10**9 + 7
    freq = Counter(arr)
    keys = sorted(freq.keys())
    res = 0

    # ---------------------------------------------------------
    # EXPLANATION:
    # We need to count the number of triplets (i, j, k) such that:
    #   arr[i] + arr[j] + arr[k] == target
    # and i < j < k (order matters by index, not by value).
    #
    # Instead of indices, we work with VALUES and their FREQUENCIES.
    #
    # Steps:
    # 1) Count frequency of each number using Counter
    # 2) Iterate over all possible (a, b) pairs from sorted keys
    # 3) Compute c = target - a - b
    # 4) Ensure ordering: a <= b <= c
    # 5) Count combinations based on whether values are equal
    #
    # Combination formulas:
    # - All same (a == b == c): nC3
    # - Two same:
    #     a == b < c → nC2 * freq[c]
    #     a < b == c → freq[a] * nC2
    # - All different (a < b < c): freq[a] * freq[b] * freq[c]
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # DRY RUN:
    #
    # arr = [1,1,2,2,2,2]
    # target = 5
    #
    # freq = {1:2, 2:4}
    # keys = [1,2]
    #
    # i=0 → a=1
    #   j=0 → b=1
    #     c = 5 - 1 - 1 = 3
    #     3 not in freq → skip
    #
    #   j=1 → b=2
    #     c = 5 - 1 - 2 = 2
    #     a < b == c
    #     count = freq[1] * (freq[2] * (freq[2]-1) // 2)
    #           = 2 * (4*3//2)
    #           = 2 * 6
    #           = 12
    #
    # i=1 → a=2
    #   j=1 → b=2
    #     c = 5 - 2 - 2 = 1
    #     c < b → skip
    #
    # FINAL RESULT = 12
    # ---------------------------------------------------------

    for i in range(len(keys)):
        a = keys[i]
        for j in range(i, len(keys)):
            b = keys[j]
            c = target - a - b

            # ensure ordering a <= b <= c
            if c < b:
                continue

            # c must exist in array
            if c not in freq:
                continue

            # case 1: a == b == c
            if a == b == c:
                n = freq[a]
                res += n * (n - 1) * (n - 2) // 6

            # case 2: a == b < c
            elif a == b < c:
                res += freq[a] * (freq[a] - 1) // 2 * freq[c]

            # case 3: a < b == c
            elif a < b == c:
                res += freq[a] * (freq[b] * (freq[b] - 1) // 2)

            # case 4: a < b < c
            elif a < b < c:
                res += freq[a] * freq[b] * freq[c]

            res %= MOD

    return res


a = [1,1,2,2,2,2]
b = 5
print(threeSumMulti(a, b))
