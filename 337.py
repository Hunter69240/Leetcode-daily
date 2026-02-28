def solution(root):
    # DFS returns:
    # [0] → max money if we ROB this node
    # [1] → max money if we SKIP this node
    
    def dfs(node):
        if not node:
            return [0, 0]   # [rob, skip]

        left = dfs(node.left)
        right = dfs(node.right)

        # If we rob current node:
        # we CANNOT rob its children
        rob = node.val + left[1] + right[1]

        # If we skip current node:
        # we can choose best of rob/skip from children
        skip = max(left[0], left[1]) + max(right[0], right[1])

        return [rob, skip]

    # Return maximum of rob or skip at root
    return max(dfs(root))