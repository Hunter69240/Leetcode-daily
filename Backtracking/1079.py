tiles = "AAABBC"

# Build frequency map manually
# This stores how many of each tile we can still use
# A -> 3, B -> 2, C -> 1
freq = {}
for ch in tiles:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1


def backtrack():
    # total stores number of valid sequences formed
    # every time we pick a letter -> we form a new sequence
    # and then try to extend it further
    total = 0

    # try using every available character
    for ch in freq:

        # skip if no tiles left of this character
        if freq[ch] == 0:
            continue

        # choosing this character creates one new sequence
        # example:
        # choose A -> "A"
        # choose A again -> "AA"
        # choose B after that -> "AAB"
        total += 1

        # use the tile (reduce available count)
        freq[ch] -= 1

        # extend the sequence further
        # this recursively builds longer strings
        total += backtrack()

        # restore tile (backtracking step)
        freq[ch] += 1

    return total


print(backtrack())


"""
DRY RUN (AAABBC)

freq = {A:3, B:2, C:1}

call backtrack()

--------------------------------
choose A
total = 1        -> "A"
freq {A:2,B:2,C:1}

    choose A
    total = 1    -> "AA"
    freq {A:1,B:2,C:1}

        choose A
        total = 1 -> "AAA"
        freq {A:0,B:2,C:1}

            choose B
            total = 1 -> "AAAB"
            freq {A:0,B:1,C:1}

                choose B
                total = 1 -> "AAABB"
                freq {A:0,B:0,C:1}

                    choose C
                    total = 1 -> "AAABBC"
                    freq {A:0,B:0,C:0}

                    return 1

                return 2

            choose C
            total = 1 -> "AAABC"

        return ...

    choose B
    total = 1 -> "AAB"

    choose C
    total = 1 -> "AAC"

--------------------------------
choose B
total += 1 -> "B"

choose C
total += 1 -> "C"

--------------------------------

Each "total += 1" counts:
A
AA
AAA
AAAB
AAABB
AAABBC
AAB
AABC
...
B
BA
...
C
CA
...

All unique sequences of all lengths are counted.

Final total = 188
"""