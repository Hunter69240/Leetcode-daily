candyType = [1,1,2,2,3,3]

cset = set(candyType)  # Convert the list to a set to get unique candy types

counts = len(cset)  # Count of unique candy types
candylen = len(candyType)  # Total number of candies Alice has

# The maximum different types Alice can eat is limited by:
# 1. How many unique types there are (counts), and
# 2. How many candies she is allowed to eat in total (half of all candies)

# So take the minimum of 'counts' and 'candylen // 2' to get the answer.
print(min(counts, candylen // 2))
