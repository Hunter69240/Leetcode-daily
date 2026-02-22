# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Value of the node
        self.left = left      # Left child
        self.right = right    # Right child


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Convert a sorted array into a height-balanced BST.

        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        # Recursive function to build BST
        def build(left_index, right_index):
            
            # Base Case:
            # If left pointer crosses right pointer,
            # there are no elements to form a node.
            if left_index > right_index:
                return None
            
            # Step 1: Find middle element
            # This ensures tree remains height-balanced
            mid = (left_index + right_index) // 2
            
            # Step 2: Create node with middle value
            node = TreeNode(nums[mid])

            # Step 3: Recursively build left subtree
            # Left half of array
            node.left = build(left_index, mid - 1)

            # Step 4: Recursively build right subtree
            # Right half of array
            node.right = build(mid + 1, right_index)

            # Return constructed node
            return node
        
        # Initial call covering entire array
        return build(0, len(nums) - 1)



# ------------------------------
# Driver Code (Testing)
# ------------------------------

if __name__ == "__main__":
    
    # Create a sorted array
    nums = [-10, -3, 0, 5, 9]
    
    # Create Solution object
    sol = Solution()
    
    # Call the function
    root = sol.sortedArrayToBST(nums)
    
    # Print root to verify
    print("Root Value:", root.val if root else None)