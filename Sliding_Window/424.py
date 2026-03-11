# 🔷 Topic: Sliding Window + Character Frequency Count
# 🔍 Problem: Longest Repeating Character Replacement
# 🎯 Goal: Given a string s and an integer k, find the length of the longest substring 
#          that can be transformed into all the same character by replacing at most k characters.

s = "XYYX"
k = 2

count = {}  # Dictionary to count frequency of characters in the current window
res = 0     # To store the maximum length of a valid substring

l = 0       # Left pointer of the sliding window

# Right pointer r moves through the string
for r in range(len(s)):
    # Count the character at the right end of the window
    count[s[r]] = count.get(s[r], 0) + 1

    # Check if current window is invalid:
    # - Window size = r - l + 1
    # - max(count.values()) = frequency of the most common character in the window
    # - If characters to replace > k, shrink the window from the left
    while (r - l + 1) - max(count.values()) > k:
        count[s[l]] -= 1  # Remove the leftmost character from the window count
        l += 1            # Move left pointer to the right

    # Update result with the size of the current valid window
    res = max(res, r - l + 1)

# ✅ Print the length of the longest valid substring found
print(res)
