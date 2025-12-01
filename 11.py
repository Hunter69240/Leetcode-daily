class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two-pointer approach:
        # i starts at left end, j at right end
        i = 0
        j = len(height) - 1

        # vol will store the maximum water area found
        vol = 0

        # Loop until the two pointers meet
        while i < j:
            # Height of the container is limited by the smaller line
            h = min(height[i], height[j])

            # Current area = height * width
            current_area = h * (j - i)

            # Update max area if current area is bigger
            if current_area > vol:
                vol = current_area

            # Move the pointer pointing to the shorter line
            # Because a taller line can potentially form a bigger area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        # Return the maximum area found
        return vol
