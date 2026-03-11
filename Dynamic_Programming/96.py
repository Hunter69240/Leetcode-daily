class Solution:
    def numTrees(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """

        # numTree[i] will store number of unique BSTs that can be formed with i nodes
        # Initialize all values as 1
        # Base cases:
        # numTree[0] = 1 (empty tree)
        # numTree[1] = 1 (single node tree)
        numTree = [1] * (n + 1)

        # Start calculating from 2 nodes up to n nodes
        for nodes in range(2, n + 1):

            total = 0  # total number of BSTs possible with 'nodes' nodes

            # Try every number from 1 to 'nodes' as root
            for root in range(1, nodes + 1):

                # Number of nodes in left subtree
                left = root - 1

                # Number of nodes in right subtree
                right = nodes - root

                # Total trees = (left subtree possibilities) * (right subtree possibilities)
                total += numTree[left] * numTree[right]

            # Store total count for 'nodes'
            numTree[nodes] = total

        # Return total BSTs possible with n nodes
        return numTree[n]
