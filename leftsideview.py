def leftSideView(root):
    if not root:
        return []

    q = collections.deque([root])
    res = []

    while q:
        level_size = len(q)

        # first node of this level is left side view
        left_node = q[0]
        res.append(left_node.value)

        # process the entire level
        for _ in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res
