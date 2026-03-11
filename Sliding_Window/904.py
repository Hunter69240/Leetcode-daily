# This is a sliding window problem because we want the longest *contiguous*
# subarray that contains at most 2 distinct fruit types. Sliding window is
# ideal since we can expand the window with `right` and shrink it with `left`
# whenever the condition (max 2 types) is violated.

# IDEOLOGY:
# - Maintain a dictionary `freq` representing fruit counts inside the window.
# - Move `right` to expand the window and include new fruits.
# - If distinct fruit types exceed 2, shrink the window by moving `left`
#   until the window becomes valid again.
# - The size of a valid window is simply (right - left + 1).
# - Track the maximum size across all valid windows.

fruits = [1, 2, 3, 2, 2]

freq = {}     # fruit → frequency inside current window
left = 0      # start of window
max_len = 0   # best result

for right in range(len(fruits)):
    fruit = fruits[right]

    # Add fruit to dictionary
    if fruit in freq:
        freq[fruit] += 1
    else:
        freq[fruit] = 1

    # Shrink window if more than 2 fruit types
    while len(freq) > 2:
        left_fruit = fruits[left]
        freq[left_fruit] -= 1
        if freq[left_fruit] == 0:
            del freq[left_fruit]
        left += 1

    # Update maximum valid window length
    max_len = max(max_len, right - left + 1)

# ---------------------------------------------------------
# DRY RUN FOR fruits = [1, 2, 3, 2, 2]
#
# right=0 → window=[1]
#   freq={1:1} → valid → max_len=1
#
# right=1 → window=[1,2]
#   freq={1:1,2:1} → valid → max_len=2
#
# right=2 → window=[1,2,3]
#   freq={1:1,2:1,3:1} → invalid (3 types)
#   shrink:
#       remove fruit at left=0 → remove 1
#   freq becomes {2:1,3:1}
#   window=[2,3] → max_len remains 2
#
# right=3 → window=[2,3,2]
#   freq={2:2,3:1} → valid → max_len=3
#
# right=4 → window=[2,3,2,2]
#   freq={2:3,3:1} → valid → max_len=4
#
# FINAL ANSWER: 4
# ---------------------------------------------------------

print(max_len)
