# Initialize parent and rank arrays
par = [i for i in range(n)]   # Each node is initially its own parent
rank = [1] * n                # Rank stores size of each component (starts at 1)

# Find with path compression
def find(n1):
    res = n1
    # Traverse up the parent chain until we reach the root
    while res != par[res]:
        par[res] = par[par[res]]  # Path compression: point node directly to grandparent
        res = par[res]
    return res

# Union by rank (size)
def union(n1, n2):
    p1, p2 = find(n1), find(n2)   # Find roots of both nodes

    if p1 == p2:                  # Already in the same component
        return 0
    
    # Attach smaller tree to larger tree
    if rank[p2] > rank[p1]:
        par[p1] = p2
        rank[p2] += rank[p1]      # Update size of new root
    else:
        par[p2] = p1
        rank[p1] += rank[p2]
    
    return 1                      # Successfully merged two sets

# Count connected components
res = n                           # Start with n components (each node alone)
for n1, n2 in edges:              # Process all edges
    res -= union(n1, n2)          # Subtract when two components merge

return res                        # Final count of connected components
