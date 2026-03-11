if not n:
    return True   # Edge case: empty graph is considered a valid tree

# Build adjacency list for undirected graph
adj = {i: [] for i in range(n)}

for n1, n2 in edges:
    adj[n1].append(n2)
    adj[n2].append(n1)

visit = set()   # keeps track of visited nodes

# DFS to detect cycles and ensure connectivity
def dfs(i, prev):
    # If we reach a node already visited → cycle detected
    if i in visit:
        return False
    
    # Mark current node as visited
    visit.add(i)

    # Explore neighbors
    for j in adj[i]:
        # Skip the edge back to the parent
        if j == prev:
            continue
        # If DFS on neighbor fails (cycle or disconnected), return False
        if not dfs(j, i):
            return False

    return True

# Graph is a valid tree if:
# 1. No cycle exists (DFS returns True)
# 2. All nodes are visited (graph is connected)
return dfs(0, -1) and n == len(visit)
