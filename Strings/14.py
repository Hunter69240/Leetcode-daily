def a():
    # Input list of strings
    strs = ["flower", "flow", "flight"]

    # Edge case: empty list
    if not strs:
        return ""

    # Variable to store the longest common prefix
    prefix = ""

    # Traverse each character index of the first string
    for i in range(len(strs[0])):
        # Current character to compare across all strings
        ch = strs[0][i]

        # Compare this character with the same index in all strings
        for s in strs:
            # If index goes out of bounds or characters mismatch,
            # return the prefix formed so far
            if i >= len(s) or s[i] != ch:
                return prefix

        # If all strings matched this character,
        # add it to the prefix
        prefix += ch

    # Return the final longest common prefix
    return prefix
