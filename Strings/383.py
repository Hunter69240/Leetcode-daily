# Problem Type:
# Frequency counting / hashmap / multiset containment
# Goal: check if ransomNote can be constructed using letters from magazine
# Rule: each letter in magazine can be used only once
# Order does NOT matter, only counts matter

ransomNote = "aa"
magazine = "aaab"

def a():
    # freq will store how many times each character appears in magazine
    # example after building: {'a': 3, 'b': 1}
    freq = {}

    # build frequency map of magazine (supply)
    for c in magazine:
        # if char exists -> increment
        # else -> start from 0 then add 1
        freq[c] = freq.get(c, 0) + 1

    # now try to construct ransomNote (demand)
    for c in ransomNote:
        # if char not available or used up -> cannot construct
        if freq.get(c, 0) == 0:
            return False
        
        # consume one character from magazine
        freq[c] -= 1

    # if all characters satisfied -> possible
    return True


print(a())


# -------------------------
# DRY RUN
# -------------------------
# ransomNote = "aa"
# magazine   = "aaab"

# Step 1: build freq from magazine
# c='a' -> {'a':1}
# c='a' -> {'a':2}
# c='a' -> {'a':3}
# c='b' -> {'a':3,'b':1}

# freq = {'a':3,'b':1}

# Step 2: iterate ransomNote

# first 'a'
# freq['a'] = 3 (available)
# decrement -> {'a':2,'b':1}

# second 'a'
# freq['a'] = 2 (available)
# decrement -> {'a':1,'b':1}

# finished loop -> all letters satisfied

# return True


# Time Complexity:
# O(n + m)

# Space Complexity:
# O(1) (at most 26 lowercase letters)