def s():
    arr = [0, 1, 0, 2]
    n = len(arr)

    zeroes = arr.count(0)

    # ---------------------------------------------------------
    # EXPLANATION:
    # This problem duplicates each zero in the array IN-PLACE.
    # Elements to the right are shifted, and elements beyond
    # array length are discarded.
    #
    # Key idea:
    # - Count number of zeros.
    # - Imagine the array is extended by `zeroes` extra spaces.
    # - Use two pointers moving from RIGHT to LEFT:
    #     i → original array index
    #     j → virtual expanded array index
    #
    # We copy values backward to avoid overwriting needed data.
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # DRY RUN:
    #
    # arr = [0, 1, 0, 2]
    # n = 4
    # zeroes = 2
    #
    # Virtual array size = n + zeroes = 6
    #
    # i = 3 (points to 2)
    # j = 5 (virtual index)
    #
    # ---------------------------------------------------------
    # i=3, arr[i]=2 (not zero)
    #   j=5 >= n → do nothing
    #   j=4
    #   i=2
    #
    # i=2, arr[i]=0
    #   j=4 >= n → do nothing
    #   j=3
    #   j < n → arr[3] = 0
    #   j=2
    #   i=1
    #
    # arr now: [0,1,0,0]
    #
    # i=1, arr[i]=1
    #   j < n → arr[2] = 1
    #   j=1
    #   i=0
    #
    # arr now: [0,1,1,0]
    #
    # i=0, arr[i]=0
    #   j < n → arr[1] = 0
    #   j=0
    #   j < n → arr[0] = 0
    #   j=-1
    #   i=-1 → stop
    #
    # FINAL ARRAY:
    # [0, 0, 1, 0]
    # ---------------------------------------------------------

    i = n - 1
    j = n + zeroes - 1

    while i >= 0:
        if arr[i] != 0:
            if j < n:
                arr[j] = arr[i]
            j -= 1
            i -= 1
        else:
            if j < n:
                arr[j] = 0
            j -= 1

            if j < n:
                arr[j] = 0
            j -= 1
            i -= 1

    return arr


a = s()
print(a)
