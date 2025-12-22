def s():

    numbers = [2, 3, 4]
    target = 6

    i = 0
    j = len(numbers) - 1

    # ---------------------------------------------------------
    # EXPLANATION:
    # This is the "Two Sum II - Input Array Is Sorted" problem.
    #
    # The array is already sorted.
    #
    # TWO POINTER + GREEDY IDEA:
    # - i starts at the beginning (smallest number)
    # - j starts at the end (largest number)
    #
    # At each step:
    # - If numbers[i] + numbers[j] == target → answer found
    # - If sum < target → move i right to increase sum
    # - If sum > target → move j left to decrease sum
    #
    # Why greedy?
    # - Because the array is sorted, moving pointers always moves
    #   the sum in the correct direction.
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # DRY RUN:
    #
    # numbers = [2, 3, 4], target = 6
    #
    # i=0 → numbers[i]=2
    # j=2 → numbers[j]=4
    #
    # curr_sum = 2 + 4 = 6
    # curr_sum == target → return [1, 3]
    #
    # (indices are 1-based as required)
    # ---------------------------------------------------------

    while i < j:
        curr_sum = numbers[i] + numbers[j]

        if curr_sum == target:
            return [i + 1, j + 1]

        # NOTE:
        # There is a small typo here in the original code:
        # `elif sum < target:` should be `elif curr_sum < target:`

        elif curr_sum < target:
            i += 1
        else:
            j -= 1


a = s()
print(a)
