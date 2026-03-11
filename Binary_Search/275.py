def a():
    citations = [0, 1, 3, 5, 6]
    n = len(citations)

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if citations[mid] == (n - mid):
            return citations[mid]

        elif citations[mid] < (n - mid):
            low = mid + 1
        else:
            high = mid - 1

    return n - low


s = a()
print(s)


# ---------------------------------------------------------
# EXPLANATION:
# This code computes the H-INDEX using BINARY SEARCH.
#
# H-index definition:
# A researcher has an h-index if:
# - They have at least h papers
# - Each paper has at least h citations
#
# Input condition:
# - citations array is sorted in NON-DECREASING order
# ---------------------------------------------------------

# ---------------------------------------------------------
# KEY OBSERVATION:
#
# At index `mid`:
# - Number of papers with citations >= citations[mid]
#   = n - mid
#
# Compare:
#   citations[mid]  vs  (n - mid)
#
# This comparison decides where the h-index lies.
# ---------------------------------------------------------

# ---------------------------------------------------------
# BINARY SEARCH LOGIC:
#
# 1) If citations[mid] == n - mid
#    → exact h-index found
#
# 2) If citations[mid] < n - mid
#    → not enough citations
#    → need to move RIGHT
#
# 3) If citations[mid] > n - mid
#    → citations are too large
#    → try LEFT for smaller h
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY RETURN (n - low) AFTER LOOP:
#
# If no exact match is found:
# - low points to the smallest index where
#   citations[low] >= n - low
#
# That means:
#   h = n - low
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# citations = [0,1,3,5,6]
# n = 5
#
# low=0, high=4
#
# mid=2 → citations[2]=3, n-mid=3
# match → return 3
#
# FINAL RESULT:
# 3
# ---------------------------------------------------------

# ---------------------------------------------------------
# ANOTHER CASE:
#
# citations = [0,0,0,4,4]
#
# low ends at index 3
# h = 5 - 3 = 2
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(log n)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
