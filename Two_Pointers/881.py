def s():
    people = [1, 2]
    limit = 3
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    # ---------------------------------------------------------
    # EXPLANATION:
    # This is the "Boats to Save People" problem.
    #
    # Each boat can carry at most 2 people.
    # Total weight on a boat must be ≤ limit.
    #
    # GREEDY STRATEGY:
    # Always try to pair the LIGHTEST person with the HEAVIEST person.
    #
    # Why greedy?
    # - The heaviest person is the hardest to place.
    # - If the lightest person can ride with the heaviest, we save a boat.
    # - If not, the heaviest must go alone anyway.
    #
    # TWO POINTERS:
    # - left  → lightest person
    # - right → heaviest person
    #
    # After placing the heaviest person, we always move `right`.
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # DRY RUN:
    #
    # people = [1, 2]
    # limit = 3
    #
    # After sort → [1, 2]
    #
    # left=0 (1), right=1 (2)
    #
    # 1 + 2 <= 3 → they share one boat
    # left → 1
    # right → 0
    # boats = 1
    #
    # left > right → stop
    #
    # FINAL RESULT: 1 boat
    # ---------------------------------------------------------

    while left <= right:
        # Try to pair the lightest with the heaviest
        if people[left] + people[right] <= limit:
            left += 1      # lightest person is used

        # heaviest person always uses a boat
        right -= 1
        boats += 1

    return boats


a = s()
print(a)
