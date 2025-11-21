# Finds the length of the longest substring without repeating characters
# Uses the sliding window technique with two pointers and a set to track unique characters
# Efficiently maintains the window by shrinking it when a duplicate is found

s = "abcbd"

charset = set()  # Set to store characters in the current window
left = 0         # Left boundary of the sliding window
res = 0          # Stores the length of the longest valid substring found

for r in range(len(s)):  # Right boundary of the sliding window
    # If the character is already in the current window, shrink the window from the left
    while s[r] in charset:
        charset.remove(s[left])  # Remove the leftmost character
        left += 1                # Move left pointer forward

    charset.add(s[r])  # Add the current character to the window
    res = max(res, r - left + 1)  # Update the result with the max window size

print(len(charset))  # ⚠️ Only prints length of final window, not the result (use print(res) for correct answer)
