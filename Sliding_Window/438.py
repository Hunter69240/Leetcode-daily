def findAnagrams(s, p):
    # ---------------------------------------------------------
    # PROBLEM:
    # Given two strings s and p, return all starting indices
    # of substrings in s that are anagrams of p.
    #
    # An anagram has the same character frequency as p.
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # STEP 1: Build frequency map of string p
    # freqP stores how many times each character appears in p
    # ---------------------------------------------------------
    freqP = {}
    for ch in p:
        freqP[ch] = freqP.get(ch, 0) + 1

    # ---------------------------------------------------------
    # STEP 2: Initialize sliding window variables
    # i -> left pointer of window
    # j -> right pointer of window
    # freqs -> frequency map of current window in s
    # res -> list to store starting indices of valid anagrams
    # ---------------------------------------------------------
    i = 0
    j = 0
    freqs = {}
    res = []

    # ---------------------------------------------------------
    # STEP 3: Slide the window across string s
    # ---------------------------------------------------------
    while j < len(s):
        # Add current character to window frequency
        freqs[s[j]] = freqs.get(s[j], 0) + 1

        # -----------------------------------------------------
        # STEP 4: Shrink window if its size exceeds len(p)
        # This keeps the window size fixed
        # -----------------------------------------------------
        while (j - i + 1) > len(p):
            freqs[s[i]] -= 1
            if freqs[s[i]] == 0:
                del freqs[s[i]]
            i += 1

        # -----------------------------------------------------
        # STEP 5: Check if current window is an anagram of p
        # If frequency maps match, store starting index
        # -----------------------------------------------------
        if freqs == freqP:
            res.append(i)

        j += 1

    # ---------------------------------------------------------
    # FINAL ANSWER:
    # res contains all starting indices of anagrams
    # ---------------------------------------------------------
    return res
