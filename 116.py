# Node class for Perfect Binary Tree
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val        # Value of node
        self.left = left      # Left child
        self.right = right    # Right child
        self.next = next      # Pointer to next right node


# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None      # Initially tree is empty

    # Create a sample perfect binary tree
    def create_sample_tree(self):
        """
                1
              /   \
             2     3
            / \   / \
           4   5 6   7
        """

        # Creating root
        self.root = Node(1)

        # Creating level 1 children
        self.root.left = Node(2)
        self.root.right = Node(3)

        # Creating level 2 children
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)

    # Print tree level by level (BFS using queue)
    def print_level_order(self):
        if not self.root:
            return
        
        queue = [self.root]   # Start BFS with root
        
        while queue:
            level_size = len(queue)   # Number of nodes at current level
            
            for _ in range(level_size):
                node = queue.pop(0)   # Remove front node
                print(node.val, end=" ")
                
                # Add children of current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            print()   # Move to next line after each level

    # Print tree using next pointers
    def print_using_next(self):
        level_start = self.root   # Start from root
        
        while level_start:
            current = level_start
            
            # Traverse current level using next pointers
            while current:
                print(current.val, end=" ")
                current = current.next
            
            print()
            
            # Move to next level (since perfect tree, go to left child)
            level_start = level_start.left


    # Connect next pointers in perfect binary tree
    def connect(self):
        if not self.root:
            return
        
        level_start = self.root   # Start from root level

        # Since it is a perfect binary tree,
        # if left exists, right also exists
        while level_start.left:

            curr = level_start    # Traverse current level

            while curr:

                # 1️⃣ Connect left child to right child
                curr.left.next = curr.right

                # 2️⃣ Connect right child to next node's left child
                # (Only if next node exists)
                if curr.next:
                    curr.right.next = curr.next.left

                # Move horizontally in current level
                curr = curr.next

            # Move down to next level
            level_start = level_start.left

        return self.root
