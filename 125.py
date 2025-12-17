def s():
    s = "A man, a plan, a canal: Panama"
    i = 0
    j = len(s) - 1

    # ---------------------------------------------------------
    # EXPLANATION:
    # This checks whether the string is a palindrome,
    # considering ONLY alphanumeric characters and
    # ignoring case.
    #
    # Two-pointer approach:
    # - i moves from left to right
    # - j moves from right to left
    #
    # Rules:
    # - If s[i] is not alphanumeric → skip it
    # - If s[j] is not alphanumeric → skip it
    # - Otherwise, compare lowercase characters
    # - If mismatch → return False
    # - If pointers cross → return True
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # DRY RUN:
    #
    # s = "A man, a plan, a canal: Panama"
    #
    # i=0 ('A'), j=29 ('a')
    # 'A'.lower() == 'a'.lower() → match
    # i=1, j=28
    #
    # i=1 (' '): not alphanumeric → i++
    # i=2 ('m'), j=28 ('a')
    # 'm' != 'a' → BUT wait, j moves first
    #
    # j=28 ('a') → ok
    # i=2 ('m'), j=27 ('m')
    # match → i++, j--
    #
    # Continue skipping spaces, commas, and colon.
    #
    # All valid characters match:
    # a m a n a p l a n a c a n a l p a n a m a
    #
    # i crosses j → loop ends
    #
    # FINAL RESULT: True
    # ---------------------------------------------------------

    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

    return True


a = s()
print(a)
