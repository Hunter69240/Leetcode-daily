# Given a list of edges representing a star graph,
# where one node (the center) is connected to all other nodes.
# To find the center, we can simply check which node is common in the first two edges.
edges = [[1, 2], [2, 3], [4, 2]]

# If the first element of the first edge is in the second edge, it's the center.
# Otherwise, the second element of the first edge must be the center.
print(edges[0][0] if edges[0][0] in edges[1] else edges[0][1])
