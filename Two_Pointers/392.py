def s():
    s = ""
    t = "ahbgdc"

    # ---------------------------------------------------------
    # EXPLANATION:
    # This checks whether string `s` is a SUBSEQUENCE of string `t`.
    #
    # Definition of subsequence:
    # - Characters of `s` must appear in `t`
    # - Order must be preserved
    # - Characters do NOT need to be contiguous
    #
    # Special cases:
    # - If s is empty → always True
    # - If t is empty but s is not → False
    #
    # Two-pointer idea:
    # - j points to current character in s we are trying to match
    # - i iterates over t
    # ---------------------------------------------------------

    if s == "":
        return True
    elif t == "":
        return False
    else:
        j = 0   # pointer for s

        # ---------------------------------------------------------
        # DRY RUN:
        #
        # s = ""
        # t = "ahbgdc"
        #
        # First condition:
        #   s == "" → True
        #
        # Function returns True immediately.
        #
        # (Empty string is a subsequence of any string)
        # ---------------------------------------------------------

        for i in range(len(t)):
            # If current characters match, move pointer in s
            if t[i] == s[j]:
                j += 1

            # If all characters of s are matched
            if j == len(s):
                return True

        # If loop ends and s not fully matched
        return False


a = s()
print(a)
