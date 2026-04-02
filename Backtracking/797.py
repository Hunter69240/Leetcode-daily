# WHY BACKTRACKING:
# - Problem asks for ALL possible paths → exhaustive exploration required
# - Each step (node) gives multiple choices (neighbors)
# - Path is built incrementally
# - Need to undo choices after exploring → classic backtracking

# ABSTRACT:
# - Start from node 0 and build paths step by step
# - At each node, explore all possible neighbors (DFS)
# - Maintain a current path list
# - When target node is reached, store the path
# - Use backtracking (append → recurse → pop) to explore all paths

res = []  # stores all valid paths from source (0) to target (n-1)

def backtracking(num, current):
    current.append(num)  
    # add current node to path
    # builds path step by step

    if (num == n - 1):
        # base case: reached target node

        res.append(current[:])  
        # store a COPY of current path
        # [:] prevents mutation issues due to backtracking

        current.pop()  
        # undo the append before returning
        # restores state for previous calls

        return  
        # stop further exploration from target node

    for neighbour in graph[num]:
        # iterate over all possible next nodes from current node

        backtracking(neighbour, current)
        # recursive call → explore each path

    current.pop()
    # backtracking step
    # remove current node before returning to previous level
    # ensures state is clean for next branch


graph = [[1,2],[3],[3],[]]  
# adjacency list representation:
# 0 → [1,2]
# 1 → [3]
# 2 → [3]
# 3 → []

n = len(graph)  
# total number of nodes → target node = n-1 = 3

backtracking(0, [])  
# start DFS from node 0 with empty path

print(res)  
# final result: all paths from 0 → 3


# DRY RUN:

# Call: backtracking(0, [])
# current = [0]

# From 0 → neighbors: [1,2]

# → go to 1
# current = [0,1]

# From 1 → neighbor: [3]

# → go to 3
# current = [0,1,3]
# reached target → store [0,1,3]
# backtrack → current = [0,1]

# backtrack → current = [0]

# → go to 2
# current = [0,2]

# From 2 → neighbor: [3]

# → go to 3
# current = [0,2,3]
# reached target → store [0,2,3]
# backtrack → current = [0,2]

# backtrack → current = [0]

# backtrack → current = []

# FINAL res:
# [[0,1,3], [0,2,3]]