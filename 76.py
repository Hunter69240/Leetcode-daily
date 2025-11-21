s = "OUZODYXAZV"
t = "XYZ"


# If t is empty, there's nothing to find, return empty string
if t == "":
    print("") 

# Initialize hashmaps for counting characters in t and in current window of s
countT, window = {}, {}

# Build the frequency map for t
for c in t:
    countT[c] = countT.get(c, 0) + 1

# `have` counts how many required characters are satisfied in the current window
# `need` is the total number of unique characters we need to satisfy
have, need = 0, len(countT)

# `res` stores the best window as [left, right]
# `resLen` stores the length of that best window
res, resLen = [-1, -1], float("infinity")

# Left pointer of the sliding window
l = 0

# Right pointer moves through the string `s`
for r in range(len(s)):
    c = s[r]
    window[c] = window.get(c, 0) + 1  # Add current char to window count

    # If the current character count matches required count, increment `have`
    if c in countT and window[c] == countT[c]:
        have += 1

    # Try to shrink the window as long as all requirements are satisfied
    while have == need:
        # If this window is smaller than the previous best, update the result
        if (r - l + 1) < resLen:
            res = [l, r]
            resLen = r - l + 1

        # Remove the leftmost character from window
        window[s[l]] -= 1
        # If this breaks the requirement, decrement `have`
        if s[l] in countT and window[s[l]] < countT[s[l]]:
            have -= 1
        # Move the left pointer to shrink the window
        l += 1

# Unpack final result window
l, r = res

# Return the minimum window substring, or "" if no valid window found
print( s[l:r+1] if resLen != float("infinity") else "")
