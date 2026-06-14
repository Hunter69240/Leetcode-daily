res = []  # stores all valid paths from source (0) to target (n-1)

def backtracking(num, current):
    current.append(num)

    if (num == n - 1):
        res.append(current[:])

        current.pop()

        return

    for neighbour in graph[num]:
        backtracking(neighbour, current)

    current.pop()


graph = [[1,2],[3],[3],[]]

n = len(graph)

backtracking(0, [])

print(res)


# ------------------------------------------------------------
# 🔹 WHAT IS THE SUM / PROBLEM ABOUT?
# ------------------------------------------------------------
# We are finding ALL paths from node 0 to node n-1.
#
# Graph is represented as an adjacency list.
#
# Example:
#
# graph = [[1,2],[3],[3],[]]
#
# Means:
#
# 0 → 1
# 0 → 2
# 1 → 3
# 2 → 3
#
# We must return every possible path from source
# node 0 to target node n-1.
#
# This is NOT a shortest path problem.
#
# We are collecting all valid paths.


# ------------------------------------------------------------
# 🔹 WHAT TYPE OF PROBLEM IS THIS?
# ------------------------------------------------------------
# This is a BACKTRACKING problem.
#
# Let’s verify using the 3 key questions:
#
# 1. Does it ask for ALL solutions?
#    ✅ Yes → all paths are required
#
# 2. Do we build the answer piece by piece?
#    ✅ Yes → path grows one node at a time
#
# 3. Can one choice lead to different future choices?
#    ✅ Yes → each node may have multiple neighbors
#
# 👉 Hence: BACKTRACKING


# ------------------------------------------------------------
# 🔹 VARIABLES
# ------------------------------------------------------------
#
# res
#
# Stores all valid paths.
#
# Example:
#
# [
#   [0,1,3],
#   [0,2,3]
# ]
#
#
# current
#
# Stores the path currently being built.
#
# Example:
#
# [0,1]
#
# Means:
# We have travelled:
#
# 0 → 1


# ------------------------------------------------------------
# 🔹 FUNCTION PARAMETERS
# ------------------------------------------------------------
#
# backtracking(num, current)
#
# num
# Current node we are standing on.
#
# current
# Path constructed so far.
#
#
# Example:
#
# backtracking(1, [0,1])
#
# Means:
#
# Current node = 1
#
# Current path:
#
# 0 → 1


# ------------------------------------------------------------
# 🔹 FIRST STEP
# ------------------------------------------------------------
#
# current.append(num)
#
# Add current node into path.
#
# Example:
#
# current = [0]
# num = 1
#
# After append:
#
# current = [0,1]


# ------------------------------------------------------------
# 🔹 BASE CASE
# ------------------------------------------------------------
#
# if num == n - 1:
#
# Reached target node.
#
# Example:
#
# n = 4
#
# Target:
#
# node 3
#
# If num becomes 3,
# current path is complete.
#
# Store it in result.


# ------------------------------------------------------------
# 🔹 WHY current[:] ?
# ------------------------------------------------------------
#
# res.append(current[:])
#
# Stores a copy of the path.
#
# Without copy:
#
# res.append(current)
#
# Every entry in res would point to the same list.
#
# Backtracking would later modify it.
#
# Using [:] freezes the current state.


# ------------------------------------------------------------
# 🔹 WHY current.pop() IN BASE CASE?
# ------------------------------------------------------------
#
# We appended the target node.
#
# Before returning,
# we must restore current to its previous state.
#
# Example:
#
# current = [0,1,3]
#
# pop()
#
# current = [0,1]
#
# So previous recursive call continues correctly.


# ------------------------------------------------------------
# 🔹 EXPLORING NEIGHBORS
# ------------------------------------------------------------
#
# for neighbour in graph[num]:
#
# Visit every outgoing edge from current node.
#
# Example:
#
# graph[0] = [1,2]
#
# Means:
#
# From node 0,
# we can go to:
#
# 1
# 2
#
# Therefore explore both.


# ------------------------------------------------------------
# 🔹 RECURSIVE CALL
# ------------------------------------------------------------
#
# backtracking(neighbour, current)
#
# Move to the neighbor node
# and continue building the path.
#
# Example:
#
# current = [0]
#
# neighbour = 1
#
# Next call:
#
# backtracking(1, [0])


# ------------------------------------------------------------
# 🔹 BACKTRACKING STEP
# ------------------------------------------------------------
#
# current.pop()
#
# Remove current node before returning.
#
# Example:
#
# current = [0,1]
#
# pop()
#
# current = [0]
#
# This allows exploration of another branch.
#
# Example:
#
# 0
# ├── 1
# └── 2
#
# After finishing branch 1,
# remove 1 so branch 2 can be explored.


# ------------------------------------------------------------
# 🔹 RECURSION TREE
# ------------------------------------------------------------
#
# backtracking(0, [])
#
#           0
#         /   \
#        1     2
#        |     |
#        3     3
#
#
# Paths found:
#
# 0 → 1 → 3
# 0 → 2 → 3


# ------------------------------------------------------------
# 🔹 DRY RUN
# ------------------------------------------------------------
#
# backtracking(0, [])
#
# current = [0]
#
# Neighbors:
# 1, 2
#
#
# Go to 1
#
# current = [0,1]
#
# Neighbor:
# 3
#
# current = [0,1,3]
#
# Reached target
#
# res = [[0,1,3]]
#
# Backtrack:
#
# current = [0,1]
#
# Backtrack:
#
# current = [0]
#
#
# Go to 2
#
# current = [0,2]
#
# Neighbor:
# 3
#
# current = [0,2,3]
#
# Reached target
#
# res = [
#   [0,1,3],
#   [0,2,3]
# ]
#
# Backtrack:
#
# current = [0,2]
#
# Backtrack:
#
# current = [0]
#
# Backtrack:
#
# current = []


# ------------------------------------------------------------
# ✅ FINAL OUTPUT
# ------------------------------------------------------------
#
# [
#   [0,1,3],
#   [0,2,3]
# ]
# ------------------------------------------------------------